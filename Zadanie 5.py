from random import getrandbits

orzel = 0
reszka = 0

for i in range(int(input('Ile razy chcesz rzucic moneta?: '))):
    if getrandbits(1) == 0:
        orzel += 1
    else:
        reszka += 1

print(f'Orzel: {orzel}\nReszka: {reszka}')