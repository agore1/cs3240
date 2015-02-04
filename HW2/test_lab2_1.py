__author__ = 'austin'

from HW2.hw2_set import OurSet


def testadd():
    test_set = OurSet()
    assert True == test_set.add(3)
    assert False == test_set.add(3)
    assert True == test_set.addList([1, 3])
    assert False == test_set.addList([1, 3])
    test_set.add(2)
    assert "<3, 1, 2>" == test_set.__str__()
    assert 3 == len(test_set)

    try:
        for i in test_set:
            print(i)
    except ValueError:
        print("Iterator not working.")

if __name__ == '__main__':
    testadd()





