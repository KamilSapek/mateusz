parzyste = 0
nieparzyste = 0

a = int(input('Podaj watrosc dolna przedzialu: '))
b = int(input('Podaj wartosc gorna pzredzialu: '))

for i in range(a, b + 1):
    if i % 2 == 0:
        parzyste += 1
    else:
        nieparzyste += 1

print(f'Parzyste: {parzyste}\nNieparzyste: {nieparzyste}')