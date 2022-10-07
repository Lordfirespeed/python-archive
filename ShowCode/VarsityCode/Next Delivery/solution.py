from datetime import datetime, date, time, timedelta


class DeliveryDates:
    working_days_only_mapping = {"True": True, "False": False}
    what_to_return_when_invalid = "Invalid Data"
    bank_holidays = (
        date(year=1900, month=12, day=25),
        date(year=1900, month=12, day=26),
        date(year=1900, month=1, day=1)
    )

    @staticmethod
    def _is_weekend(test_date: date) -> bool:
        return test_date.weekday() >= 5

    @classmethod
    def _is_bank_holiday(cls, test_date: date) -> bool:
        for bank_holiday in cls.bank_holidays:
            if test_date.day == bank_holiday.day and test_date.month == bank_holiday.month:
                return True
        return False

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