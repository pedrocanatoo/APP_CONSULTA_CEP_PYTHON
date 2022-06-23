from asyncio import events
from optparse import Values
from consultar_cep import *
from interface_grafica import *

tela_inicial()

while True:
    window, event, values = bot.read_all_windows()

    if event == bot.WIN_CLOSED:
        break

    if event == 'Consultar':
        try: 
            logradouro = consulta(values['cep'])['logradouro']
            bairro = consulta(values['cep'])['bairro']
            localidade = consulta(values['cep'])['localidade']
            uf = consulta(values['cep'])['uf']
            ibge = consulta(values['cep'])['ibge']
            ddd = consulta(values['cep'])['ddd']

            window['logradouro'].update(logradouro)
            window['bairro'].update(bairro)
            window['localidade'].update(localidade)
            window['uf'].update(uf)
            window['ibge'].update(ibge)
            window['ddd'].update(ddd)
        except:
            bot.Popup('Verifique se o campo "CEP" foi preenchido corretamente\n'
                      '                        ou se ta conectado a internet', font='arial 12', title='ERRO')