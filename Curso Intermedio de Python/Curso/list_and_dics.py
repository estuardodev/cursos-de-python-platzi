def run():
    my_list = [1, "Hello", True, 4.5]
    my_dict = {"firsname": "Estuardo", "lastname":"Ramirez"}

    super_list = [
        {"firsname": "Estuardo", "lastname":"Ramirez"},
        {"firsname": "Sara", "lastname":"Chavez"},
        {"firsname": "Ester", "lastname":"Morales"},
        {"firsname": "Juan", "lastname":"Perez"}
    ]

    super_dist = {
        "natural_nums": [1,2,3,4,5],
        "integer_nums": [-1,-2,0,1,2],
        "floating_nums": [1.1,4.5,6.43]
    }

    for key, value in super_dist.items():
        print(key, "-", value)

    for values in super_list:
        for keys, values2 in values.items():
            print(f"{keys} - {values2}")
        

if __name__ == '__main__':
    run()