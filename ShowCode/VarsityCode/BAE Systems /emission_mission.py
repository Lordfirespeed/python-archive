from __future__ import annotations
from dataclasses import dataclass


@dataclass
class Project:
    operating_hours: set[int]
    consumption: int

    @staticmethod
    def time_range_from_string(time_range_string: str) -> range:
        if "-" not in time_range_string:
            start = int(time_range_string)
            return range(start, start + 1)

        start_string, stop_string = time_range_string.split("-")
        start, stop = int(start_string), int(stop_string)
        return range(start, stop)

    @classmethod
    def from_project_string(cls, project_string: str) -> Project:
        time_ranges_string, consumption_string = project_string.split(";")
        time_ranges = [cls.time_range_from_string(string) for string in time_ranges_string.split(",")]
        operating_hours = set.union(*map(lambda time_range: set(time_range), time_ranges))
        consumption = int(consumption_string)
        return cls(operating_hours, consumption)

    def get_consumption_at_hour(self, hour: int) -> int:
        if hour not in self.operating_hours:
            return 0

        return self.consumption


class BAE_Emissions:
    def forecast(self, projects, renewable_forecast):
        # Your code goes here
        project_objects = map(Project.from_project_string, projects)

        total_emissions = 0

        for hour in range(24):
            renewable_production = renewable_forecast[hour]
            total_consumption = sum([project.get_consumption_at_hour(hour) for project in project_objects])
            emissive_production = total_consumption - renewable_production
            total_emissions += emissive_production

        return total_emissions
