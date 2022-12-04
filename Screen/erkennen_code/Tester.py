import numpy as np, os, sys
# a_list = [1, 2, 3]
# b_list = [2,3,4]

# an_array = np.array(a_list)
# bn_array = np.array(b_list)
# multiplied_array = an_array * bn_array
# print(bn_array[1])

# print(np.sum(multiplied_array))
# print(np.dot(an_array, bn_array))

# lists = np.array([2,3,3,3], float)
# print(lists)
# lists[1] += 0.5
# print(lists)

cwd = os.getcwd()
cwd = cwd.replace('\erkennen_code','')
cwd += '/'

# connection_values = []
# with open(cwd + 'connections\Test.txt', 'r') as filehandle:
#     for line in filehandle:
#         currentnum = line[:-1]
#         connection_values.append(int(currentnum))

# v1 = 'Bilder/viereck_1.txt'
# v2 = 'Bilder/viereck_2.txt'
# v3 = 'Bilder/viereck_3.txt'
# v4 = 'Bilder/viereck_4.txt'
# k1 = 'Bilder/kreis_1.txt'
# k2 = 'Bilder/kreis_2.txt'
# k3 = 'Bilder/kreis_3.txt'
# k4 = 'Bilder/kreis_4.txt'
# image_sauce = [v1,v2,v3,v4,k1,k2,k3,k4]

# current_screen = []
# np_connection_values = np.array(connection_values, float)

# with open(cwd+image_sauce[5], 'r') as filehandle:
#             for line in filehandle:
#                 currentnum = line[:-1]
#                 current_screen.append(int(currentnum))

# np_current_screen = np.array(current_screen)
# np_current_screen = np_current_screen/255

# np.set_printoptions(threshold=sys.maxsize)
# np.set_printoptions(suppress=True)
# #print(np_current_screen)

# for i in range(len(np_connection_values)):
#     if np_current_screen[i]==1: np_connection_values[i] = np_connection_values[i]+0.5
# print(np_connection_values*np_current_screen)

array = []
a = [2,3,4]
b = [10, 20]
array1 = []
array1.append(a)
array1.append(b)
array.append(array1)
a = [2,3,4]
b = np.array([10, 20])
b = b.tolist()
array2 = []
array2.append(a)
array2.append(b)
array.append(array2)
print(array)

