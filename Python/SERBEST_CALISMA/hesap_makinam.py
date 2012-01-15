#!/usr/bin/env python
# -*- coding: utf8 -*-
# http://www.serbestdoviz.com/

from __future__ import division
import math
import urllib2


print " \n\t\tHESAP MAKİNAM"

isim=raw_input("\nADINIZI GİRİNİZ: ")

if bool(isim) == True :
	print "\nHOŞGELDİNİZ SAYIN",isim
	
else:
	print "\nBİR İSİM GİRMENİZ GEREKİYOR."
	quit()
	
islem1= "\n(1) TOPLAMA"
islem2= "\n(2) ÇIKARMA"
islem3= "\n(3) ÇARPMA"
islem4= "\n(4) BÖLME"
islem5= "\n(5) ÜST ALMA"
islem6= "\n(6) KARAKÖK BULMA"
islem7= "\n(7) LOGARİTMA İŞLEMLERİ"
islem8= "\n(8) 10 TABANINDA LOGARİTMA İŞLEMLERİ"
islem9= "\n(9) MOD İŞLEMİ(KALAN BULMA) "
islem10= "\n(10) TEKLİK-ÇİFTLİK DURUMU"
islem11= "\n(11) FAKTORİYEL İŞLEMLERİ"
islem12= "\n(12) TRİGONOMETRİK İŞLEMLER(SİN,COS,TAN,COT)"
islem13= "\n(13) MUTLAK DEĞER BULMA"
islem14= "\n(14) AÇISAL İŞLEMLER(DERECEYİ RADYANA ÇEVİRMEK)"
islem15= "\n(15) AÇISAL İŞLEMLER(RADYANI DERECEYE ÇEVİRMEK)"
islem16= "\n(16) SAYIYI OCTAL(8'LİK SAYI SİSTEMİ) CİNSİNDEN YAZMA"
islem17= "\n(17) SAYIYI HEXADECİMAL (16 'LIK SAYI SİSTEMİ) CİNSİNDEN YAZMA"
islem18="\n(18)VERİLEN PARA MİKTARINI DOLAR YADA EURO'YA ÇEVİRME"



def hata1() :
	try:
		sonuc5= sayi7 / sayi8
		print sonuc5
	except ZeroDivisionError:
		print chr(7)
		print "\n*** SAYILAR 0 'A BÖLÜNMEZLER! ***"
		
		
def cikis() :
	
	if dur == "q" or dur == "Q" :
		print "\nHOŞÇAKAL"
		quit()
		
	else :
		pass
		

	
		
def cikarma() :
	
	d=input("\nilk sayıyı giriniz =  ")
	aa=[]
	print "\n***LÜTFEN SAYILAR ARASINA VİRGÜL KOYARAK YAZINIZ***"
	a=input("\ndiğer sayıları giriniz : ")
	aa.extend(a)
	
	
	for a in aa:
		d= d - a
	print d
		
	
def carpma() :
	print "\n***LÜTFEN SAYILAR ARASINA VİRGÜL KOYARAK YAZINIZ***"
	
	carpma=[]
	carp=input("\nsayıları giriniz : ")
	carpma.extend(carp)
	a = 1
	
	for carp in carpma:
		a = a * carp
	print a

def bolme() :
	c=input("\nilk sayıyı giriniz = ")
	bb=[]
	print "\n***LÜTFEN SAYILAR ARASINA VİRGÜL KOYARAK YAZINIZ***"
	b=input("\ndiğer sayıları giriniz : ")
	bb.extend(b)
	
	
	for b in bb:
		c = c / b
	print c
	
	
			
def durum() :
	
	if sayi % 2 == 0 :
		print "\nGİRDİĞİNİZ SAYI ÇİFTTİR."
	if sayi % 2 != 0 :
		print "\nGİRDİĞİNİZ SAYI TEKTİR."	

		
	
