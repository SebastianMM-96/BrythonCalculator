"""
Desarrollado por: Sebastián Marroquín Martínez
"""

from browser import document
import math

sign = False

def event(e):

    # Esta función especifica la acción que tomara cada botón 
    # cuando sea presionado. 

    # Utilizaremos dos variables para realizar cada acción:
    # Value y label

    inp = document.select('#calc>input')[0]
    display = value = inp.value

    if value == '0':
        value = ''

    if e.target.tagName == 'SUP':
        target = e.target.parent
    else:
        target = e.target

    label = target.textContent

    if label != '+/-':
        sign = False

    if label == '=':
        try:
            res = eval(display, vars(math))
            value = change_format_result(res)
        except Exception:
            value = 'Error'
    elif label == 'C':
        value = '0'
    elif label == 'CE':
        if len(display) > 1:
            value = display[:-1]
        else:
            value = '0'
    elif label in ('+', '-', '*', '/'):
        value = display + label
    elif label == '+/-':
        global sign
        if not sign:
            value += '-'
            sign = True
        else:
            sign = False
            if len(display) > 1:
                value = display[:-1]
            else:
                value = '0'
    elif label == '.':
        value = display + label
    elif label == 'x2':
        value = display + '**2'
    elif label == '\u221a':
        value += 'sqrt('
    elif label == '\u0025':
        value = display + '/100'
    else:
        value += label

    inp.title = inp.value = value[:80]

def change_format_result(res):
    
    # La función se encarga de dar el formaro adecuado a la salida
    # si es que se trata de un número entero o  de punto flotante. 

    num = int(res)
    if num == res:
        if res < pow(10, 12):
            value = str(res)
        else:
            value = format(res, 'g')
    else:
        res = round(res, 10)
        if res < pow(10, 10):
            value = str(res)
        else:
            value = format(res, 'g')

    return value

for button in document.select('button'):
    button.bind('click', event)