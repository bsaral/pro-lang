#!/usr/bin/env python
# -*- coding: utf8 -*- 

import doctest

def sondan_basa_yaz(cumle):
    
    """\
    >>>sondan_basa_yaz("ondokuz mayis Universitesi")
    isetisrevinU siyam zukokno
    >>>sondan_basa_yaz("")
    ""
    >>>sondan_basa_yaz(45)
    lütfen parametre olarak karalter dizisi giriniz.

    """
    

    dizgi=""

    if cumle==str(cumle):
        for i in cumle[::-1]:
            dizgi+=i
        return dizgi


    else:
        print "lütfen parametre olarak karakter dizisi giriniz."
        
    
doctest.testmod()
