while True:
    num1 = float(input('Digite o primeiro valor: '))
    num2 = float(input('Digite o segundo valor: '))

    print('\nEscolha a operação: \nSoma(+), Subtração(-), Multiplicação(*) e Divisão(/)')
    operacao = input('Digite a operação desejada (+, -, *, /) ou digite "s" para sair: ')

    if operacao.lower() == 's':
        print('Saindo do programa. Até logo!')
        break

    if operacao in ['+', '-', '*', '/']:
        if operacao == '+':
            resultado = num1 + num2
        elif operacao == '-':
            resultado = num1 - num2
        elif operacao == '*':
            resultado = num1 * num2
        elif operacao == '/':
            if num2 != 0:
                resultado = num1 / num2
            else:
                resultado = 'Erro: Não é possível divisão por zero!'
    else:
        resultado = 'Opção inválida. Digite uma operação válida (+, -, *, /) ou "s" para sair.'

    print('\nResultado: ', resultado)
