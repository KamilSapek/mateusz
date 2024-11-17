a = int(input('Podaj granice dolna przedzialu: '))
b = int(input('Podaj granice gorna przedzialu: '))

for i in range(a, b + 1):
    print(f'x = {i}, y = {i**2 + 1}')