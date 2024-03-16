n = int(input())
dist = n//2
hats = []
count = 0
for i in range(n):
    hats.append(int(input()))
for i in range(n//2):
    if hats[i] == hats[i+dist]:
        count+=1
print(2*count)

        