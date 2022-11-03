import PySimpleGUI as sg
import random

def Window():
    sg.theme('Dark Blue 3')  # please make your windows colorful

    layout = [[sg.Text('Which website will you sign up:')],
              [sg.Input(key='site')],
              [sg.Text('Which length do you want:')],
              [sg.Input(key='length')],
              [sg.Text('') , sg.Text(key='result')],
              [sg.Button('Generate'), sg.Button('Save'), sg.Button('Exit')]]

    window = sg.Window('Password Generator', layout)
    password_ =''
    while True:  # Event Loop
        event, values = window.read()
        print(event, values)
        if event == sg.WIN_CLOSED or event == 'Exit':
            break
        if event == 'Generate':
            password_ = GeneratePassword(values['length'])
            window['result'].update(password_)

        if event == 'Save':
            Save(values['site'], password_)
            window['result'].update('Successfully Saved')

    window.close()

def GeneratePassword(length):
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    password = ''

    i = 0
    while (i < int(length)):
        i += 1
        a = random.randint(0, 1)

        if (a == 0):
            password += str(random.randint(0, 9))
        else:
            password += alphabet[random.randint(0, 25)]

    return password
def Save(website, password):

    writedoc = website + ' password is == ' + password +'\n'
    with open('password.txt', 'a') as f:
        f.writelines(writedoc)
    
Window()