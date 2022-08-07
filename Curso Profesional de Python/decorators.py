from datetime import datetime

def execution_time(func):
    def wrapper(a, b):
        initial_time = datetime.now()
        func(a, b)
        final_time = datetime.now()
        time_elapsed = final_time - initial_time
        print("Pasaron " + str(time_elapsed.total_seconds()) + "segundos")
    return wrapper

@execution_time
def random_func():
    for _ in range(1, 1000000):
        pass

# random_func()


def suma(a: int, b: int) -> int:
    return a + b