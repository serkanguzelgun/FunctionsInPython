#method
list = [1,2,3]
list.append(4)
list.pop()

print(type(list))
print(list)

myString = 'Hello'
print(myString.upper())
print(type(myString))

#fonksiyon
def sayHello(name = 'user'):
    print('Hello ' + name)

sayHello('Çınar')
sayHello('Ada')
sayHello()

def sayHello(name = 'user'):
    return 'Hello ' + name

msg = sayHello('Çınar')
print(msg)

def total(num1,num2):
    return num1 + num2

result = total(10,20)
print(result)

def yasHesapla(dogumYili):
    return 2019 - dogumYili
ageCinar=yasHesapla(2017)
ageSena=yasHesapla(1999)

print(ageCinar)
print(ageSena)

def EmekliligeKacYilKaldi(dogumYili,isim):
    yas = yasHesapla(dogumYili)
    emeklilik = 65-yas
    if emeklilik > 0:
        print(f'emekliliğinize {emeklilik} yıl kaldı')
    else:
        print('Zaten emekli oldunuz')

EmekliligeKacYilKaldi(1983,'Ali')
EmekliligeKacYilKaldi(1955,'İbrahim')
