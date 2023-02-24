# Nomes: André Fernandes Chamis
# RM's: 97891


def get_years_smoking_input() -> float:
    while True:
        try:
            years_smoking_input = float(input(f"{'Tempo como fumante (em anos)'.ljust(35, '.')}: "))
            return years_smoking_input
        except ValueError:
            print('\nPor favor, digite apenas números!\n'
                  'Use . como separador decimal\n')


def get_cigarette_price_input() -> float:
    while True:
        try:
            cigarette_price_input = float(input(f"{'Valor do maço'.ljust(35, '.')}: "))
            return cigarette_price_input
        except ValueError:
            print('\nPor favor, digite apenas números!\n'
                  'Use . como separador decimal\n')


def get_cigarettes_per_day_input() -> float:
    while True:
        try:
            cigarettes_per_day_input = float(input(f"{'Quantidade de maços por dia'.ljust(35, '.')}: "))
            return cigarettes_per_day_input
        except ValueError:
            print('\nPor favor, digite apenas números!\n'
                  'Use . como separador decimal\n')


def convert_years_to_days(amount_of_years: float) -> float:
    amount_of_days_in_months = 30
    amount_of_months_in_years = 12
    return amount_of_years * amount_of_months_in_years * amount_of_days_in_months


def calculate_money_spent_on_cigarettes(
        amount_of_days_smoking: float,
        cigarette_price: float,
        cigarettes_per_day: float
) -> float:
    return amount_of_days_smoking * cigarette_price * cigarettes_per_day


def get_message_based_on_money_spent(money_spent: float) -> str:
    if money_spent < 20_000:
        return f"Com o valor R$ {money_spent:,.2f}, você poderia ter dado entrada em um carro."
    elif 20_000 <= money_spent < 50_000:
        return f"Com o valor R$ {money_spent:,.2f}, você poderia ter comprado um carro popular usado."
    elif money_spent >= 50_000:
        return f"Com o valor R$ {money_spent:,.2f}, você poderia ter comprado um carro zero."


if __name__ == "__main__":
    years_smoking = get_years_smoking_input()
    price_of_cigarette = get_cigarette_price_input()
    amount_of_cigarettes_per_day = get_cigarettes_per_day_input()

    time_smoking_in_days = convert_years_to_days(years_smoking)
    money_spent_on_cigarettes = calculate_money_spent_on_cigarettes(time_smoking_in_days, price_of_cigarette, amount_of_cigarettes_per_day)
    message = get_message_based_on_money_spent(money_spent_on_cigarettes)

    print(f"\n{message}\n")
