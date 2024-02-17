# even no from 1 to 100
a = []
b = []
for i in range(1,101):
    if i % 2 == 0:
        a.append(i)
    else:
        b.append(i)
print("Even No. for 1 to 100 \n",a)
print("Odd No for 1 to 100 \n",b)
# print(len(a))