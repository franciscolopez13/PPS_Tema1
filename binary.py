def Binario (strbinario):
    try:
        for numero in range(0,len(strbinario)):
            if strbinario[numero]!='1' and strbinario[numero]!='0':
                return False
        return True
    except TypeError:
        return False

def extraer (binario):
    try:
        decimal=0
        for numero in range(0,len(binario)):
            if binario[numero]=='1':
                decimal=decimal+pow(2, len(binario)-numero-1)
        return decimal
    except TypeError:
        return False

cadena=str(input("introduce un número que sea binario: "))

if Binario(cadena):
    print(f"{cadena} es binario " + str(extraer(cadena)))
else:
    print(f"{cadena} no es binario")
