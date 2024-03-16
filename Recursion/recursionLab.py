def bunnyEar(n):
    if n == 0:
        return 0
    if n%2==0:
        return 3 + bunnyEar(n-1)
    else:
        return 2 +  bunnyEar(n-1)

def pairedLetter(s):
    if len(s)<3:
        return 0
    else:
        if s[0] == s[2]:
            return 1 + pairedLetter(s[1:])
        else:
            return pairedLetter(s[1:])

