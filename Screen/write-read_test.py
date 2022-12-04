listofnum = []
for i in range(50):
    for j in range(50):
        listofnum.append(255)
print(listofnum)

with open('Test.txt', 'w') as filehandle:
    for listofnum in listofnum:
        filehandle.write('%s\n' % str(listofnum))

new_list = []
with open('Test.txt', 'r') as filehandle:
    for line in filehandle:
        currentnum = line[:-1]
        new_list.append(int(currentnum))
print(new_list)

# with open('listfile.txt', 'w') as filehandle:
#     for listitem in places:
#         filehandle.write('%s\n' % listitem)