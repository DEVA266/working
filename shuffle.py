# declaring a function that will allocate the students to their representative class 
def shuffle(all_department_details,all_department_names,all_department_strength,vacancy_class_details,vacancy_classes,vacancy_classes_strength):
    print(f"{all_department_details} \n {all_department_names} \n {all_department_strength} \n {vacancy_class_details} \n {vacancy_classes} \n {vacancy_classes_strength}")

total_department_count = int(input("Enter the total number of department writing exam : "))
# getting total department count in the college

all_department_names = []
all_department_strength = []
# declaring two list for saving the department name and strength 

for _ in range(total_department_count):
    department_name = input("Enter the department name : ")
    department_strength = int(input(f"Enter the {department_name} department Strength : "))
    # getting the department name and strength from the user and stores in the list 

    all_department_names.append(department_name)
    all_department_strength.append(department_strength)


# declaring a dictionary to map the strength of the department name to the department strength
all_department_details = dict(zip(all_department_names,all_department_strength))

print(all_department_details)

# declaring available vacancy in the class, with its class name
total_class = int(input("Enter the total number of vacancy class available for the exam : "))
vacancy_classes = []
vacancy_classes_strength = []

# getting information about tha vacany class and the strenght
for _ in range(total_class):  
    class_name = input("Enter the vacancy class name : ")
    class_strength = int(input(f"Enter the {class_name} strength : "))

    # adding those class name and strength to the list
    vacancy_classes.append(class_name)
    vacancy_classes_strength.append(class_strength)

# saving those list in the dictionary
vacancy_class_details = dict(zip(vacancy_classes,vacancy_classes_strength))

# calling the function shuffle
shuffle(all_department_details,all_department_names,all_department_strength,vacancy_class_details,vacancy_classes,vacancy_classes_strength)

print(vacancy_class_details)