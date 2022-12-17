from common.vectors import Vector2
import re
from dataclasses import dataclass, field
from typing import ClassVar, Self


@dataclass
class Sensor:
    position: Vector2 = field(compare=True)
    closest_beacon_position: Vector2 = field(compare=False)

    @property
    def radius(self) -> int:
        return (self.closest_beacon_position - self.position).manhattan

    @property
    def diameter(self) -> int:
        return self.radius * 2 + 1

    sensor_data_pattern: ClassVar[re.Pattern] = re.compile(r"Sensor at x=(-?\d+), y=(-?\d+): closest beacon is at x=(-?\d+), y=(-?\d+)")

    @classmethod
    def from_data(cls, sensor_data: str) -> Self:
        match = re.match(cls.sensor_data_pattern, sensor_data)
        assert match is not None
        groups = match.groups()
        position = Vector2(int(groups[0]), int(groups[1]))
        closest_beacon_position = Vector2(int(groups[2]), int(groups[3]))
        return cls(position, closest_beacon_position)

    def span_at_y(self, y: int) -> range:
        y_difference = abs(self.position.y - y)
        if y_difference > self.radius:
            raise ValueError("Sensor has no span at provided y value")
        span_radius = (self.radius - y_difference)
        return range(self.position.x - span_radius, self.position.x + span_radius + 1)


class Solution:
    considering_y_coordinate = 2000000

    def __init__(self, sensor_datas: [str]) -> None:
        self.sensors = [Sensor.from_data(sensor_data) for sensor_data in sensor_datas]
        self.beacon_positions = set([sensor.closest_beacon_position for sensor in self.sensors])

    @classmethod
    def combine_ranges(cls, left_ranges: [range], right_ranges: [range]) -> [range]:
        combined = []
        for left_range in left_ranges:
            has_been_combined = False
            for right_index, right_range in list(enumerate(right_ranges))[::-1]:
                if right_range.start <= left_range.start <= right_range.stop:
                    left_range = (range(right_range.start, max(left_range.stop, right_range.stop)))
                    right_ranges.pop(right_index)
                    has_been_combined = True
                    continue

                if left_range.start <= right_range.start <= left_range.stop:
                    left_range = (range(left_range.start, max(left_range.stop, right_range.stop)))
                    right_ranges.pop(right_index)
                    has_been_combined = True
                    continue

            if has_been_combined:
                right_ranges.append(left_range)
            else:
                combined.append(left_range)
        combined += right_ranges
        return combined

    @classmethod
    def simplify_ranges(cls, ranges: [range]) -> [range]:
        if len(ranges) == 1:
            return ranges

        midpoint = len(ranges) // 2
        left_reduced = cls.simplify_ranges(ranges[:midpoint])
        right_reduced = cls.simplify_ranges(ranges[midpoint:])

        return cls.combine_ranges(left_reduced, right_reduced)

    def beacon_positions_on_row(self) -> [int]:
        return [position.x for position in filter(lambda position: position.y == self.considering_y_coordinate, self.beacon_positions)]

    def positions_spanned_on_row(self) -> [range]:
        unsimplified_spans = []
        for sensor in self.sensors:
            try:
                unsimplified_spans.append(sensor.span_at_y(self.considering_y_coordinate))
            except ValueError:
                pass
        simplified_spans = self.simplify_ranges(unsimplified_spans)

        return simplified_spans

    def positions_with_no_beacon_on_row(self) -> [int]:
        spans = self.positions_spanned_on_row()
        beacon_positions = self.beacon_positions_on_row()

        beacons_in_spans = 0
        for beacon_position in beacon_positions:
            for span in spans:
                if span.start <= beacon_position < span.stop:
                    beacons_in_spans += 1
                    break

        return sum([span.stop - span.start for span in spans]) - beacons_in_spans


if __name__ == "__main__":
    with open(r"input.txt") as input_file:
        sensor_datas = [line.strip() for line in input_file.readlines()]

    solver = Solution(sensor_datas)
    result = solver.positions_with_no_beacon_on_row()
    print(f"Positions that cannot contain a beacon in row at y={solver.considering_y_coordinate}: {result}")
