import PySimpleGUI as sg

##-----------Default Button----------------###
bw: dict = {'size:':(7, 2), 'font':('Franklin Gothic Book', 24), 'button_color':("black", "#EEEEEE")}
bt: dict = {'size:':(7, 2), 'font':('Franklin Gothic Book', 24), 'button_color':("black", "#BBBBBB")}
bo: dict = {'size:':(16, 2), 'font':('Franklin Gothic Book', 24), 'button_color':("black", "#ECA527")}

##-------Window Layout-----------------------------------##

layout: list = [
  [sg.Text(size=(70, 1), background_color="#111111")],
  [sg.Text('0.0000', size=(24, 1), justification='right', background_color='white', text_color='red', 
    font=('Franklin Gothic Book', 48), relief='sunken', key="_DISPLAY_")],
  [sg.Text('C', **bt), sg.Button('CE', **bt), sg.Button('%', **bt), sg.Button('/', **bt)],
  [sg.Text('7', **bw), sg.Button('8', **bw), sg.Button('9', **bw), sg.Button('*', **bt)],
  [sg.Text('4', **bw), sg.Button('5', **bw), sg.Button('6', **bw), sg.Button('-', **bt)],
  [sg.Text('1', **bw), sg.Button('2', **bw), sg.Button('3', **bw), sg.Button('+', **bt)],
  [sg.Text('0', **bw), sg.Button('.', **bw), sg.Button('=', **bo, bind_return_key=True)]
]

window: object = sg.Window('電卓サンプル', layout=layout, background_color="#111111", size=(680, 590), return_keyboard_events=True)


#電卓関数
var: dict = {'front':[], 'back':[], 'decimal':False, 'x_val':0.0, 'y_val':0.0, 'result':0.0}

def format_number() -> float:
  return float(''.join(var['front']) + '.' + ''.join(var['back']))

def update_display(display_value: str):
  try:
    window['_DISPLAY_'].update(value='{:,.4f}'.format(display_value))
  except:
    window['_DISPLAY_'].update(value=display_value)

#clickevent
