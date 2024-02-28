nums = input().split()
t = int(nums[0])
n = int(nums[1])
answers = []
for i in range(t):
    string = input()
    charSet = set(string)
    prevChar = string[0]
    alter = True
    dict = {char: string.count(char) for char in charSet}
    for char in string[1::]:
        if not((dict[char] > 1 and dict[prevChar] <= 1) or (dict[char] <= 1 and dict[prevChar] > 1)):
            alter = False
            break
        prevChar = char
    answers.append('T' if alter else 'F')  

for answer in answers:
    print(answer)     


