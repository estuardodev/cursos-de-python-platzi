def run():
    # dicts = {i: i**3 for i in range(1,101) if i % 3 != 0}

    '''for i in range(1,101):
        if i % 3 != 0:
            dicts[i] = i**3'''

    dictionary = {i: i**(0.5) for i in range (1, 1001)}
    print(dictionary)

if __name__ == '__main__':
    run()