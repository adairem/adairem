# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

#1 pdf 1.soru
'''
toplam=0
for i in range(1,11):
    toplam=toplam+i
    
print("Sayıların toplamı=",toplam)
'''

#2.soru
'''
tektoplam=0
for i in range(1,11):
    if (i%2==1):
        tektoplam=tektoplam+i
print("Tek Sayıların Toplamı",tektoplam)
'''      

#3.soru
'''
ctoplam=0
ttoplam=0

for i in range(1,11):
    if (i%2==0):
        ctoplam=ctoplam+i
    else:
        ttoplam=ttoplam+i
print("Tek Toplam",ttoplam)
print("Çift Toplam",ctoplam)
'''

#4.soru
'''
a=int(input("Bir rakam giriniz=")) 
Toplam=0
while a>0:
      Toplam=Toplam+a
      a=a-1
      
print("Rakamların toplamı",Toplam)
'''
#5.soru
'''
sayi=int(input("Fksı alıncak sayıyı giriniz="))
c=1
while sayi>0:
    c=c*sayi
    sayi=sayi-1
print("Faktöriyel=",c)
'''
#6.soru
#7.soru
'''
soru_sayisi = 10
dogru_cevap_puanı = 10
yanlis_cevap_puanı = -5
dogru_cevap_sayisi = int(input("Doğru cevapların sayısını girin: "))
yanlis_cevap_sayisi = int(input("Yanlış cevapların sayısını girin: "))
toplam_puan = (dogru_cevap_puanı * dogru_cevap_sayisi) + (yanlis_cevap_puanı * yanlis_cevap_sayisi)
print("Toplam puan:", toplam_puan)
'''
#8.soru
'''
print("2.Dereceden Bir Denklemin Kökünü Bulma2")
a=int(input("a : "))
b=int(input("b : "))
c=int(input("c : "))
 
delta=b**2-4*a*c
 
if (delta < 0):
  print ("denklemin reel kökü yok.")
elif (delta == 0):
  print ("birinci kök = ikinci kök :", (-b/2*a))
else:  
  x1=(-b-delta**0.5)/(2*a)
  x2=(-b+delta**0.5)/(2*a)
  print("Birinci Kök : {}\nİkinci Kök : {}".format(x1,x2))       
'''

#9.soru
'''
import random

sayi=random.randint(0, 100)
print(sayi)
for i in range(0,3):
    tahmin=int(input("Tahmin Giriniz="))
    if sayi==tahmin:
        print(i,".Doğru bildiniz")
        break
    else:
        print("Tekrar deneyiniz")
'''
#10.soru
'''
ptoplam=0
ntoplam=0
toplam=0
sifirmi=True
while sifirmi:
    sayi=int(input("Bir sayı Giriniz=="))
    if sayi<0:
        ntoplam=ntoplam+1
        toplam=toplam+sayi
    elif sayi>0:
        ptoplam=ptoplam+1
        toplam=toplam+sayi
    else:
        sifirmi=False
ortalama=toplam/(ptoplam+ntoplam)
print(ptoplam,"Adet pozitif",ntoplam,"Adet Negatif",ortalama,"ortalama")
'''

#11.soru
'''
sayi=int(input("Sayı giriniz=="))
for i in range(2,sayi):
    if sayi%i==0:
        print("Sayı Asal Degildir.")
        break
    else:
        print("Sayı Asaldır.")
'''

#12.soru
'''
i=0
kelime=input("Kelime Giriniz=")
sesli="aeıioöuü"
for x in kelime:
    if x in sesli:
        i+=1    
print(i)
'''
#13.soru
'''
metin=input("Bir metin girin : ")
adet = 0
for harf in metin:
  if harf =="a":
    adet+=1
 
print("Girinlen ifadede {} tane a vardır".format(adet))
'''
#14.soru
'''
kelime=input("Kelime Giriniz=")
sesli="aeıioöuü"
sesli_sayac=0
for Harf in kelime:
    if Harf in sesli:
        sesli_sayac+=1
        
print("Sesli harf sayısı=",sesli_sayac)
print("Sessiz harf sayısı=",len(kelime)-sesli_sayac)
'''

#2.pdf 1.soru------------------------------------------------------------------------------------------------------------------
'''
vize=int(input("Vize Notunu Giriniz="))
final=int(input("Final Notunu Giriniz="))
ortalama=(vize*0.4)+(final*0.6)
if ortalama<=40:
    print("Kaldınız")
else:
    print("Geçtiniz")
'''

