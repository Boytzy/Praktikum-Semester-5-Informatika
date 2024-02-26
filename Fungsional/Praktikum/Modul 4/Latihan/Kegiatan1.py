# curry function
def perkalian(a):
    def dengan(b):
        return a * b
    return dengan

#HOF
hasiL_kali =  perkalian(5)
print(hasiL_kali(3))

#Curyying
hasiL_kali = perkalian(5)(3)
print(hasiL_kali)