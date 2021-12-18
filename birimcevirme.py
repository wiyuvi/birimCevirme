eskibirim = input("Çevirilecek olan birimi giriniz : ")
deger = int(input("Değeri giriniz : "))
yenibirim = input("Çevirmek istediğiniz birimi giriniz :")
thisdict = {
    "km" : 0.001,
    "hm" : 0.01,
    "dam": 0.1,
    "m"  : 1,
    "dm" : 10,
    "cm" : 100,
    "mm" : 1000
}
basamak=(thisdict[yenibirim]/thisdict[eskibirim])
yenibirim=basamak * deger
print(yenibirim)