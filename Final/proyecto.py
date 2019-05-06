import random

def main():
    print('BREAKPOINT!')
    dFound = False
    dF = True
    num = 2
    arregloPrimos = generaPrimos(num)
    separadores = []
    p = arregloPrimos[0]
    q = arregloPrimos[1]
    for i in range (0,len(arregloPrimos)):
        print (arregloPrimos[i])

    n = p*q
    print ('N: ',n)
    Fn = (p-1)*(q-1)
    print ('Phi(N): ',Fn)
    e = 3
    d = 0
    for i in range (0, Fn):
        if e*i%Fn==1:
            print ('d found! : ',i)
            dFound = True
            d = i
            break

    print('BREAKPOINT!')
    if dFound:
        print ('Public key:(',e,',',n,')')
        print ('Private key:(',d,',',n,')')
    else:
        print('d not Found, trying again...')
        dF = False
        main()
       
    
    mensaje = input('Escribe el mensaje a cifrar')
    separadores = transformarNumerico(mensaje)
    mensaje = separadores[0]
    cifrado = cifrarMensaje(e,n,mensaje)
    print ('Mensaje cifrado: ',cifrado)
    final = descifrarMensaje(cifrado,d,n,separadores)
    print ('Mensaje descifrado: ', final)
    
    

#numPrimos es el numero de primos aleatorios que se quiren generar
def generaPrimos(numPrimos):
    arrPrimos = []
    numsUsados = []
    for i in range (0, numPrimos):
        isPrime = True
        found = False
        while (not found):
            while True:
                actualNum = random.randint(100,200)
                
                if actualNum not in numsUsados:
                    break
                else:
                    print('numero primo igual, RECALCULANDO...')
            
            
            for num in range (2, actualNum):
                if actualNum % num == 0:
                    isPrime = False     
            if isPrime:
                numsUsados.append(actualNum)
                found = True
                arrPrimos.append(actualNum)
            isPrime = True       
    return arrPrimos

def cifrarMensaje(e,n,mensaje):
    M=pow(mensaje,e)
    C = M%n
    return C

##NO ESTÁ DESCIFRANDO DE MANERA CORRECTA
def descifrarMensaje(C,d,n,separadores):
    msg = pow(C,d)
    print ('NUMERO EXPONENCIADO DESCIFRADO',msg)
    final = msg%n
    print('Numero antes de tranformacion: ',final)
    final = invertirAString(final,separadores)
    return final


def invertirAString(final,separadores):
    final = str(final)
    anterior = 0
    normal = ""
    temp = ""
    for i in range(0,len(separadores[1])):
        letraActual = separadores[1][i]
        numDeLetra = final[anterior:letraActual]
        print (numDeLetra)
        anterior+=letraActual-1
        numDeLetra=int(numDeLetra)
        print ('NumDeLetra ',i,': ')
        temp = chr(numDeLetra)
        normal+=temp
    
    return normal

def transformarNumerico(mensaje):
    numerico = ""
    separadores = []
    prevSeparador = 0
    temp = 0
    for c in mensaje:
        temp = ord(c)
        temp = str(temp)
        prevSeparador+=(len(temp))
        print (prevSeparador)
        separadores.append(prevSeparador)
        print (str(temp))
        numerico+=str(temp)
        
    numerico=int(numerico)
    print ('Message in number format: ',numerico)
    arreglo = []
    arreglo.append(numerico)
    arreglo.append(separadores)
    print ('ARREGLO EN TRANSFORMARNUMERICO: ',arreglo)
    return arreglo

def prueba(string):
    str2=(string[1:4])
    print (str2)

def mod(x,y):
    a = x%y
    print (a)
#transformarNumerico("hola")


main()
#prueba("string")



