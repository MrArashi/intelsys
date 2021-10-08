Count = input("Укажите кол-во элементов листа: ")
Count = int(Count)
listOrigin = []
listMask = []

for item in range(Count):
    msg = "Элемент " + str(item+1) + ": "
    listOrigin.append(int(input(msg)))

x = sum(listOrigin)/Count

for item in listOrigin:
    if item > 0: 
        listMask.append(item)
    elif item < 0: 
        listMask.append(item)
    else: 
        listMask.append(x) 

print(listOrigin)
print(listMask)