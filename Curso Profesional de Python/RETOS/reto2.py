def make_division_of(n):
    def division(x):
        return x/n
    return division

def run():
    division_by_3 = make_division_of(3)
    print(division_by_3(18))
    
    division_by_5 = make_division_of(5)
    print(division_by_5(100))

    division_by_18 = make_division_of(18)
    print(division_by_18(54))

if __name__ == '__main__':
    run()