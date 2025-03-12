from Operadores import soma, subtracao, multiplicacao, divisao
from Utilidade import validar_numero

def calcular():
    print("Selecione a operação:")
    print("1. Adição")
    print("2. Subtração")
    print("3. Multiplicação")
    print("4. Divisão")

    operacao = input("Digite o número da operação (1/2/3/4): ")

    if operacao in ['1', '2', '3', '4']:
        num1 = validar_numero(input("Digite o primeiro número: "))
        num2 = validar_numero(input("Digite o segundo número: "))

        if operacao == '1':
            resultado = soma(num1, num2)
            print(f"{num1} + {num2} = {resultado}")

        elif operacao == '2':
            resultado = subtracao(num1, num2)
            print(f"{num1} - {num2} = {resultado}")

        elif operacao == '3':
            resultado = multiplicacao(num1, num2)
            print(f"{num1} * {num2} = {resultado}")

        elif operacao == '4':
            try:
                resultado = divisao(num1, num2)
                print(f"{num1} / {num2} = {resultado}")
            except ValueError as e:
                print(e)
    else:
        print("Operação inválida.")

if __name__ == "__main__":
    calcular()