from lib import easygui
import  sys

CREATE_ACC = 'Create Account'
ACCESS_ACC ='Access Account'
EXIT = 'Exit'
def main():
    r = easygui.buttonbox('Welcome to ELiTE CS BANK \n please select an option','ELiTE CS BANK',(CREATE_ACC,ACCESS_ACC,EXIT))

    if r == EXIT:
        sys.exit()
    elif r == CREATE_ACC:
        createAccount()
    elif r == ACCESS_ACC:
        accessAccount()


def createAccount():
    usr = easygui.multpasswordbox('Creating Account','new Account',('Name','Password'))

    if usr != None:
        for item in usr:
            if len(item) == 0:
                easygui.msgbox('Fields can not be empty')
                createAccount()

        #TODO: create new user here


def accessAccount():
    usr = easygui.multpasswordbox('Access Account','ELiTE CS BANK',('Name','Password'))

    if usr != None:
        for item in usr:
            if len(item) == 0:
                easygui.msgbox('Fields can not be empty')
                accessAccount()

        #TODO: access user account here


    else:
        main()

if __name__ == '__main__':
    main()