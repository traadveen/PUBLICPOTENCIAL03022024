import csv

with open('vacancy.csv', encoding='utf8') as file:
    reader = list(csv.DictReader(file, delimiter=';', quotechar='"'))

    data = sorted(reader, key = lambda x: x["Company"])



    company = input()
    while company != 'None':
        for el in reader:
            s = el['\ufeffSalary']
            if company in el['Company']:

                print(f'В {company} найдена вакансия: {el["Role"]}. З/п составит: {s}')
                break

        else:
            print('К сожалению, ничего не удалось найти')
        company = input()