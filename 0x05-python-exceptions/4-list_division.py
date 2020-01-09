#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    my_list_3 = []
    for i in range(list_length):
        try:
            op = my_list_1[i] / my_list_2[i]
        except ZeroDivisionError:
            print("division by 0")
            op = 0
        except TypeError:
            print("wrong type")
            op = 0
        except IndexError:
            print("out of range")
            op = 0
        finally:
            my_list_3.append(op)
    return my_list_3
