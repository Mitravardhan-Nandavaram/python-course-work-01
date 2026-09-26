'''
variable = lambda arguments: expression


wish = lambda name: f"Hello good morning {name}!"
print(wish("sai"))
print(wish("venky"))

gst = lambda price: price+price*0.18
print(gst(2000))
print(gst(3000))

avg = lambda a,b,c: (a+b+c)/3
print(avg(10,20,30))
print(avg(100,200,300))

iseven = lambda a: "even" if a%2==0 else "odd"
print(iseven(10))
print(iseven(11))

larest = lambda a,b,c:a if a>b and a>c else (b if b>c else c)
print(largest(23,33,12))
print(largest(30,20,10))

isvowel = lambda a: "vowel" if a in "aeiouAEIOU" else "consonant"
print(isvowel("u"))
print(isvowel("m"))


l = [1,2,3,4,5,6,7,8]
update = list(map(lambda i: i+10,l))
print(update)


t=(789,421,3444,24235,35430)
discount = list(map(lambda i: i-i*0.3,t))
print(discount)

#odd numbers:

l = [1,2,3,4,5,6,7,8]
update = list(filter(lambda i: i%2!=0,l))
print(update)


t=(789,421,3444,24235,35430)
discount = list(filter(lambda i: i>10000,t)) 
print(discount)


l = ['sowmya@codegnan.com','sowmya@yahoo.com','sowmya@gmail.com','sowmya@outlook.com']
update = list(map(lambda i: i.split('@')[-1],l))
print(update)  


from functools import reduce
l = [4,2,4,64,75,2,4653,8]
res = reduce(lambda sum,i: sum+i,l)
print(res)

resl = reduce(lambda pro,i: pro*i,l)
print(resl)


seats ={'s1':True,
        's2':False,
        's3':True,
        'S4':False,
        's5':True,
        's6':True}

ava = list(filter(lambda i:seats[i]!=True,seats))
print(ava)

products ={
    'eggs':80,
    'sugar':60,
    'salt':20,
    'butter':40,
    'milk':30
}  
res = list(filter(lambda i:products[i]>50,products))
print(res)

'''
products ={
    'eggs':80,
    'sugar':60,
    'salt':20,
    'butter':40,
    'milk':30
}

print(dict(sorted(products.items(),key= lambda i:i[1])))
print(dict(sorted(products.items(),key= lambda i:i[1],reverse=True)))

       