#2.soru
'''
eb=0
ek=0

sifirMi=True
while sifirMi:
    sayi=int(input("Bir Sayı Giriniz="))
    if sayi==0:
        sifirMi=False
    elif sayi<ek+1:
        ek=sayi
    elif sayi>eb-1:
        eb=sayi
        
print("En küçük",ek)
print("En büyük",eb)
'''

#3.soru
'''
a=(input("Kullanıcının İsmini giriniz=")) 
uzunluk=0
for x in a:
  uzunluk=uzunluk+1 
print("metin uzunluğu",uzunluk)        
'''

#4.soru
'''
taban=int(input("Tabanı Giriniz="))
us=int(input("Üs giriniz="))
c=1
for i in range(0,us):
    c=c*taban
print(taban,us,"=",c)
'''

#5.soru
'''
ad_soyad=input("Adınızı ve Soyadınızı girin=")
yas=int(input("Yaşınızı giriniz="))
if yas>40:
    print("Yaş sınırını aştınız.")
    print("Mülaket başarısız")
else:
    c=input("İngilizce ve ya Fransızca biliyor musunuz? E/ H")
    if c=="h"or c=="hayır":
        print("Dil şartını saglamıyorsunuz")
        print("Mülakat başarısız")
        
    elif c=="e" or c=="Evet":
        print("TEBRİKLER MÜLAKAT BAŞARILI")
        
    else:
        print("Yanlış Giriş")
'''

#6.soru
'''
while True:
  sifre =input("4 basamaklı bir şifre girin :")
  if len(sifre) == 4:#String ifadesinin uzunluğunu yani karakter sayısını verir
    print("Şifreniz kaydedildi")
    break
  print("Şifreniz 4 karakter olmalıdır")        
'''

#7.soru
'''
kal_saat=int(input("Kaldıgınız saati giriniz="))
tucret=0
if kal_saat<=1:
    tucret=5
elif (kal_saat>1) and (kal_saat<=5):
    tucret=kal_saat*4
elif kal_saat>5:
    tucret=kal_saat*3
    
print("Ödenecek para=",tucret)
'''

#8.soru
'''
kelime = input("Bir kelime girin: ")
kelime_buyuk = kelime.upper()
print("Tüm harfler büyük:", kelime_buyuk)
kelime_kucuk = kelime.lower()
print("Tüm harfler küçük:", kelime_kucuk)
kelime_a_e = kelime.replace("a", "e")
print("\"a\" harfleri \"e\" harfine çevrilmiş:", kelime_a_e)
kelime_uzunluk = len(kelime)
print("Kelimenin uzunluğu:", kelime_uzunluk)
'''

#9.soru
'''
parola = input("Parolanızı girin: ")
if any(char in "çÇğĞıİöÖşŞüÜ" for char in parola):
  print("Parolada Türkçe karakter kullanılamaz!")
'''
#10.soru
'''
metin1=input("Bir yazı girin=")
metin2=input("Bir yazı girin=")

for i in metin1:
    if i not in metin2:
     print(i)
'''
#------------------------------------------------------------------------------------------------------------------------
#3.pdf 1.soru
'''
rastgele_sayilar = [random.randint(0, 100) for _ in range(10)]

# 50'den küçük sayıların sayısını bulun
kucuk_sayilar = sum(1 for sayi in rastgele_sayilar if sayi < 50)

# Rastgele sayıları ve 50'den küçük sayıların sayısını ekrana yazdırın
print("Rastgele sayılar:", rastgele_sayilar)
print("50'den küçük sayıların sayısı:", kucuk_sayilar)
'''

'''
#sınıfta yapılan

liste=[]
toplam=0
eleman_sayısı=int(input("Bir sayı giriniz="))
for i in range(0,eleman_sayısı):
    eleman=int(input("Eleman giriniz="))
    toplam=toplam+eleman
    liste.append(eleman)
print(liste)



dizi = [1, 2, 3, 2, 1, 3, 4, 5, 5]
eleman_sayilari = {}
for eleman in dizi:
  if eleman in eleman_sayilari:
    eleman_sayilari[eleman] += 1
  else:
    eleman_sayilari[eleman] = 1

print("Eleman sayıları:", eleman_sayilari)
'''

