import argparse
import multiprocessing
import threading
import time


class Human:
    def __init__(self, name, occupation):
        self.name = name
        self.occupation = occupation

    def speak(self):
        print(f"{self.name} is a {self.occupation}")


def class_and_objects_demo():
    tom = Human("Tom Cruise", "actor")
    tom.speak()


class Vehicle:
    def general_usage(self):
        print("General use: Transportation")


class Car(Vehicle):
    def __init__(self):
        self.wheels = 4
        self.has_roof = True

    def specific_usage(self):
        print("Specific use: Commute to work")


def inheritance_demo():
    c = Car()
    c.general_usage()
    c.specific_usage()


class Father:
    def gardening(self):
        print("I enjoy gardening")


class Mother:
    def cooking(self):
        print("I enjoy cooking")


class Child(Father, Mother):
    def sports(self):
        print("I enjoy sports")


def multiple_inheritance_demo():
    c = Child()
    c.gardening()
    c.cooking()
    c.sports()


class AdultException(Exception):
    pass


class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def get_minor_age(self):
        if self.age >= 18:
            raise AdultException("Person is an adult")
        return self.age


def raise_exception_demo():
    p = Person("Alice", 20)
    try:
        p.get_minor_age()
    except AdultException as e:
        print(f"Caught custom exception: {e}")
    finally:
        print("Execution completed.")


class RemoteControl:
    def __init__(self):
        self.channels = ["HBO", "CNN", "ABC", "ESPN"]
        self.index = -1

    def __iter__(self):
        return self

    def __next__(self):
        self.index += 1
        if self.index >= len(self.channels):
            raise StopIteration
        return self.channels[self.index]


def iterators_demo():
    r = RemoteControl()
    itr = iter(r)
    print(next(itr))
    print(next(itr))


def fibonacci_gen():
    a, b = 0, 1
    while True:
        yield a
        a, b = b, a + b


def generators_demo():
    for f in fibonacci_gen():
        if f > 20:
            break
        print(f)


def comprehensions_demo():
    numbers = [1, 2, 3, 4, 5, 6, 7]
    even_list = [i for i in numbers if i % 2 == 0]
    print(even_list)

    s = {1, 2, 3, 2, 1, 4}
    sq_set = {x**2 for x in s}
    print(sq_set)

    cities = ["mumbai", "new york", "paris"]
    countries = ["india", "usa", "france"]
    z = zip(cities, countries)
    d = {city: country for city, country in z}
    print(d)


def sets_and_frozen_sets_demo():
    basket = {"apple", "orange", "apple", "pear", "orange", "banana"}
    print(basket)
    fs = frozenset([1, 2, 3, 4])
    print(fs)
    x = {"a", "b", "c"}
    y = {"b", "c", "d"}
    print(x.union(y))
    print(x.intersection(y))


def argparse_demo(args=None):
    parser = argparse.ArgumentParser()
    parser.add_argument("--number1", help="first number", type=int, default=10)
    parser.add_argument("--number2", help="second number", type=int, default=5)
    parser.add_argument("--operation", help="operation", default="add")
    parsed_args = parser.parse_args(args)
    if parsed_args.operation == "add":
        res = parsed_args.number1 + parsed_args.number2
    else:
        res = parsed_args.number1 - parsed_args.number2
    print(f"Argparse result: {res}")


def time_it(func):
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print(f"{func.__name__} took {(end - start)*1000:.2f} ms")
        return result

    return wrapper


@time_it
def calc_square(numbers):
    return [n * n for n in numbers]


def decorators_demo():
    calc_square(range(1, 1000))


def print_numbers():
    for i in range(1, 4):
        time.sleep(0.05)
        print(f"Thread 1: {i}")


def print_letters():
    for char in ["a", "b", "c"]:
        time.sleep(0.05)
        print(f"Thread 2: {char}")


def multithreading_demo():
    t1 = threading.Thread(target=print_numbers)
    t2 = threading.Thread(target=print_letters)
    t1.start()
    t2.start()
    t1.join()
    t2.join()


def square_list(numbers):
    for n in numbers:
        print(f"Square: {n * n}")


def multiprocessing_demo():
    p1 = multiprocessing.Process(target=square_list, args=([1, 2, 3],))
    p1.start()
    p1.join()


def calc_squares(numbers, result, val):
    val.value = 5.33
    for idx, n in enumerate(numbers):
        result[idx] = n * n


def multiprocessing_shared_data_demo():
    numbers = [2, 3, 5]
    result = multiprocessing.Array("i", 3)
    val = multiprocessing.Value("d", 0.0)
    p = multiprocessing.Process(target=calc_squares, args=(numbers, result, val))
    p.start()
    p.join()
    print(list(result))
    print(val.value)


def produce_squares(numbers, q):
    for n in numbers:
        q.put(n * n)


def multiprocessing_queue_demo():
    numbers = [1, 2, 3]
    q = multiprocessing.Queue()
    p = multiprocessing.Process(target=produce_squares, args=(numbers, q))
    p.start()
    p.join()
    while not q.empty():
        print(q.get())


def deposit(balance, lock):
    for _ in range(10):
        time.sleep(0.001)
        lock.acquire()
        balance.value = balance.value + 1
        lock.release()


def withdraw(balance, lock):
    for _ in range(10):
        time.sleep(0.001)
        lock.acquire()
        balance.value = balance.value - 1
        lock.release()


def multiprocessing_lock_demo():
    balance = multiprocessing.Value("i", 200)
    lock = multiprocessing.Lock()
    d = multiprocessing.Process(target=deposit, args=(balance, lock))
    w = multiprocessing.Process(target=withdraw, args=(balance, lock))
    d.start()
    w.start()
    d.join()
    w.join()
    print(f"Final balance: {balance.value}")


def pool_function(n):
    return n * n


def multiprocessing_pool_demo():
    array = [1, 2, 3, 4, 5]
    with multiprocessing.Pool() as p:
        result = p.map(pool_function, array)
    print(result)


def add_numbers(a, b):
    return a + b


def multiply_numbers(a, b):
    return a * b


def test_add_numbers():
    assert add_numbers(2, 3) == 5


def test_multiply_numbers():
    assert multiply_numbers(3, 4) == 12


def pytest_demo():
    test_add_numbers()
    test_multiply_numbers()
    print("Pytest tests passed!")


if __name__ == "__main__":
    class_and_objects_demo()
    inheritance_demo()
    multiple_inheritance_demo()
    raise_exception_demo()
    iterators_demo()
    generators_demo()
    comprehensions_demo()
    sets_and_frozen_sets_demo()
    argparse_demo([])
    decorators_demo()
    multithreading_demo()
    multiprocessing_demo()
    multiprocessing_shared_data_demo()
    multiprocessing_queue_demo()
    multiprocessing_lock_demo()
    multiprocessing_pool_demo()
    pytest_demo()
