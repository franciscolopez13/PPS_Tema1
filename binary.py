def Binario (strbinario):
    try:
        for elemento in range(0,len(strbinario)):
            if strbinario[elemento]!='1' and strbinario[elemento]!='0':
                return False
        return True
    except TypeError:
        return False

def extraer (binario):
    try:
        decimal=0
        for elemento in range(0,len(binario)):
            if binario[elemento]=='1':
                decimal=decimal+pow(2, len(binario)-elemento-1)
        return decimal
    except TypeError:
        return False

cadena=str(input("introduce un número binario: "))

if Binario(cadena):
    print(f"{cadena} es binario " + str(extraer(cadena)))
else:
    print(f"{cadena} no es binario")
