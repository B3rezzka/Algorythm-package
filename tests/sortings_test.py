import pytest
from src.sortings import bubble_sort, quick_sort, counting_sort, radix_sort, bucket_sort, heap_sort


class TestSortingAlgorithms:
    @pytest.fixture
    def unsorted_int_list(self):
        return [64, 34, 25, 12, 22, 11, 90]

    @pytest.fixture
    def sorted_int_list(self):
        return [11, 12, 22, 25, 34, 64, 90]

    @pytest.fixture
    def empty_list(self):
        return []

    @pytest.fixture
    def single_element_list(self):
        return [42]

    @pytest.fixture
    def reverse_sorted_list(self):
        return [5, 4, 3, 2, 1]

    @pytest.fixture
    def sorted_list(self):
        return [1, 2, 3, 4, 5]

    @pytest.fixture
    def list_with_duplicates(self):
        return [3, 1, 4, 1, 5, 9, 2, 6, 5, 3]

    @pytest.fixture
    def negative_int_list(self):
        return [-5, -2, -8, -1, -9]

    @pytest.fixture
    def mixed_int_list(self):
        return [-5, 2, -8, 1, 9, 0]

    @pytest.fixture
    def float_list_for_bucket(self):
        # Значения в [0, 1)
        return [0.42, 0.32, 0.33, 0.52, 0.37, 0.47, 0.51]

    @pytest.fixture
    def expected_sorted_float_list(self):
        return [0.32, 0.33, 0.37, 0.42, 0.47, 0.51, 0.52]


    def test_bubble_sort_basic(self, unsorted_int_list, sorted_int_list):
        assert bubble_sort(unsorted_int_list) == sorted_int_list

    def test_bubble_sort_empty(self, empty_list):
        assert bubble_sort(empty_list) == []

    def test_bubble_sort_single(self, single_element_list):
        assert bubble_sort(single_element_list) == [42]

    def test_bubble_sort_reverse(self, reverse_sorted_list, sorted_list):
        assert bubble_sort(reverse_sorted_list) == sorted_list

    def test_bubble_sort_duplicates(self, list_with_duplicates):
        assert bubble_sort(list_with_duplicates) == [1, 1, 2, 3, 3, 4, 5, 5, 6, 9]

    def test_quick_sort_basic(self, unsorted_int_list, sorted_int_list):
        assert quick_sort(unsorted_int_list) == sorted_int_list

    def test_quick_sort_empty(self, empty_list):
        assert quick_sort(empty_list) == []

    def test_quick_sort_single(self, single_element_list):
        assert quick_sort(single_element_list) == [42]

    def test_quick_sort_reverse(self, reverse_sorted_list, sorted_list):
        assert quick_sort(reverse_sorted_list) == sorted_list

    def test_quick_sort_duplicates(self, list_with_duplicates):
        assert quick_sort(list_with_duplicates) == [1, 1, 2, 3, 3, 4, 5, 5, 6, 9]

    def test_counting_sort_basic(self, unsorted_int_list, sorted_int_list):
        assert counting_sort(unsorted_int_list) == sorted_int_list

    def test_counting_sort_empty(self, empty_list):
        assert counting_sort(empty_list) == []

    def test_counting_sort_single(self, single_element_list):
        assert counting_sort(single_element_list) == [42]

    def test_counting_sort_duplicates(self, list_with_duplicates):
        assert counting_sort(list_with_duplicates) == [1, 1, 2, 3, 3, 4, 5, 5, 6, 9]

    def test_counting_sort_negative(self, negative_int_list):
        assert counting_sort(negative_int_list) == [-9, -8, -5, -2, -1]

    def test_counting_sort_mixed(self, mixed_int_list):
        assert counting_sort(mixed_int_list) == [-8, -5, 0, 1, 2, 9]

    def test_radix_sort_basic(self, unsorted_int_list, sorted_int_list):
        assert radix_sort(unsorted_int_list) == sorted_int_list

    def test_radix_sort_empty(self, empty_list):
        assert radix_sort(empty_list) == []

    def test_radix_sort_single(self, single_element_list):
        assert radix_sort(single_element_list) == [42]

    def test_radix_sort_duplicates(self, list_with_duplicates):
        assert radix_sort(list_with_duplicates) == [1, 1, 2, 3, 3, 4, 5, 5, 6, 9]

    def test_radix_sort_negative(self, negative_int_list):
        assert radix_sort(negative_int_list) == [-9, -8, -5, -2, -1]

    def test_radix_sort_mixed(self, mixed_int_list):
        assert radix_sort(mixed_int_list) == [-8, -5, 0, 1, 2, 9]

    def test_bucket_sort_basic(self, float_list_for_bucket, expected_sorted_float_list):
        result = bucket_sort(float_list_for_bucket)
        # Используем approx для сравнения float
        assert result == pytest.approx(expected_sorted_float_list)

    def test_bucket_sort_empty(self):
        assert bucket_sort([]) == []

    def test_bucket_sort_single(self):
        assert bucket_sort([0.5]) == [0.5]

    def test_heap_sort_basic(self, unsorted_int_list, sorted_int_list):
        assert heap_sort(unsorted_int_list) == sorted_int_list

    def test_heap_sort_empty(self, empty_list):
        assert heap_sort(empty_list) == []

    def test_heap_sort_single(self, single_element_list):
        assert heap_sort(single_element_list) == [42]

    def test_heap_sort_reverse(self, reverse_sorted_list, sorted_list):
        assert heap_sort(reverse_sorted_list) == sorted_list

    def test_heap_sort_duplicates(self, list_with_duplicates):
        assert heap_sort(list_with_duplicates) == [1, 1, 2, 3, 3, 4, 5, 5, 6, 9]

    def test_heap_sort_negative(self, negative_int_list):
        assert heap_sort(negative_int_list) == [-9, -8, -5, -2, -1]

    def test_heap_sort_mixed(self, mixed_int_list):
        assert heap_sort(mixed_int_list) == [-8, -5, 0, 1, 2, 9]