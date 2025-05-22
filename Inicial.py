import PySimpleGUI as sg
from executa_transformacao import executa_transformacao
import Tipagem_window

def exec_teste(texto):
    teste =  texto.split("\n")
    i = 1
    for item in teste:
        print(f'{i} - {item}')
        i+=1

def open_window():
    
    my_theme = 'Reddit'

    sg.theme(my_theme)
    
    menu_def = [['Configurações', ['Tipagem']]]

    #layout
    layout = [
        [sg.Menu(menu_def)],
        [sg.Text('Create table', size=(72,1)), sg.Text('DBTable')],
        [sg.Multiline(size=(80, 40), key='inctrl', enable_events=False), sg.Multiline(size=(80, 40), key='outctrl', enable_events=False)],
        [sg.Text("", size=(32,1))],
        [sg.Text("", size=(127,1)), sg.Button('Executar', ), sg.Button('Cancelar')]
    ]
    

    #janela
    window = sg.Window("DBTable", layout)

    #ler os eventos
    while True:
        eventos, valores = window.read()
        if eventos == sg.WINDOW_CLOSED or eventos == 'Cancelar' :
            break
        
        if eventos == 'Tipagem':
            Tipagem_window.open_window(my_theme)
        if eventos == 'Executar':
            inctrl = valores['inctrl']
            if inctrl.strip() != '':
                dbtable = executa_transformacao(inctrl)
                print(dbtable)
                window['outctrl'].update(dbtable)
            else:
                sg.Popup('Insira um valor válido                               ', keep_on_top=True)
            
      
    window.close()

open_window()


