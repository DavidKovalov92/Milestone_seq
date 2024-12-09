from faker import Faker



filename = r'C:\Users\David\Fractal_tree\hard\database.csv'

fake = Faker()

def generate_data():
    names = [fake.name() for _ in range(100)]
    data_of_hire = [fake.date_of_birth(minimum_age=3, maximum_age=10) for _ in range(100)]
    data_of_birthday = [fake.date_of_birth(minimum_age=20, maximum_age=45) for _ in range(100)]
    phone_number = [fake.phone_number() for _ in range(100)]
    department = [fake.job() for _ in range(100)]
    names = [names[i].split() for i in range(len(names))]
    print(data_of_birthday, data_of_hire)
    for i in range(len(names)):
        names[i] = names[i][-1]

    return data_of_hire, data_of_birthday, phone_number, names, department


with open(filename, 'w') as file:
    data_of_hire, data_of_birthday, phone_number, names, department = generate_data()


    for i in range(100):
        file.write(f'{names[i]} '
                   f'{data_of_hire[i]} '
                   f'{data_of_birthday[i]} '
                   f'{phone_number[i]} '
                   f'{department[i]}\n')