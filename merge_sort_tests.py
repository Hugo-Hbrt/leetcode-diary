import unittest

def merge_sort(arr):
    if len(arr) <= 1:
        return arr

    mid = len(arr) // 2
    left_arr = merge_sort(arr[0:mid])
    right_arr = merge_sort(arr[mid:len(arr)])

    i, j, k = 0, 0, 0
    
    while i < len(left_arr) and j < len(right_arr):
        if left_arr[i] <= right_arr[j]:
            arr[k] = left_arr[i]
            i += 1
        else:
            arr[k] = right_arr[j]
            j += 1
        k += 1
    
    while i < len(left_arr):
        arr[k] = left_arr[i]
        i += 1
        k += 1
    while j < len(right_arr):
        arr[k] = right_arr[j]
        j += 1
        k += 1
    
    return arr

def partition(arr, l, r):
    i, j = l, l
    pivot = arr[r]

    while i < r:
        if arr[i] < pivot:
            arr[i], arr[j] = arr[j], arr[i]
            j+=1
        i+=1
    
    arr[r] = arr[j]
    arr[j] = pivot

    return j

def quick_sort_helper(arr, l, r):
    if l >= r:
        return
    
    m = partition(arr, l, r)
    quick_sort_helper(arr, l, m-1)
    quick_sort_helper(arr, m+1, r)
    
def quick_sort(arr):
    quick_sort_helper(arr, 0, len(arr)-1)
    return arr

class TestMergeSort(unittest.TestCase):
    def test_empty_list(self):
        self.assertEqual(merge_sort([]), [])

    def test_single_element(self):
        self.assertEqual(merge_sort([1]), [1])

    def test_sorted_list(self):
        self.assertEqual(merge_sort([1, 2, 3, 4, 5]), [1, 2, 3, 4, 5])

    def test_reverse_sorted_list(self):
        self.assertEqual(merge_sort([5, 4, 3, 2, 1]), [1, 2, 3, 4, 5])

    def test_unsorted_list(self):
        self.assertEqual(merge_sort([3, 1, 4, 1, 5, 9, 2, 6, 5]), [1, 1, 2, 3, 4, 5, 5, 6, 9])

    def test_list_with_duplicates(self):
        self.assertEqual(merge_sort([4, 2, 4, 3, 1, 2]), [1, 2, 2, 3, 4, 4])

    def test_list_with_negative_numbers(self):
        self.assertEqual(merge_sort([-3, -1, -4, -2, 0]), [-4, -3, -2, -1, 0])

class TestQuickSort(unittest.TestCase):
    def test_empty_list(self):
        self.assertEqual(quick_sort([]), [])

    def test_single_element(self):
        self.assertEqual(quick_sort([1]), [1])

    def test_sorted_list(self):
        self.assertEqual(quick_sort([1, 2, 3, 4, 5]), [1, 2, 3, 4, 5])

    def test_reverse_sorted_list(self):
        self.assertEqual(quick_sort([5, 4, 3, 2, 1]), [1, 2, 3, 4, 5])

    def test_unsorted_list(self):
        self.assertEqual(quick_sort([3, 1, 4, 1, 5, 9, 2, 6, 5]), [1, 1, 2, 3, 4, 5, 5, 6, 9])

    def test_list_with_duplicates(self):
        self.assertEqual(quick_sort([4, 2, 4, 3, 1, 2]), [1, 2, 2, 3, 4, 4])

    def test_list_with_negative_numbers(self):
        self.assertEqual(quick_sort([-3, -1, -4, -2, 0]), [-4, -3, -2, -1, 0])

if __name__ == "__main__":
    print(quick_sort([3, 1, 4, 1, 5, 9, 2, 6, 5]))
    unittest.main()