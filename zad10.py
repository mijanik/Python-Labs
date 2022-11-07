import random


def random_list_generator(length, num_range):
    randomlist = []
    for i in range(0, num_range):
        randomlist.append(random.randint(0, num_range))
    return randomlist


def bubblesort(list1):
    for i in range(0,len(list1)-1):
        for j in range(len(list1)-1):
            if(list1[j]<list1[j+1]):
                temp = list1[j]
                list1[j] = list1[j+1]
                list1[j+1] = temp
    return list1


if __name__ == "__main__":
    pass
