class Sheet3:
    global firstPrimes
    firstPrimes = [2,3,5,7,11]
    global items_as_dict
    items_as_dict = dict(zip(range(0,len(firstPrimes)),firstPrimes))
    global items_as_dict_reverse
    items_as_dict_reverse = dict(zip(firstPrimes,range(0,len(firstPrimes))))

    global nextPrime
    def nextPrime(start):
        if start in items_as_dict_reverse and start!=firstPrimes[-1]:
            return items_as_dict.get(items_as_dict_reverse.get(start)+1)
        n=start+1
        while True:
            for i in range(2, int(n**0.5)+1):
                if n%i==0:
                    n += 1
                    break
            else:
                firstPrimes.append(n)
                items_as_dict.update({len(firstPrimes)-1:n})
                items_as_dict_reverse.update({n:len(firstPrimes)-1})
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
while (True):
    print(firstPrimes)
    print(items_as_dict)
    print(items_as_dict_reverse)
    ex.exercise7()
    if input("Do you want to continue? (y/n):")=='n':
        break