# -*- coding: cp1254 -*-

class UniYer:
    def __init__(self,ad,soyad):
        self.ad=ad
        self.soyad=soyad
    def isim_cagir(self):
        print "ho�geldiniz say�n",self.ad,self.soyad
    def tc_no(self):
        while(1):
            a=input("\ntc kimlik numaran�z� giriniz:")
            if len(str(a))==11:
                print str(a)
                break;
            else :
                print "tc kimlik no 11 haneli olmal�d�r.tekrar deneyiniz."


class OgretimUye(UniYer):
    def __init__(self,ad,soyad):
        UniYer.__init__(self,ad,soyad)

    def santral(self):
        a=input("size ula�mam�z i�in santral numaran�z� giriniz : ")
        print a


class Ogrenci(UniYer):
    def __init__(self,ad,soyad):
        UniYer.__init__(self,ad,soyad)
    def kimlik(self):
        while (1):
            a=input("��renci numaran�z� giriniz : ")
            if len(str(a))==8:
                print a
                break
            else:
                print "\n��renci numaras� 8 haneden olu�ur.tekrar deneyiniz"

class Burslu(Ogrenci):
    def __init__(self,ad,soyad):
        Ogrenci.__init__(self,ad,soyad)

    def burs(self):
        a=raw_input("burslu musunuz (e/h) : ")
        if str(a)=="e":
            print "har� paran�z 170 tl"
        else:
            print "har� paran�z 420 tl "
            
        
        
    
            
    
    
        
        
#budaki fonksiyonlar deneme ama�l� olarak kar���k �a��r�lm��t�r.
#kendiniz d�zenleyebilirsiniz.
    
        
   
f1=UniYer("buraya isim gir","buraya soyad�n� gir")
f2=OgretimUye("buraya isim gir","buraya soyad�n� gir")
f3=Ogrenci("buraya isim gir","buraya soyad�n� gir")
f4=Burslu ("buraya isim gir","buraya soyad�n� gir")
f2.isim_cagir()
f3.kimlik()
f4.tc_no()
f4.burs()



        
