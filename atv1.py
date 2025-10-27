def calcular(num1, num2, operacao):
    """
    Função para calcular dois números com base na operação escolhida.
    Parâmetros:
        num1 (float): primeiro número
        num2 (float): segundo número
        operacao (str): operação desejada ('+', '-', '*', '/')
    Retorna:
        float: resultado da operação
    """
    if operacao == '+':
        return num1 + num2
    elif operacao == '-':
        return num1 - num2
    elif operacao == '*':
        return num1 * num2
    elif operacao == '/':
        if num2 != 0:
            return num1 / num2
        else:
            return "Erro: divisão por zero!"
    else:
        return "Operação inválida!"


# Exemplo de uso:
a = float(input("Digite o primeiro número: "))
b = float(input("Digite o segundo número: "))
op = input("Digite a operação (+, -, *, /): ")

resultado = calcular(a, b, op)
print("Resultado:", resultado)
