TelephoneBook = {'Amal':111,'Mohammed':2222222222,"Khadijah":3333333333,'Abdullah':4444444444,'Rawan':5555555555,'Faisal':6666666666,'Layla':7777777777}

def AddFunc(NewName,Phone): #function add a new item to the dictionary
    TelephoneBook[NewName] = Phone

def Add(): # let the user add the new Item
    newN = input('Enter New Name :')
    newP = input('Enter New number :')
    AddFunc(newN,newP)

def Search(): #Search for a number by the name
    name = input('Enter Name :')
    print(name,'\'s number is :',TelephoneBook[name])

serves = None

while serves != 0: #Provides services until the user chooses to exit the program
    print()
    print('1- Print the dictionary')
    print('2- Add a phone number to the dictionary')
    print('3- Search for a number by the name')
    print('0- To Exit')
    print()
    serves = int(input('write the number next to the serves that you want :'))

    if serves == 1:
        print(TelephoneBook)

    elif serves == 2:
        Add()

    elif serves == 3:
        Search()

    else:
        print('Sorry! we don\'t provide tihs serves')