import random
def main():
    dFound = False
    num = 2
    arregloPrimos = generaPrimos(num)
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
    if dFound:
        print ('Public key:(',e,',',n,')')
    else:
        print('d not Found, trying again...')
        main()
        

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


main()




