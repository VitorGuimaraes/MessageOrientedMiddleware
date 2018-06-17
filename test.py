# -*- coding: utf-8 -*-
l1 = [["a", 1], ["b", 2], ["c", 3]]

import time

time = time.strftime("%H:%M:%S")
print(time)

# for item in l1:
#     # if "a" in item[0]:
#         # print("Elemento a encontrado")
#     print item[1]

# if [x[0] for x in l1 if x[0] == "a"]:
#     print("ok")

# for x in l1:
#     print(x)
#     print(x[1])

def run():
    obj = [x[1] for x in l1 if x[0] == "a"]
    print obj
        # print x[1]
        # # print x[2]

# print [x[1] for x in l1 if "a" not in x[1]]

# run()