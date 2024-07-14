
valor_concurso = float(input("Digite o valor do concurso (em reais): "))

primeiro_ganhador = valor_concurso * (46 / 100)
segundo_ganhador = valor_concurso * (32 / 100)
terceiro_ganhador = valor_concurso - primeiro_ganhador - segundo_ganhador

print("O primeiro ganhador receberá:", primeiro_ganhador, "reais")
print("O segundo ganhador receberá:", segundo_ganhador, "reais")
print("O terceiro ganhador receberá:", terceiro_ganhador, "reais")