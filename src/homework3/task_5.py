# Дан список. Выведите те его элементы, которые встречаются в списке только один раз.
# Элементы нужно выводить в том порядке, в котором они встречаются в списке.


list_ = [1, 2, 3, 1, 2, 3, 4, 5, 'asd', 'asd', 'dsa']
new_list = []

for elem in list_:
    if elem not in new_list:
        new_list.append(elem)
print(new_list)
