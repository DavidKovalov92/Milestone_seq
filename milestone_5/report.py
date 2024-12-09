from generate_data import filename
from datetime import datetime



def generate_report(file_, month_):
    month = datetime.strptime(month_.capitalize(), '%B').month


    with open(file_, 'r') as file:
        lines = file.readlines()

    birthday_count = 0
    jubilee_count = 0
    department_birthdays = {}
    department_jubilees = {}

    for line in lines:
        parts = line.split()

        birth_date = parts[2]
        department = parts[-1]

        birth_obj = datetime.strptime(birth_date, '%Y-%m-%d')

        if birth_obj.month == month:
            birthday_count += 1
            department_birthdays[department] = department_birthdays.get(department, 0) + 1


            current_year = datetime.now().year
            age = current_year - birth_obj.year
            if age % 10 == 0:
                jubilee_count += 1
                department_jubilees[department] = department_jubilees.get(department, 0) + 1


    print(f"Report for {month_.capitalize()} generated")
    print("--- Birthdays ---")
    print(f"Total: {birthday_count}")
    print("By department:")
    for department, count in department_birthdays.items():
        print(f"- {department}: {count}")
    print("--- Anniversaries ---")
    print(f"Total: {jubilee_count}")
    print("By department:")
    for department, count in department_jubilees.items():
        print(f"- {department}: {count}")

month_ = input("Enter month: ")
generate_report(filename, month_)