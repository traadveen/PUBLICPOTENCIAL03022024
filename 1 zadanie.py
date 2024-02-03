import csv

with open('vacancy.csv', encoding='utf8') as file:
    reader = csv.reader(file, delimiter=';', quotechar='"')
    tab =  list(reader)[1:]

    com_sal = {}

    m = 0
    c = 3
    for Salary, Work_Type, Company_Size, Role, Company in reader:
        m = max(m, int(Salary))
    for Salary, Work_Type, Company_Size, Role, Company in reader:
        if int(Salary) == m:
            print(f'{Company}')



    with open('vacancy_new.csv', 'w', encoding='utf8', newline='') as f:
        w = csv.writer(f)
        w.writerow(['company', 'role', 'salary'])
