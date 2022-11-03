import PySimpleGUI as sg
import sqlite3 as lite

def Window():
    sg.theme('Light Blue')  # please make your windows colorful

    layout = [[sg.Text('Username:')],
              [sg.Input(key='username')],
              [sg.Text('Password:')],
              [sg.Input(key='password')],
              [sg.Text('') , sg.Text(key='result')],
              [sg.Button('Login'), sg.Button('Sign Up'), sg.Button('Exit')]]

    window = sg.Window('Login Window', layout)
    password_ =''
    while True:  # Event Loop
        event, values = window.read()
        print(event, values)
        
        if event == sg.WIN_CLOSED or event == 'Exit':
            break

        if event == 'Login':
            print(values['username'], values['password'])

            if databaselogincheck(values['username'], values['password']) == True:
                window['result'].update('Login Successful')
                sg.popup("Welcome to AUT'S program")
                break

            else:
                window['result'].update('Access Denied')


        if event == 'Sign Up':
            databasesignup(values['username'], values['password'])
            window['result'].update('SignUp Successful')


    window.close()

def databasesignup(username, password):
    dbConnect = lite.connect("UserData.db")
    dbCursor = dbConnect.cursor()

    pack = [(username), (password)]

    dbCursor.execute("""INSERT INTO logindata VALUES(?, ?)""", pack)

    dbConnect.commit()
    dbConnect.close()

def databaselogincheck(username, password):
    dbConnect = lite.connect("UserData.db")
    dbCursor = dbConnect.cursor()

    testpword = dbCursor.execute("SELECT password FROM logindata WHERE username = ?", [username]).fetchall()
    

    if testpword[0][0] == password:
        return True
    else:
        return False

    dbConnect.commit()
    dbConnect.close()

Window()
