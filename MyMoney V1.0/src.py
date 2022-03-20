
stundenlohn = input('Bitte Geben sie ihren Stundenlohn an ')
stunden = input('Wieviel Stunden am Tag Arbeiten sie? ')
tag = int(stunden) * int(stundenlohn)
Monat = int(tag) * 22 
Jahr = int(Monat) * 12






print('ihr Stundenlohn beträgt ' + str(stundenlohn) +'€\r\n')
print('Sie verdienen '+ str(tag) +' € pro tag\r\n')
print('Sie verdiene '+ str(Monat) +'€ im Monat\r\n')
print('Sie haben ein Jahresgehalt von ' + str(Jahr) +'€\r\n')

void1 = input('abrechen (a) oder von vorne beginnen (d) ')



if void1 == 'a':
    exit()
if void1 == 'd':
    stundenlohn1 = input('Bitte Geben sie ihren Stundenlohn an ')
    stunden1 = input('Wieviel Stunden am Tag Arbeiten sie? ')
    tag1 = int(stunden) * int(stundenlohn)
    Monat1 = int(tag) * 22 
    Jahr1 = int(Monat) * 12  

print('ihr Stundenlohn beträgt ' + str(stundenlohn1) +'€\r\n')
print('Sie verdienen '+ str(tag1) +' € pro tag\r\n')
print('Sie verdiene '+ str(Monat1) +'€ im Monat\r\n')
print('Sie haben ein Jahresgehalt von ' + str(Jahr1) +'€\r\n')



end = input('drücke eine beliebige Taste!...')
