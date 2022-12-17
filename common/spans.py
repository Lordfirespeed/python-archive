from typing import Union, overload, Self

Number = Union[int, float]


class SpanAbc:
    pass


class EmptySpan(SpanAbc):
    _instance = None

    def __new__(cls, *args, **kwargs):
        if not cls._instance:
            cls._instance = super(EmptySpan, cls).__new__(cls, *args, **kwargs)
        return cls._instance

    def __sub__(self, other: SpanAbc) -> Self:
        if isinstance(other, SpanAbc):
            return self
        raise TypeError

    def __add__(self, other: SpanAbc) -> SpanAbc:
        if isinstance(other, Span):
            return other
        if isinstance(other, EmptySpan):
            return self
        raise TypeError

    def __eq__(self, other: SpanAbc) -> bool:
        return self is other

    def __repr__(self):
        return "Span<Empty>"


class Span(SpanAbc):
    __slots__ = [
        "start",
        "stop"
    ]

    def __init__(self, start: Number, stop: Number) -> None:
        self.start = start
        self.stop = stop

    def __new__(cls, start: Number, stop: Number, *args, **kwargs):
        if start >= stop:
            return EmptySpan()
        return super(Span, cls).__new__(cls, *args, **kwargs)

    def __sub__(self, other: SpanAbc) -> Self | "SpanCollection" | EmptySpan:
        if isinstance(other, EmptySpan):
            return self  # should copy
        if isinstance(other, Span):
            if self.is_subspan(other):
                return EmptySpan

            if self.is_superspan(other):
                left = Span(self.start, other.start)
                right = Span(other.stop, self.stop)

                return SpanCollection(left, right)

            if self.left_overlaps(other):
                return Span(self.start, other.start)

            if self.right_overlaps(other):
                return Span(other.stop, self.stop)

            return self  # should copy

        raise TypeError

    def __add__(self, other: SpanAbc) -> Self | "SpanCollection":
        if isinstance(other, EmptySpan):
            return self  # should technically copy
        if isinstance(other, Span):
            if self.left_overlaps(other):
                return Span(self.start, max(self.stop, other.stop))

            if self.right_overlaps(other):
                return Span(other.start, max(self.stop, other.stop))

            return SpanCollection(self, other)

        raise TypeError

    def __eq__(self, other: SpanAbc) -> bool:
        if isinstance(other, EmptySpan):
            return False
        if isinstance(other, Span):
            return other.start == self.start and other.stop == self.stop

    def __contains__(self, item: Number) -> bool:
        return self.start <= item < self.stop

    def __repr__(self):
        return f"Span<{self.start}, {self.stop}>"

    def is_superspan(self, other: SpanAbc) -> bool:
        if isinstance(other, EmptySpan):
            return True
        if isinstance(other, Span):
            return self.start <= other.start and self.stop >= other.stop

        raise TypeError

    def is_subspan(self, other: SpanAbc) -> bool:
        if isinstance(other, EmptySpan):
            return False
        if isinstance(other, Span):
            return other.start <= self.start and other.stop >= self.stop

    def left_overlaps(self, other: Self) -> bool:
        """True if 'other' is a span which overlaps such that this span's start is to the left of 'other'."""
        if isinstance(other, Span):
            return self.start <= other.start <= self.stop

        raise TypeError

    def right_overlaps(self, other: Self) -> bool:
        """True if 'other' is a span which overlaps such that this span's start is to the right of 'other'."""
        if isinstance(other, Span):
            return other.start <= self.start <= other.stop

        raise TypeError

    def overlaps(self, other: Self) -> bool:
        if isinstance(other, Span):
            return self.left_overlaps(other) or self.right_overlaps(other)

        raise TypeError


class SpanCollection:
    __slots__ = [
        "_spans"
    ]

    def __init__(self, *spans: [Span]) -> None:
        self._spans: list[Span] = list(spans)
        self._sort()
        self._fully_simplify()

    def _fully_simplify(self) -> None:
        if self.is_in_simplest_form:
            return

        current_index = 0

        while current_index < len(self._spans) - 1:
            if self._spans[current_index].stop >= self._spans[current_index + 1].start:
                start = self._spans.pop(current_index).start
                stop = self._spans[current_index].stop
                self._spans[current_index] = Span(start, stop)
            else:
                current_index += 1

    def _sort(self) -> None:
        if self.is_in_simplest_form:
            return

        self._spans.sort(key=lambda span: span.start)

    @classmethod
    def _index_of_gap_where_fits(cls, value: Number, spans: list[Span]) -> int:
        if value < spans[0].start:
            return 0

        if value > spans[-1].start:
            return len(spans)

        guess = len(spans) // 2

        if spans[guess - 1].start <= value <= spans[guess].start:
            return guess

        if value < spans[guess].start:
            return cls._index_of_gap_where_fits(value, spans[:guess])
        else:
            return guess + cls._index_of_gap_where_fits(value, spans[guess:])

    @property
    def is_in_simplest_form(self):
        return all([left.stop < right.start for left, right in zip(self._spans[:-1], self._spans[1:])])

    def _simplify_index(self, index: int) -> None:
        at = self._spans[index]

        try:
            after = self._spans[index + 1]

            if at.left_overlaps(after):
                self._spans.pop(index + 1)
                at = Span(at.start, max(at.stop, after.stop))
                self._spans[index] = at
        except IndexError:
            pass

        try:
            assert index - 1 >= 0
            before = self._spans[index - 1]

            if at.right_overlaps(before):
                self._spans.pop(index - 1)
                at = Span(before.start, max(at.stop, before.stop))
                self._spans[index - 1] = at
        except AssertionError:
            pass

    def __iadd__(self, other: SpanAbc) -> Self:
        if isinstance(other, EmptySpan):
            return self

        if isinstance(other, Span):
            insert_at = self._index_of_gap_where_fits(other.start, self._spans)
            self._spans.insert(insert_at, other)
            self._simplify_index(insert_at)
            return self

        raise TypeError

    def __isub__(self, other: SpanAbc) -> Self:
        if isinstance(other, EmptySpan):
            return self

        if isinstance(other, Span):
            gap_index = self._index_of_gap_where_fits(other.start, self._spans)

            if gap_index > 0:
                before = self._spans[gap_index - 1]

                self._spans[gap_index - 1] = Span(before.start, min(other.start, before.stop))

                if before.stop > other.stop:
                    self._spans.insert(gap_index, Span(other.stop, before.stop))
                    return self

            current_index = gap_index
            while other.stop > self._spans[current_index].stop:
                if current_index < len(self._spans):
                    self._spans.pop(current_index)
                else:
                    break
            else:
                current = self._spans[current_index]
                current = Span(other.stop, current.stop)
                self._spans[current_index] = current

            return self

        raise TypeError

    def __contains__(self, item: Number) -> bool:
        index_of_span_to_check = self._index_of_gap_where_fits(item, self._spans) - 1
        if index_of_span_to_check < 0:
            return False
        return item in self._spans[index_of_span_to_check]

    def __repr__(self):
        return f"Spans{''.join([f'<{span.start}, {span.stop}>' for span in self._spans])}"
