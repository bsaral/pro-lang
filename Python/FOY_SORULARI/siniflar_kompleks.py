#!/usr/bin/env python
# -*- coding: utf8 -*-
class kompleks:
    def __init__(self,arg_re,arg_im):
        self.gercel=arg_re
        self.sanal=arg_im

    def mutlak(self):
        return ((self.gercel**2+self.sanal**2)**0.5)

    def yazdir(self):
        print self.gercel ,"+ i",self.sanal