def para() :
	
	ni=raw_input("\nPARANIZI EURO MI *(E)* YOKSA DOLARA MI *(D) ÇEVİRMEK İSTİYORSUNUZ (E/D) : ")
	na=input("\nPARA MİKTARINIZI GİRİNİZ (TL): ")

	page=urllib2.urlopen("http://www.serbestdoviz.com/")
	text=page.read()
	
	if ni=="d" or ni=="D":

                #burası satış fiyatı için
		a=text.find('"usd2"')
		b=text.find(">",a)+1
		c=text.find("<",b)
		#bu sıranın altındaki alış fiyatı için
		
		a1=text.find('"usd"')
		b1=text.find(">",a1)+1
		c1=text.find("<",b1)
		
		kur=float(text[b:c])
		kur2=float(text[b1:c1])
		
		print "\nDOLAR IN SATIŞ FİYATI=%f TL"%(kur)
		print "\nDOLAR IN ALIŞ FİYATI=%f TL"%(kur2)
		
		paran=na/kur
		
		print "\nPARANIZIN DOLAR KARŞILIĞI",paran,"$"
	
		
	if ni == "e" or ni == "E" :
                
                #burası satış fiyatı için
		d=text.find('"eur2o"')
		e=text.find(">",d)+1
		f=text.find("<",e)
		#bu sıranın altındakiler alış fiyatı için
		
		d1=text.find('"euro"')
		e1=text.find(">",d1)+1
		f1=text.find("<",e1)
		
		kur_euro=float(text[e:f])
		kur2_euro=float(text[e1:f1])
		
		print "\nEURO NUN SATIŞ FİYATI=%f TL"%(kur_euro)
		print "\nEURO NUN ALIŞ FİYATI=%f TL"%(kur2_euro)
		
		paran=na/kur_euro
		
		print "\nPARANIZIN EURO KARŞILIĞI",paran,"€"
		
		
		
	
trig1= "\n(1)SİNÜS(SİN) DEĞERİ"
trig2= "\n(2)COSİNÜS(COS) DEĞERİ"
trig3= "\n(3)TANJANT(TAN) DEĞERİ"
trig4= "\n(4)COTANJANT(COT) DEĞERİ"


def son() :
	while True :
		print trig1; print trig2 ; print trig3 ; print trig4
		
		global cik
		
		cik=raw_input("\n**bu DÖNGÜDEN ÇIKMAK İÇİN 'q' tuşuna VEYA devam etmek için \n\nİŞLEM NUMARASINI  GİRİNİZ= **")
		
		if cik == "q" :
			print "\nTRİGONOMETRİK İŞLEMLER DÖNGÜSÜNDEN ÇIKTINIZ"
			break
		
		else :
			pass
		
		
		
		if cik == "1" :
			ooo=[]
			oo=input("\ndereceyi giriniz = ")
			ooo.append(oo)
			print "\nGİRDİĞİNİZ DERECENİN SİNÜS DEĞERİ = %f "%math.sin(math.radians(oo))
			
		if cik == "2" :
			aaa=[]
			aa=input("\ndereceyi giriniz = ")
			aaa.append(aa)
			print "\nGİRDİĞİNİZ DERECENİN COSİNÜS DEĞERİ = %f "%math.cos(math.radians(aa))
		
		
		if cik == "3" :
			bbb=[]
			bb=input("\ndereceyi giriniz = ")
			bbb.append(bb)
			print "\nGİRDİĞİNİZ DERECENİN TANJANT DEĞERİ = %f "%math.tan(math.radians(bb))
		
		if cik == "4" :
			ccc=[]
			cc=input("\ndereceyi giriniz = ")
			ccc.append(cc)
			print "\nGİRDİĞİNİZ DERECENİN COTANJANT DEĞERİ = %f "%(1 / math.tan(math.radians(cc)))

	
	