#2.soru
#0 ile 100 arasında yine rastgele olacak şekilde 10 adet sayı oluşturup bu kez bu sayılardan 50’den küçük olanları bir liste içerisine aktaran Python uygulamasını yazınız.
'''
import random
rastgele_sayilar = [random.randint(0, 100) for _ in range(10)]
kucuk_sayilar = [sayi for sayi in rastgele_sayilar if sayi < 50]
# Filtrelenmiş listeyi ekrana yazdırın
print("50'den küçük sayılar:", kucuk_sayilar)
'''
'''
#sınıfta yapılan
liste=[]
eleman_sayisi=int(input("Eleman sayısı Giriniz="))
toplam=0
for i in range(0,eleman_sayisi):
    eleman=int(input("Eleman giriniz"))
    liste.append(eleman)
    
for i in range(0,eleman_sayisi):
    toplam=toplam+eleman_sayisi[i]
        print(liste)

'''

#3.soru
'''
import random
rastgele_sayilar = [random.randint(0, 100) for _ in range(10)]
ortalama = sum(rastgele_sayilar) / len(rastgele_sayilar)
yuksek_sayilar = sum(1 for sayi in rastgele_sayilar if sayi > ortalama)
print("Ortalamadan yüksek sayıların sayısı:", yuksek_sayilar)
'''
'''sınıfta yapılan
iste=[]
liste1=[]
sayi=int(input("Eleman giriniz="))
for i in range(0,sayi):
    eleman=int(input("Eleman giriniz"))
    
'''
#4
'''
dizi = [1, 2, 3, 2, 1, 3, 4, 5, 5]
eleman_sayilari = {}
for eleman in dizi:
  if eleman in eleman_sayilari:
    eleman_sayilari[eleman] += 1
  else:
    eleman_sayilari[eleman] = 1

print("Eleman sayıları:", eleman_sayilari)
'''
'''
#5
liste1 = input("İlk listeyi girin: ").split()
liste2 = input("İkinci listeyi girin: ").split()
if liste1 == liste2:
  print("İki liste aynıdır.")
else:
  print("İki liste aynı değildir.")
  
'''
#-------Sınava Çalışma-------------------------------------------
'''
sayi1 = input('1. Sayı : ')
sayi2 = input('2. Sayı : ')
toplam=float(sayi1)+float(sayi2)
print("Toplam :{0} ".format(toplam))
'''
'''
vize = int(input('Vize Notunuz : '))
final = int(input('Final Notunuz : '))
ortalama=((vize)*0.3)+((final)*0.7)
print("Ortalama :{0} ".format(ortalama))
'''
'''
boy = float(input("Boy (m):"))
kilo = int(input("Kilo (kg):"))
endeks = kilo/(boy*boy)
if endeks <=18:
 print("\n zayıf VKİ:{}".format(endeks))
elif endeks > 18 and endeks <=25 :
 print("\n kilolu VKİ:{}".format(endeks))
elif endeks > 25 and endeks <=30:
 print("\n obez VKİ:{}".format(endeks))
elif endeks > 30:
 print("\n ciddi obez VKİ:{}".format(endeks))
'''
'''
yas = int(input('Yaşınız : '))
if(yas<18):
 print("Yaşınız Ehliyet almak İçin Uygun Değil")
else:
 print("Yaşınız Ehliyet almak İçin Uygun")
'''
'''
for i in range(1,101):
    if(i%3==0 or i%5==0):
        print(i)
'''
'''
s=int(input("sayı gir"))
for i in range(1,s+1):
    print(i)
'''
'''
isim=input("Adınızı Girin ")
sayac=0
while sayac < len(isim):
 print(isim[sayac])
 sayac += 1
else:
 print("Adının harflerini listeledim.")
'''
'''sy=0
s=int(input("Sayı giriniz"))
for i in range(2,s):
    if (s%i==0):
        print("Asal degil")
        break
    else:
        print("aSAL")
        break'''
