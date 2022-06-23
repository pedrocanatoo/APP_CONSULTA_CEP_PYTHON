import PySimpleGUI as bot
# pip install pysimplegui

def tela_inicial():
    bot.theme('Dark2')

    cep = [
        [bot.Text('Informe um CEP:', font='arial 12', pad=(0,0))],
        [bot.Input(size=(20,0), font='arial 12', pad=(0,0), key='cep')]    
    ]

    coluna1 = [
        [bot.Text('LOGRADOURO:', font='arial 12')],
        [bot.Text('BAIRRO:', font='arial 12')],
        [bot.Text('LOCALIDADE:', font='arial 12')],
        #Localidade
        [bot.Text('UF:', font='arial 12')],
        # UF
        [bot.Text('IBGE:', font='arial 12')],
        #IBGE
        [bot.Text('DDD:', font='arial 12')]
        #DDD 
    ]

    coluna2 = [
        [bot.Input(font='arial 12 bold', key='logradouro', size=(35,1))],
        [bot.Input(font='arial 12 bold', key='bairro', size=(30,1))],
        #Localidade
        [bot.Input(font='arial 12 bold', key='localidade', size=(35,1))],
        # UF
        [bot.Input(font='arial 12 bold', key='uf', size=(4,1))],
        #IBGE
        [bot.Input(font='arial 12 bold', key='ibge', size=(15,1))],
        #DDD 
        [bot.Input(font='arial 12 bold', key='ddd', size=(4,1))]
    ]

    botoes = [
        [bot.Button('Consultar', font='arial 12', size=(10, 1), pad=((0, 15), 0)), 
        bot.CButton('Sair', font='arial 12', size=(8,1))]
    ]

    layout = [ 
        [bot.Text('CONSULTA CEP', font='arial 18 bold')],
        [bot.Column(cep, justification='center', element_justification='center')],
        [bot.Column(coluna1, pad=((0,20), 0)),
        bot.Column(coluna2)],
        [bot.Column(botoes, justification='center')]
    ]

    telaprin = bot.Window('CONSULTA CEP', element_padding=(0, 10), layout=layout, size=(600,500), finalize=True)