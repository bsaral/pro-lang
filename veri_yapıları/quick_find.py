# -*- coding: cp1254 -*-

def quick_find(dizi):
    for i in range(len(dizi)):
            sor=raw_input("ba�lant� noktas� girin(or. 6-9 veya birlestir('b1') veya bul ('b2'):)")
            if sor=="end":
                break
            elif sor=="b1":
                ###birle�tir fonksiyon b�l�m�
                sor2=raw_input("id-basla-bitir:")
                id_,basla,bitir=sor2.split("-")
                for i in range(int(basla),int(bitir)+1):
                    dizi[i]=int(id_)
                    
            elif sor=="b2":
                #bul fonksiyonu b�l�m�
                sor3=raw_input("p-q(�rn:(3-4)):")
                p,q=sor3.split("-")
                if dizi[int(p)]==dizi[int(q)]:
                    print "birbirine ba�l�"
                else:
                    print "birbirine ba�l� de�il."
                
            else:
                #quick_find b�l�m�
                ilk,son = sor.split("-")
                ilk,son = int(ilk), int(son)
                a=dizi[ilk]
                dizi[ilk]=dizi[son]
                for j in range(len(dizi)):
                    if dizi[j]==a:
                        dizi[j]=dizi[son]
                
            print dizi

quick_find([0,1,2,3,4,5,6,7,8,9])


        
