__author__ = 'austin'


def maxmin(_list):
    if not _list:
        return None
    temp_max = _list[0]
    temp_min = _list[0]
    for i in _list:
        if i < temp_min:
            temp_min = i
        if i > temp_max:
            temp_max = i
    return (temp_max, temp_min)


def common_items(list1, list2):
    result_list = []
    for i in list1:
        if i in list1 and i in list2:
            result_list.append(i)
    return result_list


def notcommon_items(list1, list2):
    result_list = []
    for i in list1:
        if i not in list2:
            result_list.append(i)
    for j in list2:
        if j not in list1:
            result_list.append(j)
    return result_list


def count_list_items(list):
    temp_dict = {}
    for i in list:
        if i in temp_dict:
            temp_dict[i] += 1
        else:
            temp_dict[i] = 1
    return temp_dict


def test_maxmin():
    assert (1, 1) == maxmin([1])
    test_list = [1, 3, 3]
    assert (3, 1) == maxmin(test_list)
    assert (3, -2) == maxmin([3, 1, -2])
    assert ('Z', 'A') == maxmin(['Q', 'Z', 'C', 'A'])


def test_common_items():
    assert [1, 2] == common_items([1, 2, 3], [5, 2, 1])
    assert [] == common_items([1, 2, 3], [4, 5, 6])
    assert ["hey", "bee"] == common_items(["hey", "there", "bee"], ["bee","hey", "hay", "hi"])


def test_notcommon_items():
    assert [1, 2] == notcommon_items([1, 2, 3, 4], [3, 4])
    assert [] == notcommon_items([1, 2], [1, 2])


def test_count_list_items():
    assert {1: 3, 2: 3, 3: 2} == count_list_items([1, 3, 2, 2, 3, 1, 1, 2])
    assert {} == count_list_items([])
    assert {"hello": 1, "world": 2} == count_list_items(["hello", "world", "world"])

if __name__ == "__main__":
    test_maxmin()
    test_common_items()
    test_notcommon_items()
    test_count_list_items()
