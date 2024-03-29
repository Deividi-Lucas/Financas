# Definido função para o programa principal
cor = {'preto': '\033[30m',
       'vermelho': '\033[31m',
       'verde': '\033[32m',
       'amarelo': '\033[33m',
       'azul': '\033[34m',
       'magenta': '\033[35m',
       'ciano': '\033[0;36m',
       'cinza': '\033[37m',
       'branco': '\033[97m',
       'limpa': '\033[m',
       'amarelobrin': '\033[1;93m'}


def linha():
    print(f'{cor["azul"]}~{cor["limpa"]}' * 80)


def menu(texto="CONTROLE FINANCEIRO"):
    linha()
    print(f'{cor["branco"]}{texto.strip():^80}')
    linha()


def leia_numero(texto):
    leitura = ''
    while not leitura.isnumeric():
        leitura = str(input(f'{cor["magenta"]}{texto}')).strip()
        if leitura.isnumeric():
            return int(leitura)
            break
        else:
            menu("ERRO, TENTE NOVAMENTE!")


# a para appeding, acrescentar algo
# w é para criar .
# r é para leitura


def quest(texto):
    while True:
        quest = input(f'{cor["magenta"]}{texto}')
        if quest.strip()[0] in 'Nn':
            break
        elif quest.strip()[0] in 'Ss':
            perg = input(f'{cor["verde"]}O que deseja? ')
            print(
                'Vamos anotar aqui no nosso sistema para está resolvendo este problema.')
            a = open('duvidas.txt', 'a+')
            a.write(perg+'\n')
            break
    print(f'Obrigado por utilizar.{cor["limpa"]}')


def simulacao():
    linha()
    print(
        f'{cor["amarelobrin"]}Olá{cor["ciano"]}, meu nome é {cor["amarelobrin"]}Karla{cor["ciano"]}')
    print(f'Quero que você me responda.')
    valor = leia_numero('Deseja fazer a simulação com que número? ')
    hora = valor / 176
    dia = hora * 8
    semana = dia*7
    if valor == 0:
        print(
            f'{cor["vermelho"]}Não há possibilidade de fazer cálculo com esse valor.')
    else:
        print(f'{cor["ciano"]}Faremos uma simulação de controle financeiro.',
              f'Veja como separamos. ', sep='\n')
        menu()
        print(f'Já que temos R${valor:.2f}',
              f'50% deve ser separado para depesas mensal, o qual seria \tR${valor / 2:.2f}',
              f'30% deve ser para o lazer mensalmente, o qual seria \t\tR${valor*0.3:.2f}',
              f'20% deve ser aplicado em investimento, o qual seria \t\tR${valor*0.2:.2f}',
              f'{cor["amarelobrin"]}{"-=" *40}{cor["limpa"]}',
              f'Colocando uma média horaria de trabalho de 40 horas semanal',
              f'Logo você ganha por hora \t\t\t\t\tR${hora:.2f}',
              f'Ganha por dia \t\t\t\t\t\t\tR${dia:.2f} ',
              f'Ganha por semana \t\t\t\t\t\tR${semana:.2f} ',
              sep='\n')

    linha()
    quest('Deseja algo? [S/N] ')
