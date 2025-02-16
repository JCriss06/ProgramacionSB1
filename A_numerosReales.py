#Reglas gramaticales
#Un numero real puede comenzar con un signo opcional (+ o -)
#La parte entera cosiste en uno o mas digitos (0 - 9)
#la base decimal es opcional y consiste en un punto(.), seguido de uno o mas digitos (0 - 9)
#la parte exponencial es opcional y consiste en una letra e o E, seguida de un signo opcional (+ o -) y uno o mas digitos (0 - 9)

def es_numeros_real(cadena):
    #inicio
    #leer cadena
    #iniciar contador i = 0 para recorrer la cadena, caracter por caracter
    #iniciar variable numvalido a verdadero
    #si la cadena esta vacia, entonces numvalido es falso

    #si el primer caracter es un signo y i es menor que longitud de la cadena, entonces se incrementa i
        #si el siguiente caracter es un digito, y i es menor que la longitud de la cadena, entonces se incrementa i
            #si no hay digitos, entonces numvalido es falso

    #si el siguiente caracter es un punto y i es menor que la longitud de la cadena, entonces se incrementa i
        #si el siguiente caracter es un digito y i es menor que la longitud de la cadena, entonces se incrementa i
            #si no hay digitos, entonces numvalido es falso

    #si el siguiente caracter es una e o E y i es menor que la longitud de la cadena, entonces se incrementa i
        #si el siguiente caracter es un signo y i es menor que la longitud de la cadena, entonces se incrementa i
            #si el siguiente caracter es un digito y i es menor que la longitud de la cadena, entonces se incrementa i
                #si no hay digitos, entonces numvalido es falso
    #si i es diferente a la longitud de la cadena, entonces numvalido es falso
    #regresar numvalido
    #fin

    n = len(cadena)
    i = 0
    numvalido = True

    if n == 0:
        return False

    if i < n and (cadena[i]  == "+" or cadena[i] == "-"):
        i += 1

    if i < n and cadena[i].isdigit():
        while i < n and cadena[i].isdigit():
            i += 1
    else:
        numvalido = False

    if i < n and cadena[i] == ".":
        i += 1
        if i < n and cadena[i].isdigit():
            while i < n and cadena[i].isdigit():
                i += 1
        else:
            numvalido = False

    if i < n and (cadena[i] == "e" or cadena[i] == "E"):
        i += 1
        if i < n and (cadena[i] == "+" or cadena[i] == "-"):
            i += 1
        if i < n and cadena[i].isdigit():
            while i < n and cadena[i].isdigit():
                i += 1
        else:
            numvalido = False

    if i != n: #verifica que se haya recorrido toda la cadena
        numvalido = False

    return numvalido

if __name__ == "__main__":
    print(es_numeros_real("-123.456"))  # True
    print(es_numeros_real("123.456e+789"))  # True
    print(es_numeros_real("123"))  # True
    print(es_numeros_real("123e-10"))  # True
    print(es_numeros_real("123."))  # False
    print(es_numeros_real(".456"))  # False
    print(es_numeros_real("e10"))  # False
    print(es_numeros_real("123e"))  # False



