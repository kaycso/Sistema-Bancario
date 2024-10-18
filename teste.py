valor = 1234567.89

# Convertendo para string com duas casas decimais e substituindo o ponto por vírgula
valor_formatado = f"{valor:,.2f}".replace(".", ",").replace(",", ".", 1)

# Adicionando o símbolo monetário
valor_formatado = "R$ " + valor_formatado

print(valor_formatado)  # Saída: R$ 1.234.567,89