while True :

	print islem1
	print islem2
	print islem3
	print islem4
	print islem5
	print islem6
	print islem7
	print islem8
	print islem9
	print islem10 ; print islem11 ; print islem12; print islem13 ; print islem14 
	print islem15 ; print islem16 ; print islem17 ; print islem18
	
	
	dur=raw_input("\n**çıkmak için 'q' harfini VEYA devam etmek için HERHANGİ BİR HARF giriniz= **")
	cikis()
	soru=raw_input("\nYAPILACAK İŞLEMİN NUMARASINI SEÇİNİZ : ")		
	

	if soru == "1":
		sayilar = []
		print "\n(***SAYILARIN ARASINA VİRGÜL KOYARAK VE BOŞLUK BIRAKMAYARAK YAZINIZ***)"
		sayi=input("\nTOPLAMAK İSTEDİĞİNİZ SAYILARI GİRİNİZ : ")
		sayilar.extend(sayi)
		print "\nGİRDİĞİNİZ SAYILAR TOPLAMI : ",sum(sayilar)
		
		
	
	if soru == "2":
		cikarma()
		
		
	if soru == "3":
		carpma()
	
	
	if soru == "4" :	
		bolme()

	if soru == "5":
		sayi9=input("\nbir sayı girin : ")
		print sayi9
		kuvvet=input("\nsayının alacağı kuvveti yazın : ")
		print sayi9,"**",kuvvet,"=", sayi9**kuvvet

		
	if soru == "6" :
		karakokler=[]
		karakok = input("\nbir sayı giriniz = ")
		karakokler.append(karakok)
		print "\nGİRDİĞİNİZ SAYININ KARAKÖKÜ = %f"%(math.sqrt(karakok)) 
	
	
	if soru == "7" :
		logaritmik1=[]
		logaritmik2=[]
		logaritma1=input("\nlogaritması alınacak sayıyı giriniz = ")
		logaritma2=input("\nlogaritmanın taban sayısını giriniz = ")
		logaritmik1.append(logaritma1)
		logaritmik2.append(logaritma2)
		print "\nİŞLEMİN SONUCU = %f "%(math.log(logaritma1,logaritma2))
		
	
	if soru == "8" :
		print " \n**NOTTTT= BU BÖLÜMDE YAPACAĞINIZ İŞLEMLERDE LOGARİTME TABANI 10 OLARAK \nKABUL EDİLİR**"
		logaritmika=[]
		logaritmaa=input("\nlogaritması alınacak sayıyı giriniz=")
		logaritmika.append(logaritmaa)
		print "\nİŞLEMİN SONUCU = %f"%(math.log10(logaritmaa))
	
		
	if soru == "9":
		sayi10=input("\nilk sayıyı girin : ")
		print sayi10
		sayi11=input("\nikinci sayıyı girin : ")
		print sayi10,"/",sayi11,"=", sayi10%sayi11
	
	
	if soru == "10":
		sayi=input("\nbir sayı girin : ")
		durum()
	
	if soru == "11":
		faktor=[]
		faktoriyal=input("\nbir sayı giriniz = ")
		faktor.append(faktoriyal)
		print "\nGİRDİĞİNİZ SAYININ FAKTÖRÜ = %d "%(math.factorial(faktoriyal))
		
	if soru == "12" :
		son()
		
	
	if soru == "13" :
		mutlaklar=[]
		mutlak = input("\nNEGATİF yada POZİTİF bir sayı giriniz : ")
		mutlaklar.append(mutlak)
		print "\nGİRDİĞİNİZ SAYININ MUTLAK DEĞERİ = %d"%(math.fabs(mutlak))
		
	
	if soru == "14" :
		acilar=[]
		aci = input("\ndereceyi giriniz = ")
		acilar.append(aci)
		print "\nGİRDİĞİNİZ DERECENİN RADYAN CİNSİ = %f "%(math.radians(aci))
		
		
	if soru == "15" :
		acilar2=[]
		aci2 = input("\nradyanı giriniz = ")
		acilar2.append(aci2)
		print "\nGİRDİĞİNİZ RADYANIN DERECE CİNSİ = %f"%(math.degrees(aci2))
		
	
		
	if soru == "16" :
		nolar = []
		no=input("\nbir sayı girin : ")
		nolar.append(no)
		print "\nGİRDİĞİNİZ SAYININ OCTAL DEĞERİ = %o  "%(no)

	
	if soru == "17" :
		nular = []
		nu = input("\nbir sayı girin : ")
		nular.append(nu)
		print "\nGİRDİĞİNİZ SAYININ HEXADECİMAL DEĞERİ  =  %X "%(nu)
		

	if soru == "18" :
		para()


	
		#     BETÜL SARAL               	
	
		
		

	