'''      
s=int(input("Sayı Giriniz"))
tk=0
ct=0
for i in range(1,s+1):
    if(s%i==0):
        ct=ct+i
    else:
        tk=tk+i
print("Cift Toplam",ct) 
print("Tek Toplam",tk)       
'''
'''
yeniMaas=0
maas=int(input("Maaşı Gir : "))
zam=int(input("Zam Oranı(%) : "))
yeniMaas=(maas+(maas*zam)/100)
print("Zamlı Maaş :",yeniMaas)
'''
#listeler-------------------------------------------------------
'''
import random as rn
liste=[]
toplam=0
for i in range(0,10):
    sayi=rn.randint(0,100)
    liste.append(sayi)
eleman_sayisi=len(liste)
for i in range(0,eleman_sayisi):
    toplam=toplam+liste[i]
ortalama=toplam/eleman_sayisi
ortalama_ustu=[]
for i in range(0,10):
    if liste[i]>ortalama:
        ortalama_ustu.append(liste[i])
print(liste)
print(ortalama)
print(ortalama_ustu)
'''
'''
import random as rn
liste1=[]
toplam=0
for i in range(0,10):
    sayi=rn.randint(0,100)
    liste1.append(sayi)
print(liste1)
liste1.sort(reverse=False)
print(liste1)
'''
'''
cumle="Belirli bir düzende otomatik listeler oluşturmak için liste üreteçleri kullanılır."
kelime=cumle.split(" ")
for i in kelime:
    if len(i)>7:
        print(i)
'''  
      
#---------------------------------------------------------------------
#Fonksiyonlar
'''
def faktoriyel(n):
    if n == 0:
        return 1
    else:
        return n * faktoriyel(n-1)

print(faktoriyel(5))  # 1
'''
'''
def ortalama_disi_aktar(dizi):
    ortalama = sum(dizi) / len(dizi)
    disi = [sayi for sayi in dizi if sayi < ortalama or sayi > ortalama]

    return disi

print(ortalama_disi_aktar([1, 2, 3, 4, 5])) 
'''
'''
liste = [ 'GeeksforGeeks' , 'Geeky' , 'Bilgisayarlar' , 'Algoritmalar' ]
aranan = input ( "aranan harfi giriniz" )

def  metin_ara (liste,a):
     liste1 = [x for x in liste if aranan in x ]  
     return liste1
print(len(metin_ara(liste,aranan)))  
'''
'''
cumle = "Belirli bir düzende otomatik listeler oluşturmak için liste üreteçleri kullanılır."
karakter_sayisi = int(input("Karakter sayısını girin" ))

def  bul (cumle ,a):    
    liste = cumle .split ( " " )
    for i   in liste :
          if len(i) >a:
            print (i)          
bul (cumle , karakter_sayisi)
'''
'''
def faktoriyel(a):
    carpim=1
    for i in range(1,a+1):
        carpim=carpim*i
    print (carpim)
    
faktoriyel(6)
'''
#büyük küçük harf
'''
metin="RETURN ifadesi bir fonsiyonda geriye deger döndürür"
def string_kontol(x):
    buyuk=[]
    kucuk=[]
    for i in x:
        if i.upper():
            buyuk.append(i)
        elif i.lower():
            kucuk.append(i)
        else:
            pass
    return kucuk,buyuk
s1,s2=string_kontol(metin)
print("küçük harf",s1)
print("büyük harf",s2)
'''

#gönerilen metni ters cevir
'''
def ters_çevir(s):
    x=""
    index=len(s)
    while index>0:
        x+=s[index-1]
        index=index-1
    return x
print(ters_çevir("123sdfgh"))
'''
#mükemmel sayı
'''
def mükemmelsayı(a):
 toplam=0   
 for i in range(1,a):
    if(a%i == 0):
        toplam +=i
        
    if(a == toplam):
     print("Mükemmel Sayidir.")
    else:
     print("Mükemmel Sayi Degildir")
'''
''' 
def faktoriyel(a):
    carpim=1
    for i in range(1,a+1):
     carpim *=i
     return(carpim)
     return a * faktoriyel(carpim)
'''    
#taban üs
'''
def us_al(taban,us):
    carpim=1
    for i in range(1,us+1):
        carpim*=taban
    print(carpim)

us_al(5,3)
'''
#REQURSİVE
'''
def us_al(taban,us):
    if taban==1:
        return 1
    elif us==0:
        return 1
    else :
        return taban*us_al(taban, us-1)
    
print(us_al(5, 3))
'''
'''
def faktoriyel(n):
   if n==0:
       return 1
   elif n==1:
       return 1
   else:
       return n*faktoriyel(n-1)
sayi=int(input("sayı giriniz"))
fak=faktoriyel(sayi)
print(faktoriyel)
'''