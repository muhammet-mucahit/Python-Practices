"""This is the module docstring."""


def keyword_list():
    import keyword
    print(keyword.kwlist)


def is_instance():
    issubclass(bool, int)  # True
    isinstance(True, bool)  # True
    isinstance(False, bool)  # True


def datatype_list():
    names = ['Alice', 'Bob', 'Craig', 'Diana', 'Eric']
    names.append("Sia")
    names.insert(1, "Nikki")
    names.remove("Bob")
    names.index("Alice")
    len(names)
    names.count("Alice")

    names.reverse()
    names[::-1]
    names.pop()

    a = [1, 2, 3, 4, 5, 6, 7, 7]
    b = [8, 9, 10]
    # Extend list by appending all elements from b
    a.extend(b)
    # a: [1, 2, 3, 4, 5, 6, 7, 7, 8, 9, 10]

    a.pop(8)
    # Returns: 7
    # a: [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

    a.sort(reverse=True)

    # ----------------------------------------------------------------------
    class Person:
        def __init__(self, name):
            self.name = name

    l = [
        Person("John Cena"),
        Person("Chuck Norris"),
        Person("Jon Skeet")
    ]
    l.sort(key=lambda item: item.name)

    # ----------------------------------------------------------------------
    import datetime
    l = [{'name': 'John Cena', 'birthday': datetime.date(1992, 9, 12),
          'height': 175},
         {'name': 'Chuck Norris', 'birthday': datetime.date(1990, 8, 28),
          'height': 180},
         {'name': 'Jon Skeet', 'birthday': datetime.date(1991, 7, 6),
          'height': 185}]
    l.sort(key=lambda item: item['name'])
    # l: [Chuck Norris, John Cena, Jon Skeet]
    l.sort(key=lambda item: item['birthday'])
    # l: [Chuck Norris, Jon Skeet, John Cena]
    l.sort(key=lambda item: item['height'])
    # l: [John Cena, Chuck Norris, Jon Skeet]

    # ----------------------------------------------------------------------
    l = [{'name': 'John Cena', 'birthday': datetime.date(1992, 9, 12),
          'size': {'height': 175,
                   'weight': 100}},
         {'name': 'Chuck Norris', 'birthday': datetime.date(1990, 8, 28),
          'size': {'height': 180,
                   'weight': 90}},
         {'name': 'Jon Skeet', 'birthday': datetime.date(1991, 7, 6),
          'size': {'height': 185,
                   'weight': 110}}]
    l.sort(key=lambda item: item['size']['height'])

    # ----------------------------------------------------------------------
    from operator import itemgetter, attrgetter
    people = [{'name': 'chandan', 'age': 20, 'salary': 2000},
              {'name': 'chetan', 'age': 18, 'salary': 5000},
              {'name': 'guru', 'age': 30, 'salary': 3000}]
    by_age = itemgetter('age')
    by_salary = itemgetter('salary')
    people.sort(key=by_age)  # in-place sorting by age
    people.sort(key=by_salary)  # in-place sorting by salary

    # ----------------------------------------------------------------------
    list_of_tuples = [(1, 2), (3, 4), (5, 0)]
    list_of_tuples.sort(key=itemgetter(1))
    print(list_of_tuples)  # [(5, 0), (1, 2), (3, 4)]

    # ----------------------------------------------------------------------
    b = ["blah"] * 3
    # b = ["blah", "blah", "blah"]

    # ----------------------------------------------------------------------
    a = list(range(10))
    del a[::2]
    # a = [1, 3, 5, 7, 9]
    del a[-1]
    # a = [1, 3, 5, 7]
    del a[:]
    # a = []

    b = a
    a.append(6)
    # b: [1, 2, 3, 4, 5, 6]

    # ----------------------------------------------------------------------
    lst = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']
    lst[::2]
    # Output: ['a', 'c', 'e', 'g']
    lst[::3]
    # Output: ['a', 'd', 'g']


def datatype_tuple():
    one_member_tuple = ('Only member',)
    one_member_tuple = 'Only member',
    one_member_tuple = tuple(['Only member'])

    t = tuple('lupins')
    print(t)  # ('l', 'u', 'p', 'i', 'n', 's')
    t = tuple(range(3))
    print(t)  # (0, 1, 2)

    first, *more, last = (1, 2, 3, 4, 5)
    # first == 1
    # more == [2, 3, 4]
    # last == 5

    tuple1 = ('a', 'b', 'c', 'd', 'e')
    tuple2 = ('1', '2', '3')
    tuple3 = ('a', 'b', 'c', 'd', 'e')

    max(tuple2)
    # Out: '3'

    out = tuple1 + tuple2
    # Out: ('a', 'b', 'c', 'd', 'e', '1', '2', '3')

    hash((1, 2))  # ok
    hash(([], {"hello"}))  # not ok, since lists and sets are not hashabe


