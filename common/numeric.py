Huge = None
NegativeHuge = None


class _ArbitrarilyLarge:
    pass


class _Huge(_ArbitrarilyLarge):
    def __ge__(self, other: int | float) -> bool:
        return self > other

    def __gt__(self, other: int | float) -> bool:
        if isinstance(other, _Huge):
            raise TypeError("Can't compare arbitrarily positive values.")

        if isinstance(other, _NegativeHuge):
            return True

        if isinstance(other, int):
            return True

        if isinstance(other, float):
            return True

        raise TypeError

    def __le__(self, other: int | float) -> bool:
        return self < other

    def __lt__(self, other: int | float) -> bool:
        if isinstance(other, _Huge):
            raise TypeError("Can't compare arbitrarily positive values.")

        if isinstance(other, _NegativeHuge):
            return False

        if isinstance(other, int):
            return False

        if isinstance(other, float):
            return False

        raise TypeError

    def __add__(self, other):
        return self

    def __radd__(self, other):
        return self

    def __sub__(self, other):
        if isinstance(other, _ArbitrarilyLarge):
            raise NotImplementedError
        return self

    def __rsub__(self, other):
        if isinstance(other, _ArbitrarilyLarge):
            raise NotImplementedError
        return NegativeHuge

    def __pos__(self):
        return self

    def __neg__(self):
        return NegativeHuge

    def __repr__(self):
        return "Huge"

    def __str__(self):
        return repr(self)


class _NegativeHuge(_ArbitrarilyLarge):
    def __ge__(self, other: int | float) -> bool:
        return self > other

    def __gt__(self, other: int | float) -> bool:
        if isinstance(other, _Huge):
            return False

        if isinstance(other, _NegativeHuge):
            raise TypeError("Can't compare arbitrarily negative values.")

        if isinstance(other, int):
            return False

        if isinstance(other, float):
            return False

        raise TypeError

    def __le__(self, other: int | float) -> bool:
        return self < other

    def __lt__(self, other: int | float) -> bool:
        if isinstance(other, _Huge):
            return True

        if isinstance(other, _NegativeHuge):
            raise TypeError("Can't compare arbitrarily negative values.")

        if isinstance(other, int):
            return True

        if isinstance(other, float):
            return True

        raise TypeError

    def __add__(self, other):
        if isinstance(other, _ArbitrarilyLarge):
            raise NotImplementedError
        return self

    def __radd__(self, other):
        return self

    def __sub__(self, other):
        return self

    def __rsub__(self, other):
        if isinstance(other, _ArbitrarilyLarge):
            raise NotImplementedError
        return Huge

    def __pos__(self):
        return NegativeHuge

    def __neg__(self):
        return Huge

    def __repr__(self):
        return "-Huge"

    def __str__(self):
        return repr(self)


Huge = _Huge()
NegativeHuge = _NegativeHuge()
