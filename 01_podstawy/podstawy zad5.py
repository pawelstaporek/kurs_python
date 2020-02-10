"""
Napisz kod który na podstawie wprowadzonych wymiarów opakowania (prostopadłościan) obliczy i sprawdzi 
czy objętość jest większa od 1 l (1000 cm3)
"""

a = 10
b = 5
c = 21

#albo a, b, c = 10, 5, 21

warunek = a * b * c > 1000
if warunek == True:
   print("Większe niż 1 litr")
#elif 
else:
   print:("Nie większe niż 1 litr")