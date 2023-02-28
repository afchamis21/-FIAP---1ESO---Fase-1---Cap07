# Nomes: André Fernandes Chamis
# RM's: 97891


def pegar_input_quantidade_de_anos_fumando() -> float:
    while True:
        try:
            input_quantidade_de_anos_fumando = float(input(f"{'Tempo como fumante (em anos)'.ljust(35, '.')}: ").replace(",", "."))
            return input_quantidade_de_anos_fumando
        except ValueError:
            print('\nPor favor, digite apenas números!\n')


def pegar_input_preco_cigarro() -> float:
    while True:
        try:
            input_preco_cigarro = float(input(f"{'Valor do maço'.ljust(35, '.')}: ").replace(",", "."))
            return input_preco_cigarro
        except ValueError:
            print('\nPor favor, digite apenas números!\n')


def pegar_input_quantidade_de_cigarros_por_dia() -> float:
    while True:
        try:
            input_cigarro_por_dia = float(input(f"{'Quantidade de maços por dia'.ljust(35, '.')}: ").replace(",", "."))
            return input_cigarro_por_dia
        except ValueError:
            print('\nPor favor, digite apenas números!\n')


def converter_anos_para_dias(quantidade_de_anos: float) -> float:
    quantidade_de_dias_em_um_mes = 30
    quantidade_de_meses_no_ano = 12
    return quantidade_de_anos * quantidade_de_meses_no_ano * quantidade_de_dias_em_um_mes


def calcular_dinheiro_gasto_com_cigarros(
        quantidade_de_dias_fumando: float,
        preco_do_cigarro: float,
        cigarros_por_dia: float
) -> float:
    return quantidade_de_dias_fumando * preco_do_cigarro * cigarros_por_dia


def selecionar_mensagem_baseada_no_valor_gasto(dinheiro_gasto: float) -> str:
    if dinheiro_gasto < 20_000:
        return f"Com o valor R$ {dinheiro_gasto:,.2f}, você poderia ter dado entrada em um carro."
    elif dinheiro_gasto < 50_000:
        return f"Com o valor R$ {dinheiro_gasto:,.2f}, você poderia ter comprado um carro popular usado."
    elif dinheiro_gasto >= 50_000:
        # Esse bloco poderia ser um else, mas preferi manter assim por legibilidade
        return f"Com o valor R$ {dinheiro_gasto:,.2f}, você poderia ter comprado um carro zero."


if __name__ == "__main__":
    anos_fumando = pegar_input_quantidade_de_anos_fumando()
    preco_do_maco_de_cigarro = pegar_input_preco_cigarro()
    macos_de_cigarro_por_dia = pegar_input_quantidade_de_cigarros_por_dia()

    dias_fumando = converter_anos_para_dias(anos_fumando)
    dinheiro_gasto_em_cigarro = calcular_dinheiro_gasto_com_cigarros(dias_fumando, preco_do_maco_de_cigarro, macos_de_cigarro_por_dia)
    mensagem = selecionar_mensagem_baseada_no_valor_gasto(dinheiro_gasto_em_cigarro)

    print(f"\n{mensagem}\n")
