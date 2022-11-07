from zad10 import bubblesort, random_list_generator


def test_sample_list():
    testlist = [1, 3, 2, 4, 9, 5, 7, 8, 6]
    sortlist = bubblesort(testlist)
    assert(sortlist == [9, 8, 7, 6, 5, 4, 3, 2, 1])

def test_empty():
    testlist = []
    sortlist = bubblesort(testlist)
    assert(sortlist == [])

def test_big_data():
    mylist = random_list_generator(50, 99)
    reference = mylist
    reference.sort(reverse=True)
    mylistsorted = bubblesort(mylist)
    assert(mylistsorted == reference)
