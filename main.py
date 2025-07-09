import random

print("labas")
print('labas')

skaicius = 25

print(skaicius)

skaicius = 24.3

print(skaicius)

# print("uzkomentuokime sia eilute")
'''
asdfg dar 
sadfg vienas 
sadfg komentaras
'''

tekstas = "labas, as esu tekstas"
print(tekstas)

ar_galima = True
ar_buvo = False

skaicius = 14
if skaicius == 14:
    print("wau,")
    print("atspejai is pirmo karto")
else:
    print("haha neatspejai")

print("zemiau salyginio sakinio")

skaicius = 32

if skaicius == 1:
    print("vienas")
elif skaicius == 2:
    print("du")
elif skaicius == 3:
    print("trys")
elif skaicius == 4:
    print("keturi")
else:
    print("penki")

if skaicius != 20:
    print("skaicius nelygus 20")

if skaicius > 10 and skaicius < 40:
    print("skaicius " + str(skaicius) + " tarp 10 ir 40")

if 10 < skaicius < 40:
    print("skaicius " + str(skaicius) + " tarp 10 ir 40")

if skaicius == 50 or skaicius == 40:
    print("skaicius " + str(skaicius) + " tarp 10 ir 40")

# case
# 	when shipping_price = 0 then 'nemokamai'
# 	when shipping_price <=10 then 'vidutiniskai'
# 	when shipping_price >10 then 'brangiai'
# end as "shipping_price_groups"

# if shipping_price == 0:
#     print('nemokamai')
# elif shipping_price <= 10:
#     print('vidutiniskai')
# else:
#     print('brangiai')

rnd_num = random.randint(5, 14)
print(rnd_num)

num1 = random.randint(0,4)
num2 = random.randint(0,4)

print(num1, num2)
print(num1 + num2)

salis = "Lietuva"
miestas = "Kaunas"

print("salies pavadinimas yra " + salis + " o miestas - " + miestas)
print("salies pavadinimas yra ", salis, "o miestas - ", miestas)
