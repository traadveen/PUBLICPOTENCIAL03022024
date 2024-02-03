import csv
with open('vacancy.csv', encoding='utf8') as file:
    reader = list(csv.DictReader(file, delimiter=';', quotechar='"'))
    for i in range(len(reader)):
        j = i - 1
        key = reader[i]
        # print(key)
        while int(reader[j]['Company_Size']) > int(key['Company_Size']) and j >= 0:
            reader[j + 1] = reader[j]
            j -= 1
    reader[j + 1] = key
    for el in reader:
        print(el)
        if 'классный руководитель' in el['Role']:
            print(el)