def datatype_defaultdict():
    """
    A defaultdict will never raise a KeyError. Any key that does not exist
    gets the default value returned
    """
    from collections import defaultdict
    state_capitals = defaultdict(lambda: 'Boston')
    state_capitals['Arkansas'] = 'Little Rock'
    print(state_capitals['Alabama'])
    print(state_capitals['Arkansas'])


def builtins_python():
    import math
    dir(__builtins__)
    dir(math)
    print(math.__doc__)
    import main
    print(main.__doc__)
    print(main.datatype_defaultdict.__doc__)


def method_helper():
    help(max)
    help(pow)


def hello(name, language="en"):
    """Say hello to a person.
    :param name: the name of the person
    :type name: str
    :param language: the language in which the person should be greeted
    :type language: str
    :return: a number
    :rtype: int
    """
    pass


def hello_google_style(name, language="en"):
    """Say hello to a person.
    Args:
        name: the name of the person as string
        language: the language code string
    Returns:
        A number.
    """
    pass


def operation_on_sets():
    # Intersection
    {1, 2, 3, 4, 5}.intersection({3, 4, 5, 6})  # {3, 4, 5}
    {1, 2, 3, 4, 5} & {3, 4, 5, 6}  # {3, 4, 5}
    # Union
    {1, 2, 3, 4, 5}.union({3, 4, 5, 6})  # {1, 2, 3, 4, 5, 6}
    {1, 2, 3, 4, 5} | {3, 4, 5, 6}  # {1, 2, 3, 4, 5, 6}
    # Difference
    {1, 2, 3, 4}.difference({2, 3, 5})  # {1, 4}
    {1, 2, 3, 4} - {2, 3, 5}  # {1, 4}
    # Symmetric difference with
    {1, 2, 3, 4}.symmetric_difference({2, 3, 5})  # {1, 4, 5}
    {1, 2, 3, 4} ^ {2, 3, 5}  # {1, 4, 5}
    # Superset check
    {1, 2}.issuperset({1, 2, 3})  # False
    {1, 2} >= {1, 2, 3}  # False
    # Subset check
    {1, 2}.issubset({1, 2, 3})  # True
    {1, 2} <= {1, 2, 3}  # True
    # Disjoint check
    {1, 2}.isdisjoint({3, 4})  # True
    {1, 2}.isdisjoint({1, 4})  # False

    # Existence check
    2 in {1, 2, 3}  # True
    4 in {1, 2, 3}  # False
    4 not in {1, 2, 3}  # True
    # Add and Remove
    s = {1, 2, 3}
    s.add(4)  # s == {1,2,3,4}
    s.discard(3)  # s == {1,2,4}
    s.discard(5)  # s == {1,2,4} No key error, returns None
    s.remove(2)  # s == {1,4}
    s.remove(2)  # KeyError!

    """
    Set operations return new sets, but have the corresponding in-place versions
    method in-place operation in-place method
    union ----------------> s |= t -> update
    intersection ---------> s &= t -> intersection_update
    difference -----------> s -= t -> difference_update
    symmetric_difference -> s ^= t -> symmetric_difference_update
    """

    s = {1, 2}
    s.update({3, 4})  # s == {1, 2, 3, 4}


def datatype_counter():
    from collections import Counter
    counterA = Counter(['a', 'b', 'b', 'c'])
    # counterA = Counter({'b': 2, 'a': 1, 'c': 1})


foo = 1


def global_local_scope():
    print(globals().keys())  # prints all variable names in global scope
    print(locals().keys())  # prints all variable names in local scope

    foo = 2  # creates a new variable foo in local scope
    print(foo)  # prints 2
    # global variable foo still exists, unchanged:
    print(globals()['foo'])  # prints 1
    print(locals()['foo'])  # prints 2


