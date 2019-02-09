#coding=utf-8
from sys import argv
import string

#Strutture dati Globali
vocali = ('a','e','i','o','u')
mesi = ('a','b','c','d','e','h','l','m','p','r','s','t')
comuni = {'udine':'l483', 'verona':'l781', 'legnago': 'e512', 'negrar':'f861', 'bassano del grappa': 'a703'}

#CODICI DI CONTROLLO
regole_pari = {}
alfabeto = string.ascii_lowercase
for i in xrange (0,10):
    regole_pari[str(i)] = i
for i in xrange (0,26):
    regole_pari[alfabeto[i]] = i

regole_dispari = {}
temp_tuple = (1,0,5,7,9,13,15,17,19,21)
for i in xrange(0,10):
    regole_dispari[str(i)] = temp_tuple[i]
    regole_dispari[alfabeto[i]] = temp_tuple[i]

temp_tuple2 = (2,4,18,20,11,3,6,8,12,14,16,10,22,25,24,23)
index = 0
for i in xrange(10,26):
    regole_dispari[alfabeto[i]] = temp_tuple2[index]
    index += 1

regole_resto = [alfabeto[i] for i in xrange(0,26)]

#------------------------------

def estrai_cognome(aString):
    if (' ' in aString):
        aString = aString[:aString.find(' ')] + aString[aString.find(' ')+1:]
    if ("'" in aString):
        aString = aString[:aString.find("'")] + aString[aString.find("'")+1:]
    temp_string = ''

    temp_string = ''
    for aChar in aString:
        if not aChar in vocali:
            temp_string += aChar

        if len(temp_string) >= 3:
            break

    if (len(temp_string)<3):
        for aChar in aString:
            if aChar in vocali: #prendo le vocali
                temp_string += aChar #aggiungo la vocale
                if len(temp_string) >= 3:
                    break
        if (len(temp_string) < 3): #aggiungo le x nel caso in cui la stringa non è 3
            temp_string += 'x'*(3-(len(temp_string)))

    return temp_string

def estrai_nome(aString):
    if (' ' in aString):
        aString = aString[:aString.find(' ')] + aString[aString.find(' ')+1:]
    temp_string = ''

    n_consonanti = 0
    for aChar in aString:
        if not aChar in vocali:
            n_consonanti+=1 #incremnto il numero di consonanti del nome

    if (n_consonanti <= 3): #quindi prendo tutti e tre le consonanti
        for aChar in aString:
            if not aChar in vocali:
                temp_string += aChar
                if len(temp_string) >= 3:
                    break

        if (len(temp_string)<3): #prendo le vocali e le aggiungo
            for aChar in aString:
                if aChar in vocali:
                    temp_string += aChar
                if (len(temp_string)>=3):
                    break
        if (len(temp_string)<3):
            temp_string += 'x'*(3-(len(temp_string)))

    else: #caso se ho tante consonanti
        for aChar in aString:
            if not aChar in vocali:
                temp_string += aChar
            if (len(temp_string)>3):
                break
        #togliamo la consonante in posizione due
        temp_string = temp_string[:1] + temp_string[2:]

    return temp_string

def genera_mese(unMese):
    return mesi[int(unMese)-1]


def codice_comune(comune):
    return comuni[comune]


def genera_giorno(unGiorno, unSesso):
    if int(unGiorno) in xrange(1,31):
        if unSesso == 'm':
            return unGiorno
        elif unSesso == 'f':
            return str(int(unGiorno)+40)


def genera_codice_controllo(aCodiceFiscale):
    parita = 1
    temp_dispari = 0
    temp_pari = 0

    for aChar in aCodiceFiscale:
        if parita:
            temp_dispari += int(regole_dispari.get(aChar))
            parita = 0
        else:
            temp_pari += int(regole_pari.get(aChar))
            parita = 1

    return regole_resto[(temp_dispari+temp_pari) % 26]

def main(): #pragma: no cover
    nome            = raw_input("Nome: ").lower()
    cognome         = raw_input("Cognome: ").lower()
    data_nascita    = raw_input("Data di nascita (gg/mm/aaaa): ").lower()
    comune          = raw_input("Comune di nascita: ").lower()
    sesso           = raw_input("Sesso (m/f): ").lower()
    #cognome      = string.lower(argv[1])
    #nome         = string.lower(argv[2])
    #data_nascita = string.lower(argv[3])
    #comune       = string.lower(argv[4])
    #sesso        = string.lower(argv[5])

    nomeCF = estrai_nome(nome)
    cognomeCF = estrai_cognome(cognome)

    data_nascitaCF = data_nascita.split("/")
    anno_nascitaCF = data_nascitaCF[2][2:]

    mese_nascitaCF = genera_mese(data_nascitaCF[1])
    giorno_nascitaCF = genera_giorno(data_nascitaCF[0], sesso)

    codice_fiscale = cognomeCF + nomeCF + anno_nascitaCF + mese_nascitaCF + giorno_nascitaCF + codice_comune(comune.lower())

    codiceCF = genera_codice_controllo(codice_fiscale)

    codice_fiscale += codiceCF

    print (codice_fiscale)

if __name__ == "__main__":  #pragma: no cover
    main()
