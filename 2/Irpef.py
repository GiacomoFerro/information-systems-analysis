import sys

aliquota = [15000.0, 28000.0, 55000.0, 75000.0, 75000.0]
percentuale = [0.23,0.27,0.38,0.41,0.43]
eccesso = [0, 3450.0, 6960.0, 17220.0, 25420.0 ]

def irpef_calculation(income):
    i = 0
    for i in range(0,5):
        if (income < (aliquota[i])):
            irpef = income * percentuale[i]
            return irpef
        if (i == 4 and income>aliquota[i]):
            irpef = eccesso[i] + (income-aliquota[i])*percentuale[i]
            return irpef
        if (income>aliquota[i] and income<=aliquota[i+1]):
            irpef = eccesso[i+1] + (income-aliquota[i])*percentuale[i+1]
            return irpef


def main(income): # pragma: no cover
    print(" -------------------------------------")
    print("|                                     |")
    print("|            CALCOLO IRPEF            |")
    print("|                                     |")
    print(" -------------------------------------")

    print("IRPEF: \x80 {:.2f} \n".format(irpef_calculation(income))).decode("windows-1252")

if __name__ == '__main__':  # pragma: no cover
    if len(sys.argv) > 1:
        if float(sys.argv[1]) >= 0:
            main(float(sys.argv[1]))
