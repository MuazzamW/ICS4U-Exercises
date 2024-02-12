class Sheet3:

    global nextPrime
    def nextPrime(start):
        firstPrimes = [2,3,5,7,9]
        if start in firstPrimes and start!=9:
            return firstPrimes[firstPrimes.index(start)+1]
        n=start+1
        while True:
            for i in range(2, n):
                if n%i==0:
                    n += 1
                    break
            else:
                return n      
    def exercise7(self):

        while True:
            try:
                n = int(input("enter an integer:"))
                break
            except ValueError as e:
                print("Error: ",e)
        finalDict = {}
        divisor = 2
        count = 0
        while n!=1:
            if(n%divisor==0):
                n = n//divisor
                count+=1
                if n==1:
                    finalDict.update({divisor:count})
            else:
                if count>=0:
                    if not count==0:
                        finalDict.update({divisor:count})
                        divisor = nextPrime(divisor)
                        count=0
                    else:
                        divisor = nextPrime(divisor)

        print(finalDict)

ex = Sheet3()
ex.exercise7()