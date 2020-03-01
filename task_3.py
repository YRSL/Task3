from concurrent.futures import ThreadPoolExecutor
from threading import Lock


class ModifiableObject:
    def __init__(self):
        self.__a = 0
        self.__lock = Lock()

    @property
    def a(self):
        return self.__a

    @a.setter
    def a(self, a):
        if a:
            self.__a = a
        else:
            print("Incorrect value")

    @property
    def get_lock(self):
        return self.__lock


def function(arg, my_obj):
    for _ in range(arg):
        with my_obj.get_lock:
            my_obj.a += 1
    return my_obj.a


def main():

    my_obj = ModifiableObject()
    max_workers = 5
    value = 1000000

    with ThreadPoolExecutor(max_workers) as executor:
        for worker in range(max_workers):
            executor.submit(function, value, my_obj)
    print("----------------------", my_obj.a)


if __name__ == "__main__":
        main()
