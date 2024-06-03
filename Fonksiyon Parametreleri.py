def changeName(n):
    n = 'ada'
name = 'yiğit'
changeName(name)
print(name)

def change(n):
    n[0] = 'istanbul'
sehirler = ['ankara','izmir']
change(sehirler)
print(sehirler)

def change(n):
    n[0] = 'istanbul'
sehirler = ['ankara','izmir']
n = sehirler[:]
n[0] = 'istanbul'
print(sehirler)
print(n)

def add(a,b, c=0):
    return sum((a,b,c))
print(add(10,20))
print(add(10,20,30))

def add(*params):
    print(params[0])
    return sum(params)
print(add(10,20))
print(add(10,20,30,40,50))

def add(*params):
    print(type(params))
    sum = 0
    for n in params:
        sum = sum+n
    return sum
print(add(10,20))
print(add(10,20,30,40,50))

def displayUser(**args):
    print(type(args))
    for key,value in args.items():
        print('{} is {} '.format(key,value))
displayUser(name = 'Çınar', age = 2, city = 'İstanbul')
displayUser(name = 'Ada', age = 12, city = 'Kocaeli',phone = '122324')
displayUser(name = 'Yiğit', age = 14, city = 'Ankara',phone = '123456',mail = 'yigit@mail.com')

def myfunc(a,b,c ,*args,**kwargs):
    print(a)
    print(b)
    print(c)
    print(args)
    print(kwargs)
myfunc(10,20,30,40,50, key1 = 'value1', key2 = 'value2' )