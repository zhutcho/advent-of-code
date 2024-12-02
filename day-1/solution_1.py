file = open('./Day 1/input.txt', 'r')

list_1 = []
list_2 = []

while True:
    content = file.readline()
    if not content:
        break
    to_append = content.strip("\n").split(" ")
    to_append.pop(1)
    to_append.pop(1)
    list_1.append(to_append[0])
    list_2.append(to_append[1])

list_1.sort()
list_2.sort()

difference = []

total = 0
count = 0
while True:
    if count >= len(list_1):
        break
    total += abs(int(list_1[count]) - int(list_2[count]))
    count += 1
    
print(total)