def group_by_exercises():
    from itertools import groupby
    things = [("animal", "bear"), ("animal", "duck"), ("plant", "cactus"),
              ("vehicle", "harley"), \
              ("vehicle", "speed boat"), ("vehicle", "school bus")]
    dic = {}
    f = lambda x: x[0]
    for key, group in groupby(sorted(things, key=f), f):
        dic[key] = list(group)

    # Result:
    # {'animal': [('animal', 'bear'), ('animal', 'duck')],
    #  'plant': [('plant', 'cactus')],
    #  'vehicle': [('vehicle', 'harley'),
    #              ('vehicle', 'speed boat'),
    #              ('vehicle', 'school bus')]}

    list_things = ['goat', 'dog', 'donkey', 'mulato', 'cow', 'cat',
                   ('persons', 'man', 'woman'), \
                   'wombat', 'mongoose', 'malloo', 'camel']
    c = groupby(list_things, key=lambda x: x[0])
    dic = {}
    for k, v in c:
        dic[k] = list(v)

    # {'c': ['camel'],
    #  'd': ['dog', 'donkey'],
    #  'g': ['goat'],
    #  'm': ['mongoose', 'malloo'],
    #  'persons': [('persons', 'man', 'woman')],
    #  'w': ['wombat']}


def calendar_module():
    import calendar
    print(calendar.TextCalendar(firstweekday=6).formatyear(2015))


def heap_q():
    import heapq
    numbers = [1, 4, 2, 100, 20, 50, 32, 200, 150, 8]
    print(heapq.nlargest(4, numbers))  # [200, 150, 100, 50]
    print(heapq.nsmallest(4, numbers))  # [1, 2, 4, 8]

    people = [
        {'firstname': 'John', 'lastname': 'Doe', 'age': 30},
        {'firstname': 'Jane', 'lastname': 'Doe', 'age': 25},
        {'firstname': 'Janie', 'lastname': 'Doe', 'age': 10},
        {'firstname': 'Jane', 'lastname': 'Roe', 'age': 22},
        {'firstname': 'Johnny', 'lastname': 'Doe', 'age': 12},
        {'firstname': 'John', 'lastname': 'Roe', 'age': 45}
    ]
    oldest = heapq.nlargest(2, people, key=lambda s: s['age'])
    print(oldest)


def input_output():
    with open('shoppinglist.txt', 'r') as fileobj:
        # this method reads line by line:
        lines = []
        for line in fileobj:
            lines.append(line.strip())

    # with open(input_file, 'r') as in_file, open(output_file, 'w') as out_file:
    #     for line in in_file:
    #         out_file.write(line)

    # import shutil
    # shutil.copyfile(src, dst)


def os_module():
    import os
    os.path.join('a', 'b', 'c')
    # 'a\b\c'


def iterator_and_iterables():
    class MyIterable:
        def __iter__(self):
            return self

        def __next__(self):
            pass

    s = {1, 2}  # or list or generator or even iterator
    i = iter(s)  # get iterator
    a = next(i)  # a = 1
    b = next(i)  # b = 2
    c = next(i)  # raises StopIteration

    def gen():
        yield 1

    iterable = gen()
    for a in iterable:
        print(a)


def lambda_function():
    greet_me = lambda: "Hello"
    print(greet_me())

    strip_and_upper_case = lambda s: s.strip().upper()
    strip_and_upper_case(" Hello ")
    # HELLO

    greeting = lambda x, *args, **kwargs: print(x, args, kwargs)
    greeting('hello', 'world', world='world')
    # hello ('world',) {'world': 'world'}

    sorted([" foo ", " bAR", "BaZ "], key=lambda s: s.strip().upper())
    # [' bAR', 'BaZ ', ' foo ']

    sorted([" foo ", " bAR", "BaZ "], key=lambda s: s.strip())
    # ['BaZ ', ' bAR', ' foo ']

    sorted(map(lambda s: s.strip().upper(), [" foo ", " bAR", "BaZ "]))
    # ['BAR', 'BAZ', 'FOO']

    lambda_factorial = lambda i: 1 if i == 0 else i * lambda_factorial(i - 1)
    print(lambda_factorial(4))  # 4 * 3 * 2 * 1 = 12 * 2 = 24


def closure():
    def makeInc(x):
        def inc(y):
            return y + x

        return inc

    incOne = makeInc(1)
    incFive = makeInc(5)

    incOne(5)  # returns 6
    incFive(5)  # returns 10


def functional_programming():
    from functools import reduce

    s = lambda x: x * x
    s(2)  # => 4
    name_lengths = map(len, ["Mary", "Isla", "Sam"])
    print(name_lengths)  # => [4, 4, 3]

    total = reduce(lambda a, x: a + x, [0, 1, 2, 3, 4])
    print(total)  # => 10

    arr = [1, 2, 3, 4, 5, 6]
    output = [i for i in filter(lambda x: x > 4, arr)]
    # output => [5,6]


