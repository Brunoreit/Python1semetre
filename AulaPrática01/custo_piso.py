comprimento = float(input("digite o comprimento em metro"))
largura= float(input("digite a largura"))
M_quadrado= comprimento*largura
preco_Mquadrado= float(input("digite o preço do metro quadrado em R$"))
custo_forro= M_quadrado*preco_Mquadrado
print (f"o custo total para forrar o piso da sala é: {custo_forro}")
