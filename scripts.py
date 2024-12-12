from operator import index

from src.randomizers import randomizer_person

# print(randomizer_person.generate_first_name_female())
#
# for i in range(10):
#     print(i, end='*')
#     if i > 6:
#         break
#
# tmp = [1, 2, 33, 4, 5, 6, 7, 8, 9, 10]
#
# tmp[3:4] = [11, 23, 23]
# print(tmp)


hotels = [
    {"id": 0, "title": "Sochi", "name": "sochi"},
    {"id": 1, "title": "Дубай", "name": "dubai"},
    {"id": 2, "title": "Мальдивы", "name": "maldivi"},
    {"id": 3, "title": "Геленджик", "name": "gelendzhik"},
    {"id": 4, "title": "Москва", "name": "moscow"},
    {"id": 5, "title": "Казань", "name": "kazan"},
    {"id": 6, "title": "Санкт-Петербург", "name": "spb"},
    [{"id": 0, "title": "Геленджик", "name": "gelendzhik"},
     {"id": 1, "title": "Москва", "name": "moscow"},
     {"id": 2, "title": "Казань", "name": "kazan"},
     {"id": 3, "title": "Мальдивы", "name": "maldivi"},
     {"id": 4, "title": "Геленджик", "name": "gelendzhik"},
     {"id": 5, "title": "Москва", "name": "moscow"},
     {"id": 6, "title": "Казань", "name": "kazan"},
     ]
]

page = 7
per_page = 1

# print(hotels[page:][:per_page])

for i in range(len(hotels)):
    # print(i)
    if i == 7:
        # print(hotels[i])
        for j in range(len(hotels[i])):
            print(hotels[i][j])

lst1 = 'sdfjksdf'
print(lst1.strip())


numbers = [-6, -8, 0, 1, 3, 8, -7, 12, 17, 24, 25, 3, 5, 1]
res = 0
for num in numbers:
    res += (num % 2 == 1) and (num > 1)
print(res)