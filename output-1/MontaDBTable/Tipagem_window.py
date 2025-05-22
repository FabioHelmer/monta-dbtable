from PySimpleGUI import PySimpleGUI as sg
import json

def open_window(theme):
    
    sg.theme(theme)
    
    #dados
    file = open("config.json",encoding='UTF-8')
    data = json.load(file)
    json_formatado = json.dumps(data, indent=4)
    

    # layout 
    layout =[
        [sg.Multiline(size=(60, 10), key='tipos', default_text=json_formatado)],
        [sg.Button('Salvar', key='salvar')]
    ]
    
    #janela
    janela = sg.Window('Configurações/Tipagem', layout, modal=True)
    
    #ler os eventos
    while True:
        eventos, valores = janela.read()
        if eventos == sg.WINDOW_CLOSED:
            break
        if valores['tipos'].strip()=='':
            sg.Popup('Insira um valor válido                               ', keep_on_top=True)
        else:
            file = open("config.json", 'w' ,encoding='UTF-8')
            data = json.loads(valores['tipos'])
            file.write(json.dumps(data, indent = 4) )
            file.close()
            janela.close()
            break
       