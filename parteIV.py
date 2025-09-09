#ciclos
i=1
while i<=5:
    print(i)
    i+=1 #es lo mismo que: i = i+1

for i in range(5):
    print(i)

frutas = ["manzanas", "pera", "fresas"]

print(frutas[2])
for fruta in frutas:
    print(fruta)

#break y continue: romper el ciclo
for j in range(10):
    if j == 5:
        break
    print(j)

for k in range(5):
    if k == 2:
        continue
    print(k)






