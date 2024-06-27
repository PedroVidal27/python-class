def calculator():
    print("Calculadora")
    print("Escolha uma operação:")
    print("1. Adição")
    print("2. Subtração")
    print("3. Multiplicação")
    print("4. Divisão")

    operation = input("Insira o número da operação que gostaria de iniciar: ")

    if operation not in ['1', '2', '3', '4']:
        print("Operação Inválida")
        return

    num1 = float(input("Insira o primeiro número: "))
    num2 = float(input("Insira o segundo número: "))

    if operation == '1':
        result = num1 + num2
        print(f"O resultado de {num1} + {num2} é: {result}")
    elif operation == '2':
        result = num1 - num2
        print(f"O resultado de {num1} - {num2} é: {result}")
    elif operation == '3':
        result = num1 * num2
        print(f"O resultado de {num1} * {num2} é: {result}")
    elif operation == '4':
        if num2 == 0:
            print("Erro: Divisão por zero não permitida")
        else:
            result = num1 / num2
            print(f"O resultado de {num1} / {num2} é: {result}")

if __name__ == "__main__":
    calculator()
