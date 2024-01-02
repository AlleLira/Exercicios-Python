def obter_ano_nascimento():
    while True:
        try:
            ano_nascimento = int(input('Digite o ano de nascimento (1922-2024): '))
            if 1922 <= ano_nascimento <= 2024:
                return ano_nascimento
            else:
                print('Ano fora do intervalo permitido. Tente novamente.')
        except ValueError:
            print('Por favor, digite um número válido.')

def calcular_idade(ano_nascimento, ano_atual):
    idade = ano_atual - ano_nascimento
    return idade

def main():
    nome_completo = input('Digite seu nome completo: ')
    ano_nascimento = obter_ano_nascimento()

    ano_atual = 2024  # Supondo que o ano atual é 2024

    idade = calcular_idade(ano_nascimento, ano_atual)

    print(f'\nNome: {nome_completo}')
    print(f'Idade: {idade} anos')

if __name__ == "__main__":
    main()
