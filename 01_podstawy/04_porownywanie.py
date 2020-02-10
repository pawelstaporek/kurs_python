a = 1
b = 10

print(a == b)
print(a != b)
print(a < b) # >
print(a <= b) #>=

a = a + 1 #to samo co:
a += 1

print(a < b and a % 2 == 0 and a / 0 == 3) #ostatnie wyrażenie nie jest sprawdzane bo drugie jest false
print(a < b or a % 2 == 0)
