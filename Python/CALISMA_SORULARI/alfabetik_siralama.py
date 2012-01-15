#!/usr/bin/env python
# -*- coding: utf8 -*- 



def alfabetik_artan(dizgi):
  liste=[]
  son=""
  for i in dizgi:
      liste.append(i)
      liste.sort()
  for a in liste:
      son+=a

  if dizgi==son:
      print "true"

  else:
      print "false"
  
