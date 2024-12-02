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

count = 0
similarity = 0
while True:
    if count >= len(list_1):
        break
    similarity += int(list_1[count]) * list_2.count(list_1[count])
    count += 1
    
print(similarity)