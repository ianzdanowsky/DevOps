tuple_list = [("Ian",100),("Paloma", 200),("Lucas",300)]

def check_top_employee(tuple_list):

    # Placeholder variables

    current_max = 0
    top_employee = ''


    for employee,hours in tuple_list:
        if hours > current_max:
            current_max = hours
            top_employee = employee
        else:
            pass
    
    return (top_employee,current_max)


#result = check_top_employee(tuple_list)

name,hours = check_top_employee(tuple_list)

print(name)
print(hours)