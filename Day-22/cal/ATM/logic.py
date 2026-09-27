data ={
    1234567:{'name':"Mitra",'pin':1234,'balance':10000,'history':[]},
    2345678:{'name':"Pramod",'pin':2345,'balance':20000,'history':[]},
    3456789:{'name':"supri",'pin':8498,'balance':30000,'history':[]}
}

def logib():
    global acc_num
    acc_num = int(input("Enter your account number: "))
    pin = int(input("Enter the pin: "))
    if acc_num in data and data[acc_num]['pin']== pin:
        print("Login successful")
        return True
    else:
        print("Invalid Login")

def menu():
    print(f"welcome to the ATM, {data[acc_num]['name']}")
    print('[c]heck Balance')
    print('[D]eposite')
    print('[W]ithdraw')
    print('[V]iew Transactions')
    print('[E]xit')


def checkbalance():
    print(f'Hello {data[acc_num]["name"]},')
    print("Current Balance:",data[acc_num]["balance"],end='\n\n')
    
def deposit():
    amount = int(input("Enter the amount to withdraw: "))
    if data[acc_num]["balance"]>=amount:
        data[acc_num]["balance"]-=amount
        data[acc_num]["history"].append(f"{amount} is withdraw")
        porint(f"{amount} is withdraw successfully")
        checkbalance()
        else:
            print("Insufficient balance")

def viewtransaction():
    if data[acc_num]["history"]:
        print("======= Trasaction History =======")
        for i in data[acc_num]["history"]:
            print(i)
        else:
            print("========End of the History========")
        else:
            print("No Trasaction History")
         
