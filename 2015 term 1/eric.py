__author__ = 'Administrator'from lib import easyguiimport badHard_drive=[]## def index_of_account(name)#     for a in range (len(Hard_drive)):#         account = Hard_drive[a]#         print (str(account))def index_of_account(name):    for w in Hard_drive:        print(str(w))        if(w.AccountName==name):            return Truedef savetofile(list):    filestring = ''    for item in list:        filestring +=str(item)+'\n'        print(filestring)        myfiles =open('accountsfile.txt','w')        myfiles.write(filestring)        myfiles.close()def getFromfile():    try:        ret=[]        dan = open('accountsfile.txt','r')        lines =dan.readlines()        print(lines)        for line in lines:            print(line)            cleanline =line.replace('\n','')            accountInfo =cleanline.split(':')            name = accountInfo[0]            balance =accountInfo[1]            newAccount =bad.Banky(name,balance)            ret.append(newAccount)    except:        print('Error file not found')        return []    return retHard_drive =getFromfile()while True:        r=easygui.buttonbox("what would you like to do?",                      "Banky Account System",                      ("create account","login","exit"))        print(r)        if r=="create account":            name = easygui.enterbox("enter your name","creating account")            amt =easygui.enterbox("enter your ini_amount",'creating account')            account = bad.Banky(name,amt)            print (str(account))            Hard_drive.append(account)            savetofile(Hard_drive)            print(Hard_drive)        elif r=="login":            n = easygui.enterbox("logging into account","please enter your account name")            account_index =index_of_account(n)            if account_index > -1:                myAccount =Hard_drive[account_index]                opt=easygui.buttonbox("choose an option","welcome to Banky",                                  ('withdraw','deposit','check balance','exit'))                if opt =="withdraw":                  myAccount.deposit()                elif opt=="withdraw":                    amt = easygui.enterbox('How much do you want to deposit','Deposit')                    myAccount.withdraw(int(amt))                    print(str(myAccount))                # elif opt =="withdraw":                #     myAccount.withdraw                #                # elif opt=="withdraw":                #     amt = easygui.enterbox('How much do you want to withdraw','Withdraw')                #     myAccount.withdraw(int(amt))                #     print(str(myAccount))                #     pass            else:                easygui.msgbox('sorry')                print("account_index")                pass        else:            exi= easygui.buttonbox("are you sure you want to leave ",'thank you',                              ('exit','stay'))            if exi == 'exit':                exit()