#coding=utf-8
import sys

# usando il METODO ARITMETICO DI GAUSS per il calcolo della data della Pasqua
#anno = anno di cui si vuole sapere la data della pasqua
def pasqua(anno):
    #condizioni da verificare
    if anno<1583 or anno>2499: return None
    tabella={15:(22, 2), 16:(22, 2), 17:(23, 3), 18:(23, 4), 19:(24, 5),
           20:(24, 5), 21:(24, 6), 22:(25, 0), 23:(26, 1), 24:(25, 1)}
    m, n = tabella[anno//100]

    #faccio il modulo di certi elementi
    a=anno%19
    b=anno%4
    c=anno%7
    d=(19*a+m)%30
    e=(2*b+4*c+6*d+n)%7

    #faccio la somma tra due elementi calcolati
    giorno=d+e
    if (d+e<10): #se queasta somma è minore di 10 entro, quindi il giorno è minore di 32 (quindi minore o uguale a 31) se condiseriamo già la somma con 22
        giorno+=22 #sommo 22 al giorno indicato
        mese=3 #per indicare il mese Marzo

    else: #caso in cui il giorno non è minore o uguale a 31
        giorno-=9 #tolgo giorni alla data prestabilita
        mese=4 #per indicare il mese Aprile
        if ((giorno==26) or ((giorno==25) and (d==28) and (e==6) and (a>10))):
            giorno-=7
    #ritorno una tupla di (giorno, mese, anno) in mvalore numerico
    return giorno, mese, anno


def main(anno):  # pragma: no cover
    print(" -------------------------------------")
    print("|                                     |")
    print("|           CALCOLO PASQUA            |")
    print("|                                     |")
    print(" -------------------------------------")

    print((pasqua(anno)) )


if __name__ == '__main__':  # pragma: no cover
    main(float(sys.argv[1]))
