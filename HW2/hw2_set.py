__author__ = 'austin'


class OurSet:
    """Simple set class.
        Implements add, add_list, union and intersection functions.
        Also overrides __len__, __str__ and __iter__ functions."""
    def __init__(self):
        self.list = []

    def add(self, item):
        """Add an item to the set if not already present."""
        if item not in self.list:
            self.list.append(item)
            return True
        else:
            return False

    def add_list(self, list):
        """Attempt to add all items in list, return true if at least one is added."""
        result = False
        for i in list:
            flag = self.add(i)
            if flag:
                result = True
        return result

    def __len__(self):
        return len(self.list)

    def __str__(self):
        """The special string format, eg. <1, 2, 3>"""
        # add each item in the list to the string
        string = self.list.__str__()
        string = string.replace('[', '<')
        string = string.replace(']', '>')
        return string

    def __iter__(self):
        """Return an iterator."""
        return self.list.__iter__()

    def union(self, set2):
        """Union this set and set2, return a new set."""
        union = OurSet()
        for i in self:
            union.add(i)
        for j in set2:
            union.add(j)
        return union

    def intersection(self, set2):
        intersection = OurSet()
        for i in self:
            if i in set2:
                intersection.add(i)
        return intersection


def testadd():
    test_set = OurSet()
    assert True == test_set.add(3)
    assert False == test_set.add(3)
    assert True == test_set.add_list([1, 3])
    assert False == test_set.add_list([1, 3])
    test_set.add(2)
    assert "<3, 1, 2>" == test_set.__str__()
    assert 3 == len(test_set)

    try:
        for i in test_set:
            print(i)
    except ValueError:
        print("Iterator not working.")

    # print(test_set.__str__())


def testunion():
    set1 = OurSet()
    set2 = OurSet()
    set1.add_list([1, 2, 3])
    set2.add_list([3, 4, 5])
    set3 = set1.union(set2)
    assert "<1, 2, 3, 4, 5>" == set3.__str__()
    print(set3)


def testintersection():
    set1 = OurSet()
    set2 = OurSet()
    set1.add_list([1, 2, 3])
    set2.add_list([3, 4, 5])
    set3 = set2.intersection(set1)
    assert "<3>" == set3.__str__()
    print(set3)


if __name__ == "__main__":
    testadd()
    print([1, 2, 3])
    test = "[1, 2, 3]"
    # test[1] = '<'
    print(test.__str__())
    testunion()
    testintersection()

