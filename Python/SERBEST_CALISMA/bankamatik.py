#!/usr/bin/env python
# -*- coding: utf8 -*- 

from __future__ import division

print " \n\t\tSARALBANK"

isim=raw_input("\nADINIZI GİRİNİZ : ")

if bool(isim) != True :
	print "\nKULLANICI ADINIZI GİRMENİZ GEREKİYOR."
	quit()
	
else :
	print "\nTEŞEKKÜRLER"
	
	parola=raw_input("\nŞİFRENİZİ GİRİNİZ : ")

if bool(parola) != True :
	print "\nŞİFRENİZİ GİRMEZSENİZ HESABINIZA ERİŞEMEZSİNİZ"
		
	parola=raw_input("\nŞİFRENİZİ GİRİNİZ : ")

if bool(parola) != True :
	print "\nŞİFRENİZİ GİRMEZSENİZ HESABINIZA ERİŞEMEZSİNİZ"	
	quit()
	
if len(parola) <= 4 :
	print "\n ŞİFRENİZ EN AZ 5 KARAKTERLİ OLMALIDIR."
		
	parola=raw_input("\nŞİFRENİZİ GİRİNİZ : ")

if len(parola) <= 4 :
	print "\n ŞİFRENİZ EN AZ 5 KARAKTERLİ OLMALIDIR."
	quit()
else :
	print "\n\tSARAL BANKA GİRİŞİNİZ BAŞARIYLA GERÇEKLEŞMİŞTİR SAYIN",isim
	

	


yap1="\n(1) HESAPTAKİ PARA MİKTARINIZ ÖĞRENİN"
yap2="(2) HESABINIZDAN PARA ÇEKİN"
yap3="(3) HESABINIZA PARA EKLEYİN"

def durum2() :
	print "\nSAYIN",isim,"\t\tHESAPTAKİ MİKTAR  \t\t%f TL DİR"%1575

def islem1() :

	print"\nHESABINIZDAKİ PARA MİKTARI %f TL KADARDIR."%1575
	
	durum=raw_input("\nHESABINIZDAKİ PARA MİKTARI DOĞRUMU,YANLIŞMI (D/Y) : " )
	
	if durum == "y":
		print "\nDURUM BANKA YÖNETİCİLERİNE OTOMATİK OLARAK BİLDİRİLMİŞTİR."
		print "\nGEÇİCİ BİR SÜRE İÇİN HESABINIZ KAPATILACAKTIR.VE SORUN GİDERİLECEKTİR."
		quit()
	else :
		pass
	
	
	
def islem2() :
	durum2()
	
	cek=float(raw_input("\nHESABINIZDAN NE KADAR ÇEKMEK İSTİYORSUNUZ : "))
	
	print "\nHESABINIZDAN BAŞARIYLA",cek,"TL ÇEKİŞMİŞTİR."
	
	soru=raw_input("\nHESABINIZDA KALAN SON PARA MİKTARINI ÖĞRENMEK İSTİYORMUSUNUZ (E/H) :")
	
	if soru == "e" :
		global sonuc
		sonuc=(1575 - cek)
		
		print sonuc, "TL NİZ KALMIŞTIR"
		
	else :
		pass
	

def islem3() :
	durum2()
	
	cek2=float(raw_input("\nHESABINIZA NE KADAR PARA EKLEMEK İSTİYORSUNUZ : "))
	
	print "\nHESABINIZA BAŞARIYLA",cek2,"TL EKLENMİŞTİR."
	
	soru=raw_input("\nHESABINIZDA OLAN SON PARA MİKTARINI ÖĞRENMEK İSTİYORMUSUNUZ? (E/H) :")
	
	if soru == "e" :
		global sonuc
		sonuc=1575 + cek2
		
		print sonuc, "TL NİZ VARDIR"
		
	else :
		pass

	
	
def islem4() :
	durum2()
	
	soru5=raw_input("\nPARANIZIN EURO YADA DOLAR KARŞILIĞINI ÖĞRENMEK İSTERMİSİNİZ? (E/H) : ")
	
	if soru5 == "h" :
		islem6()
		
	if soru5 == "e" :
		islem8()
		islem6()
	
	
def islem5() :	

	soru11=raw_input("\nPARANIZIN EURO YADA DOLAR KARŞILIĞINI ÖĞRENMEK İSTERMİSİNİZ? (E/H) : ")
	
		
	if soru11 == "h" :
		islem6()
	
	if soru11 == "e" :
		islem7()
		islem6()
	
	
def islem6() :

	soru4=raw_input("\nHESAP İŞLEMLERİNE DEVAM ETMEK İSTİYORMUSUNUZ? (E/H) : ")
	
	if soru4 == "e" :	
		pass
	
	else :
		print "\n*HESAP OTURUMUNUZ BAŞARIYLA KAPATILMIŞTIR.\n\nBİZİ TERCİH ETTİĞİNİZ İÇİN TEŞEKKÜR EDERİZ."
		quit()	
	
def islem7() :
	
	global soru10
	soru10=raw_input("\nDOLAR (D) & EURO (E)  (D/E) : ")
	
	if soru10 == "d" :
		sonuc7= (sonuc / 1.55)
		print "\nPARANIZIN DOLAR KARŞILIĞI",sonuc7,"$"
		
	if soru10 == "e" :
		sonuc10= (sonuc / 2.15)
		print "\nPARANIZIN EURO KARŞILIĞI",sonuc10,"€"
	

def islem8() :
	global soru9
	soru9=raw_input("\nDOLAR (D) & EURO (E)  (D/E) : ")
			
	if soru9 == "d" :
		sonuc5= 1575 / 1.55
		print "\nPARANIZIN DOLAR KARŞILIĞI",sonuc5,"$"
		
	if soru9 == "e" :
		sonuc6= 1575 / 2.15
		print "\nPARANIZIN EURO KARŞILIĞI",sonuc6,"€"
	

while True :
	
	print yap1
	print yap2
	print yap3

	
	num=raw_input("\nYAPMAK İSTEDİĞİNİZ İŞLEMİN NUMARASINI SEÇİNİZ : ")	

	if num == "1" :
		islem1()
		islem4()
		
	
	if num == "2" :
		
		islem2()
		islem5()
		
		
		
	if num == "3" :
		islem3()
		islem5()
		
	
		

                                    #BETÜL SARAL              19.02.2011
