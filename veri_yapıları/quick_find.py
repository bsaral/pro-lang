# -*- coding: cp1254 -*-

def quick_find(dizi):
    for i in range(len(dizi)):
            sor=raw_input("bağlantı noktası girin(or. 6-9 veya birlestir('b1') veya bul ('b2'):)")
            if sor=="end":
                break
            elif sor=="b1":
                ###birleştir fonksiyon bölümü
                sor2=raw_input("id-basla-bitir:")
                id_,basla,bitir=sor2.split("-")
                for i in range(int(basla),int(bitir)+1):
                    dizi[i]=int(id_)
                    
            elif sor=="b2":
                #bul fonksiyonu bölümü
                sor3=raw_input("p-q(örn:(3-4)):")
                p,q=sor3.split("-")
                if dizi[int(p)]==dizi[int(q)]:
                    print "birbirine bağlı"
                else:
                    print "birbirine bağlı değil."
                
            else:
                #quick_find bölümü
                ilk,son = sor.split("-")
                ilk,son = int(ilk), int(son)
                a=dizi[ilk]
                dizi[ilk]=dizi[son]
                for j in range(len(dizi)):
                    if dizi[j]==a:
                        dizi[j]=dizi[son]
                
            print dizi

quick_find([0,1,2,3,4,5,6,7,8,9])


        
