#!/usr/bin/env python
# -*- coding: utf8 -*- 


isim=raw_input("ADINIZ : ")

if bool(isim) == True :
	print "\nWİNDOWS 8 KURULUMUNA HOŞGELDİNİZ SAYIN",isim
	
else:
	print "LÜTFEN ADINIZI GİRİNİZ"
	quit()

print "\nBURDA LİSANS ANTLAŞMASI VAR KABUL EDİN "
	
soru=raw_input("\nWİNDOWS 8 İN LİSANS ANTLAŞMASINI KABUL EDİYORMUSUNUZ? (E/H) : ")

if soru == "e" :
	print "\nKURULUM DEVAM EDİYOR"
else :
	print "\nDEVAM ETMEK İÇİN ŞARTLARI KABUL ETMENİZ GEREKİYOR"
	quit()
	
print "\nSAYIN",isim,"WİNDOWS 8 AİT 3 FARKLI KURULUM AŞAĞIDA VERİLMİŞTİR.BİRİNİ SEÇİNİZ"

li1="(1) STANDART PAKET"
li2="(2) MİNUMUM KURULUM"
li3="(3) ÖZEL KURULUM"



bil2="(1) YAZILIM ÖZELLİKLERİ"
bil3="(2) KURULUM ÖZELLİKLERİ"
bil4="(3) İŞLETİM ÖZELLİKLERİ"

def bil1():
	print bil2, bil3, bil4
	print "\nSTANDART PAKET UYGULAMA ÖZELLİKLERİ BUNLARDIR."
	soru2=raw_input("\nSİLMEK İSTEDİĞİNİZ HERHANGİ BİR ÖZELLİK VARMI? (E/H) : ")
	print soru2
	
		
	if soru2 == "e" :
		soru3=raw_input("HANGİ NUMARALI ÖZELLİĞİ SİLMEK İSTİYORSUNUZ?  :  ")
	
	if soru3 == "1" :
		print "\nİŞLEM BAŞARIYLA GERÇEKLEŞTİRİLDİ."
		print bil3,bil4
		
	if soru3 == "2" :
		print "\nİŞLEM BAŞARIYLA GERÇEKLEŞTİRİLDİ."
		print bil2,bil4
	   
	if soru3 == "3" :
		print "\nİŞLEM BAŞARIYLA GERÇEKLEŞTİRİLDİ."
		print bil2,bil3
    
	else :
		print "O ZAMAN İŞLEME DEVAM EDELİM"
		
		
print li1
print li2
print li3

while True :

	soru1=raw_input("\nİSTEDİĞİNİZ KURULUM NUMARASI : ")
	
	
	
	if soru1 == "1" :
		bil1()

	if soru1 == "2" :	
		bil1()
	
	if soru1== "3" :
		bil1()
	
	soru4=raw_input("\nBU KURULUMA DEVAM ETMEK İSTERMİSİNİZ ?	(E/H) : ")
	
	if soru4 == "e" :
		
		soru5=raw_input("\nSİSTEM KURULUM YERİNİ GİRİNİZ: ")
		
		print "\nİŞLEM BAŞARIYLA GERÇEKLEŞTİ. SİSTEM",soru5,"KURULDU."
		
		print "\nBİLGİSAYARINIZA WİNDOWS 8 KURULUMU TAMAMLANMIŞTI.\nBİZİ TERCİH ETTİĞİNİZ İÇİN TEŞEKKÜR EDERİZ"
		
		quit()
		
	if soru4 == "h" :
		print "\nLÜTFEN YENİDEN KURULUM NUMARASI SEÇİN"
		
		
		
	
	
	
	                              # BETÜL SARAL

