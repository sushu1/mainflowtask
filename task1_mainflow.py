# -*- coding: utf-8 -*-
"""Task1 Mainflow.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1UG6bTQH3Fl-N1fLzgrUcTeOcOW69e1Yq
"""

#LIST
list=['Sairam','Hanuman','Sushma','Sruthi','Maruthi']
#Adding
list.append('Shiva')
#removing
list.remove('Sushma')
#Modifying
list[2]='Jaya'
print("My Final list is:",list)

#Dictionary
dict={'name':'swaraj','branch':'It','Age':19,'Address':'Nellore'}
#Adding
dict['College']='Siddartha'
#removing
del dict['Age']
#Modifying
dict['Address']='Gudur'
print("My Final Dictionary is:",dict)

#set
set={10,20,30,40,50}
#adding
set.add(60)
#removing
set.remove(30)
#modifying
set.discard(10)
set.add(70)
print("My Final set is:",set)