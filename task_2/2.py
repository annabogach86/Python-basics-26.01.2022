class DivByNull:
    def __init__(self, divider, denominator):
        self.divider = divider
        self.denominator = denominator

    @staticmethod
    def divide_by_null(divider, denominator):
        try:
            return (divider / denominator)
        except:
            return (f"Деление на ноль недопустимо")


div = DivByNull(20, 200)
print(DivByNull.divide_by_null(20, 0))
print(DivByNull.divide_by_null(20, 0.1))
print(div.divide_by_null(200, 0))
