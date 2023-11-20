#!/usr/bin/python3
# 3-safe_print_division.py
# Sweilam


def list_division(my_list_1, my_list_2, list_length):
    my_list_ret = []
    for i in range(list_length):
        try:
            div = my_list_1[i] / my_list_2[i]
        except IndexError:
            print('out of range')
            div = 0
        except ZeroDivisionError:
            print('division by 0')
            div = 0 
        except TypeError:
            print('wrong type')
            div = 0
        finally:
            my_list_ret.append(div)
    return (my_list_ret)
        
        
            
            
        
