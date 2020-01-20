import colorama
from colorama import Fore, Back, Style
colorama.init()
old_list = [12, 2, 33, 55, 32, -1, 23, 0]


def bubble_sort(new_list):
    stop_item = len(new_list) - 1
    for z in range(0, stop_item):
        for x in range(0, stop_item - z):
            print(Fore.GREEN + str(new_list))
            if new_list[x] > new_list[x+1]:
                new_list[x], new_list[x+1] = new_list[x+1], new_list[x]

    return new_list


print(Fore.YELLOW + "Old list is==> ", old_list)
my_list = bubble_sort(old_list).copy()
print("New List is", my_list)
