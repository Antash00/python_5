import os
import re
from shlex import join

f = open('files/cookbook.txt', encoding="utf-8").read().split('\n')
cookbook = {}
group = []
list_ingredients = []
i = 0
j = 0
for line in f:
    if line != '':
        group.append(line)
        if len(group) > 2:
            if len(group) == (2 + int(group[1])):
                cookbook[group[0]] = [group[2:]]
                for row in cookbook[group[0]]:

                    cook = []
                    for el in row:
                        result = {}
                        el = el.split(' | ')
                        result['ingredient_name'] = el[0]
                        result['quantity'] = int(el[1])
                        result['measure'] = el[2]
                        cook.append(result)
                    list_ingredients = cook

                cookbook[group[0]] = list_ingredients
                group = []
                i += 1
                j = 0
            else:
                j += 1


# print(cookbook)


def get_shop_list_by_dishes(dishes, person_count, cookbook):
    list_cooking = []
    result = {}
    for dish in dishes:
        for index in enumerate(cookbook[dish]):
            cookbook[dish][index[0]]['quantity'] = cookbook[dish][index[0]]['quantity'] * person_count
        for row in cookbook[dish]:
            key_exists = row['ingredient_name'] in result
            if key_exists:
                result[row['ingredient_name']] = {'measure': row['measure'],
                                                  'quantity': result[row['ingredient_name']]['quantity'] + row[
                                                      'quantity']}
            else:
                result[row['ingredient_name']] = {'measure': row['measure'], 'quantity': row['quantity']}
    return result


# print(get_shop_list_by_dishes(['Фахитос', 'Омлет'], 2, cookbook))
def byLen(file):
    return file['len']


file_dir = 'files/sorted_files/'
list_of_files = os.listdir(file_dir)

files = []
i = 0
for file in list_of_files:
    f1 = open(file_dir + file, encoding="utf-8").readlines()
    files.append({'len': len(f1), 'text': ''.join(f1), 'file': file})
sorted_arr_files = sorted(files, key=byLen)
f2 = open('files/sorted.txt', 'w', encoding="utf-8")
for sort_file in sorted_arr_files:
    f2.write(sort_file['file'] + '\n')
    f2.write(str(sort_file['len']) + '\n')
    f2.write(sort_file['text']+ '\n')


