from datetime import datetime, date, time, timedelta
from functools import cache


class DeliveryDates:
    working_days_only_mapping = {"True": True, "False": False}
    what_to_return_when_invalid = "Invalid Data"
    bank_holidays = (
        date(year=1900, month=1, day=1),
        date(year=1900, month=12, day=25),
        date(year=1900, month=12, day=26)
    )  # needs to be sorted chronologically

    @staticmethod
    def _is_weekend(test_date: date) -> bool:
        return test_date.weekday() >= 5

    @classmethod
    @cache
    def _bank_holidays_near(cls, year: int) -> [date]:
        expected_bank_holidays = []
        for year in range(year-1, year+2):
            for bank_holiday in cls.bank_holidays:
                expected_bank_holidays.append(date(year=year, month=bank_holiday.month, day=bank_holiday.day))

        actual_bank_holidays = []
        for bank_holiday in expected_bank_holidays:
            while cls._is_weekend(bank_holiday) or bank_holiday in actual_bank_holidays:
                bank_holiday += timedelta(days=1)
            actual_bank_holidays.append(bank_holiday)
        return actual_bank_holidays

    @classmethod
    def _is_bank_holiday(cls, test_date: date) -> bool:
        return test_date in cls._bank_holidays_near(test_date.year)

    @classmethod
    def _is_working_day(cls, test_date: date, working_days_only: bool) -> bool:
        if working_days_only and cls._is_weekend(test_date):
            return False

        if cls._is_bank_holiday(test_date):
            return False

        return True

    @classmethod
    def _next_working_day(cls, from_day: date, working_days_only: bool) -> date:
        if cls._is_working_day(from_day, working_days_only):
            return from_day

        return cls._next_working_day(from_day + timedelta(days=1), working_days_only)

    @classmethod
    def _calculate_delivery_date(cls, order_datetime: datetime, lead_days: int, dispatch_cutoff: time,
                                 working_days_only: bool) -> date:
        order_date = order_datetime.date()
        if order_datetime.time() >= dispatch_cutoff:
            lead_days += 1

        expected_delivery_date = order_date + timedelta(days=lead_days)
        actual_delivery_date = cls._next_working_day(expected_delivery_date, working_days_only)
        return actual_delivery_date

    @classmethod
    def calculate_delivery_date(cls, order_datetime: str, lead_days: str, dispatch_cutoff: str,
                                working_days_only: str) -> str:
        try:
            order_datetime = datetime.strptime(order_datetime, "%d/%m/%Y %H:%M:%S")
        except ValueError:
            return cls.what_to_return_when_invalid

        try:
            lead_days = int(lead_days)
            assert lead_days >= 0
        except (ValueError, AssertionError):
            return cls.what_to_return_when_invalid

        try:
            dispatch_cutoff = datetime.strptime(dispatch_cutoff, "%H:%M:%S").time()
        except ValueError:
            return cls.what_to_return_when_invalid

        try:
            working_days_only = cls.working_days_only_mapping[working_days_only]
        except KeyError:
            return cls.what_to_return_when_invalid

        delivery_date = cls._calculate_delivery_date(order_datetime, lead_days, dispatch_cutoff, working_days_only)
        return delivery_date.strftime("%d/%m/%Y")