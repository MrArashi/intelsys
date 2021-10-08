x = 3
List = [];

for i in range(x):
	msg = "Значение " + str(i+1) + ": "
	List.append(int(input(msg)))

for i in range(len(List)):
	if List[i] <= 3 and List[i] >= 1:
		print("Число " + str(List[i]) + " входит в диапазон [1,3]")
