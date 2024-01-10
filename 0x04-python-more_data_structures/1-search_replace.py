#!/usr/bin/python3
def search_replace(my_list, search, replace):
    new_list = my_list.copy()

    for i in range(len(my_list)):
        new_list = list(map(lambda x: replace if x == search else x, my_list))

    return (new_list)
