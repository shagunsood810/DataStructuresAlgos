# Bubble Sort
x = [8.1,5,-7,8,3,2, 0]
def bubble(a):
	for j in range(len(a)):
		for i in range(len(a) - 1):
			if a[i] > a[i+1]:
				a[i], a[i+1] = a[i+1], a[i]
	return a


print("Sorted list using Bubble sort: ", bubble(x))



# Insertion sort
def insertion(a):
	for i in range(len(a)-1):
		if a[i] > a[i+1]:
			a[i], a[i+1] = a[i+1], a[i]
			for j in range(i):
				# print(i,j)
				if a[i] < a[j]:
					a[j], a[i] = a[i], a[j]

	return a


# x = [6,8,5,7,3,2]

print("Sorted list using Insertion sort: ",insertion(x))