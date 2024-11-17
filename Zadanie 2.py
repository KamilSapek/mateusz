x = int(input('Podaj wartosc gorna przedzialu: '))
y = int(input('Podaj wartosc dolna przedzialu: '))

for i in range(x, y - 1, -1):
    if i != y:
        print(i, end=', ')
    else:
        print(str(i) + '.')