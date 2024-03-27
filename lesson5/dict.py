# dictionart = {
#     "key":"value",
#     "arr":[1,2,3,5],
#     "number":12,
#     'txt':"text",
#     "new_dict":{
#         "massiv":[1,2,3]
#     }
# }
# x = dictionart["arr"]
# for i in x:
#     print(i)

# dictionart = {
#     "key":"value",
#     "arr":[1,2,3,5],
#     "number":12,
#     'txt':"text",
#     "first_dict":{
#         "name":"MuhammadAmin",
#         "surname":"Boymuhammedov",
#         "age":[12,34,65,17,18,20]
#     },
#     "new_dict":{
#         "massiv":[1,2,3]
#     }
# }
# x = dictionart["first_dict"]["age"]
# print(17 if 17 in x else "topilmadi")
import random
# from faker import Faker
# name=Faker()
# print(name.name())
# new_dict = {}
# for i in range(20):
#     new_dict.update({i:i})
#     print(new_dict)

import random
from faker import Faker
dict = {}
fake = Faker()
for i in range(20):
      dict.update({fake.name():random.randint(1,100)})
print(dict)





# random.randint(1,100)


# from faker import Faker
# name = Faker()
# print(name.name())