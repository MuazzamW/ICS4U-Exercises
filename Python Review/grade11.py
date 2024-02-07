import random

def postalCode():
    code = []
    for i in range(6):
        if i%2==0:
            code.append(str(random.randint(0,9)))
        else:
            code.append(chr(random.randint(65,90)))
    final = "".join(code)
    return final[:3] + " " + final[3:]

print(postalCode())
