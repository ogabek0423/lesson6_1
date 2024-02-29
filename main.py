a = [1, 2, 3, 4]
b = [3, 4, 5]
sum = 0
for i in range(len(a)):
    kop = 1
    for j in range(len(b)):
        kop = kop * (a[i] + b[j])
        print(kop)
    sum = sum + kop

print(sum)