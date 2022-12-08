the_int = 99
the_list = [1, 2, 3]


def my_function_1(an_int, a_list):
    print(f"1.1 an_int ({id(an_int)}) is {an_int}, a_list ({id(a_list)}) is {a_list}")
    an_int = 77
    a_list.append(500)
    print(f"1.2 an_int ({id(an_int)}) is {an_int}, a_list ({id(a_list)}) is {a_list}")


def my_function_2(*args, **kwargs):
    for arg in args:
        print(f"{arg}")
    for k, v in kwargs.items():
        print(f"{k}: {v}")

    return "obj1", "obj2", "obj3"


def my_function_3(list_3_1):
    list_3_1.append(999)

    return list_3_1


print(f"1. the_int ({id(the_int)}) is {the_int}, the_list ({id(the_list)}) is {the_list}")

my_function_1(the_int, the_list)
my_function_1(a_list=the_list, an_int=the_int)
fun2result = my_function_2(88, 77, 66, k1=22, k2=33)

print(f"2. the_int ({id(the_int)}) is {the_int}, the_list ({id(the_list)}) is {the_list}")

list_3_result = my_function_3(the_list)

print(f"the_list: {the_list} ... list_3_result: {list_3_result}")