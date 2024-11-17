tekst = input('Podaj tekst: ')
litera = input('Podaj litere: ')
wynik = 0

for i in tekst:
    if i == litera:
        wynik += 1

print(f'Litera {litera} w tekscie "{tekst}" wystepuje {wynik} razy')