class IncomeTaxCalculator:
    def _init_(self):

        self.total_salary = None

    def calculate_tax(self): 
        slabs = [(250000, 0.05), (500000, 0.20), (1000000, 0.30)] 
        tax = 0

        remaining_income = self.total_salary

        for i in range(len(slabs)-1, -1, -1):

            if remaining_income > slabs[i][0]:

                slab_income = remaining_income - slabs[i][0]

                slab_tax = slab_income * slabs[i][1]

                tax += slab_tax

                remaining_income -= slab_income

        return tax

    def print_tax_details (self):
        while True:
            try:
                self.total_salary = float(input("Enter your total salary: "))
                if self.total_salary < 0:
                    print("Salary cannot be negative. Please enter a positive number.")
                    break
                else:
                    print(f"Total Salary: {self.total_salary}")
                    print(f"Calculated Income Tax: {self.calculate_tax()}")
 
            except ValueError:
                print("Invalid input! Please enter a valid number (int or float).")


if __name__ == "__main__":
    tax_calculator = IncomeTaxCalculator()
    tax_calculator.print_tax_details()