def decorators():
    def super_secret_function(f):
        return f

    @super_secret_function
    def my_function():
        print("This is my secret function.")

    # The @ -notation is syntactic sugar that is equivalent to the following:
    # my_function = super_secret_function(my_function)
    # --------------------------------------------------

    def disabled(f):
        """
        This function returns nothing, and hence removes the decorated function
        from the local scope.
        """
        pass

    @disabled
    def my_function():
        print("This function can no longer be called...")

    my_function()  # TypeError: 'NoneType' object is not callable

    # --------------------------------------------------

    # This is the decorator
    def print_args(func):
        def inner_func(*args, **kwargs):
            print(args)
            print(kwargs)
            return func(*args, **kwargs)

        return inner_func

    @print_args
    def multiply(num_a, num_b):
        return num_a * num_b

    print(multiply(3, 5))

    # --------------------------------------------------
    class Decorator(object):
        """Simple decorator class."""

        def __init__(self, func):
            self.func = func

        def __call__(self, *args, **kwargs):
            print('Before the function call.')
            res = self.func(*args, **kwargs)
            print('After the function call.')
            return res

    @Decorator
    def testfunc():
        print('Inside the function.')

    testfunc()
    # Before the function call.
    # Inside the function.
    # After the function call.

    # Note that a function decorated with a class decorator will no longer
    # be considered a "function" from type-checking perspective:
    import types
    isinstance(testfunc, types.FunctionType)
    # False
    type(testfunc)
    # <class '__main__.Decorator'>
    # --------------------------------------------------

    from types import MethodType

    class Decorator(object):
        def __init__(self, func):
            self.func = func

        def __call__(self, *args, **kwargs):
            print('Inside the decorator.')
            return self.func(*args, **kwargs)

        def __get__(self, instance, cls):
            # Return a Method if it is called on an instance
            return self if instance is None else MethodType(self, instance)

    class Test(object):
        @Decorator
        def __init__(self):
            pass

    a = Test()

    # --------------------------------------------------

    def decoratorfactory(message):
        def decorator(func):
            def wrapped_func(*args, **kwargs):
                print('The decorator wants to tell you: {}'.format(message))
                return func(*args, **kwargs)

            return wrapped_func

        return decorator

    @decoratorfactory('Hello World')
    def test():
        pass

    # test() --> The decorator wants to tell you: Hello World
    # --------------------------------------------------

    def decoratorfactory(*decorator_args, **decorator_kwargs):
        class Decorator(object):
            def __init__(self, func):
                self.func = func

        def __call__(self, *args, **kwargs):
            print('Inside the decorator with arguments {}'.format(
                decorator_args
            ))

            return self.func(*args, **kwargs)

        return Decorator

    @decoratorfactory(10)
    def test():
        pass

    # test() --> Inside the decorator with arguments (10,)
    # --------------------------------------------------
    from functools import wraps

    def decorator(func):
        # Copies the docstring, name, annotations and module to the decorator
        @wraps(func)
        def wrapped_func(*args, **kwargs):
            return func(*args, **kwargs)

        return wrapped_func

    @decorator
    def test():
        pass

    # test.__name__ --> 'test'
    # --------------------------------------------------

    class Decorator(object):
        def __init__(self, func):
            # Copies name, module, annotations and docstring to the instance.
            self._wrapped = wraps(func)(self)

        def __call__(self, *args, **kwargs):
            return self._wrapped(*args, **kwargs)

    @Decorator
    def test():
        """Docstring of test."""
        pass

    # test.__doc__ --> 'Docstring of test.'
    # --------------------------------------------------
    import time
    def timer(func):
        def inner(*args, **kwargs):
            t1 = time.time()
            f = func(*args, **kwargs)
            t2 = time.time()
            print('Runtime took {0} seconds'.format(t2 - t1))
            return f

        return inner

    @timer
    def example_function():
        pass

    # --------------------------------------------------
    # Singleton Pattern with Decorator
    def singleton(cls):
        instance = [None]

        def wrapper(*args, **kwargs):
            if instance[0] is None:
                instance[0] = cls(*args, **kwargs)
            return instance[0]

        return wrapper

    @singleton
    class SomeSingletonClass:
        x = 2

        def __init__(self):
            print("Created!")

    instance = SomeSingletonClass()  # prints: Created!
    instance = SomeSingletonClass()  # doesn't print anything
    print(instance.x)  # 2
    instance.x = 3
    print(SomeSingletonClass().x)  # 3
    # --------------------------------------------------

