fa  = eval(input("Follows Account"))
if fa:
    cf = eval(input("close Friend:"))
    if cf:
        print("Not in Close Friend List")
else:
    print("Follow the Account First")
'''


 reg = eval(input("Registered: "))

if reg:
    fee = eval(input("Fee Paid: "))

    if fee:
        print("Tourist Entry Confirmed")
    else:
        print("Fee Pending")
else:
    print("Registration Pending") 
    '''

data = {
           'Mitra':{'status':True,'python':90,'mysql':80,'flask':98},
            'ravi':{'status':False,'python':None,'mysql':None,'flask':None},
            'sita':{'status':True,'python':80,'mysql':70,'flask':90},
            'ram':{'status':True,'python':90,'mysql':80,'flask':98},
            'laxman':{'status':False,'python':None,'mysql':None,'flask':None}
           }
           