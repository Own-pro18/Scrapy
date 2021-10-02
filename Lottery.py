import random
list = []
dict = dict()
for i in range(1, 4):
    list1 = random.randrange(111, 333)
    list.append(list1)
    dict = {list1: f" {i} winner"}
    print(dict)
print(f'{list}')
# my_list = list(range(1, 1001))
