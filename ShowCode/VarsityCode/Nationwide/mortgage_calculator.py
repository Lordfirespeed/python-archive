class MortgageCalculator:
    house_costs = {
        1: 120_000,
        2: 400_000
    }

    debt_interest_rate = 0.05
    repayment_period_years = 20

    def calculate_eligibility(self, number_of_people_on_mortgage, deposit, salary1, salary2, annual_overpayment):
        house_cost = self.house_costs[number_of_people_on_mortgage]

        try:
            assert number_of_people_on_mortgage in (1, 2)
            assert deposit > 0 and type(deposit) is int
            assert salary1 > 0 and type(salary1) is int
            if number_of_people_on_mortgage == 2:
                assert salary2 > 0 and type(salary2) is int
            else:
                salary2 = 0

            assert annual_overpayment >= 0 and type(annual_overpayment) is int

            assert deposit >= 0.1 * house_cost
        except AssertionError:
            return [0, 0, 0, 0]

        maximum_mortgage = 5 * (salary1 + salary2)

        minimum_annual_payment = (maximum_mortgage * self.debt_interest_rate) / (
                    1 - (1 + self.debt_interest_rate) ** -self.repayment_period_years)
        total_repaid = minimum_annual_payment * self.repayment_period_years

        if annual_overpayment == 0:
            return [maximum_mortgage, round(minimum_annual_payment, 2), round(total_repaid, 2),
                    self.repayment_period_years]

        debt_remaining = maximum_mortgage
        years_to_repay = 0

        while debt_remaining > 0:
            debt_remaining *= (1 + self.debt_interest_rate)
            debt_remaining -= (minimum_annual_payment + annual_overpayment)
            years_to_repay += 1

        return [maximum_mortgage, round(minimum_annual_payment, 2), round(total_repaid, 2), years_to_repay]

