def run():
    '''for i in range(1, 101):
        i **= 2
        if i %  3 != 0:
            print(i)'''
    '''squares = [i**2 for i  in range(1, 101) if i % 3 != 0]
    print(squares)'''

    squares = [i for i in range(1, 9999) if i % 4 == 0 and i % 6 == 0 and i % 9 == 0]
    print(squares)

if __name__ == '__main__':
    run()