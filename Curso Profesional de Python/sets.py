def remove_duplicate(some_list):
    without_duplicate = []
    for element in some_list:
        if element not in without_duplicate:
            without_duplicate.append(element)
    return(without_duplicate)

def run():
    random_list = [1, 1, 2, 2, 4]
    print(remove_duplicate(random_list))

if __name__ == '__main__':
    run()