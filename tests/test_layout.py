import pytest
from django.core.paginator import Paginator

from django_rangepaginator.layout import calculate_pages


@pytest.mark.parametrize("page_num, expected", [
    (1, [1, 2, None, 50]),
    (2, [1, 2, 3, None, 50]),
    (3, [1, 2, 3, 4, None, 50]),
    (4, [1, 2, 3, 4, 5, None, 50]),
    (5, [1, None, 4, 5, 6, None, 50]),
    (6, [1, None, 5, 6, 7, None, 50]),
    (45, [1, None, 44, 45, 46, None, 50]),
    (46, [1, None, 45, 46, 47, None, 50]),
    (47, [1, None, 46, 47, 48, 49, 50]),
    (48, [1, None, 47, 48, 49, 50]),
    (49, [1, None, 48, 49, 50]),
    (50, [1, None, 49, 50]),
])
def test_calculate_range_1(page_num, expected):
    objects = ['foo'] * 50
    paginator = Paginator(objects, 1)
    page = paginator.page(page_num)

    result = calculate_pages(page.number, paginator.num_pages, distance=1)
    assert expected == result


@pytest.mark.parametrize("page_num, expected", [
    (1, [1, 2, 3, None, 50]),
    (2, [1, 2, 3, 4, None, 50]),
    (3, [1, 2, 3, 4, 5, None, 50]),
    (4, [1, 2, 3, 4, 5, 6, None, 50]),
    (5, [1, 2, 3, 4, 5, 6, 7, None, 50]),
    (6, [1, None, 4, 5, 6, 7, 8, None, 50]),
    (45, [1, None, 43, 44, 45, 46, 47, None, 50]),
    (46, [1, None, 44, 45, 46, 47, 48, 49, 50]),
    (47, [1, None, 45, 46, 47, 48, 49, 50]),
    (48, [1, None, 46, 47, 48, 49, 50]),
    (49, [1, None, 47, 48, 49, 50]),
    (50, [1, None, 48, 49, 50]),
])
def test_calculate_range_2(page_num, expected):
    objects = ['foo'] * 50
    paginator = Paginator(objects, 1)
    page = paginator.page(page_num)

    result = calculate_pages(page.number, paginator.num_pages, distance=2)
    assert expected == result


@pytest.mark.parametrize("page_num, expected", [
    (1, [1, 2, 3, 4, None, 50]),
    (2, [1, 2, 3, 4, 5, None, 50]),
    (3, [1, 2, 3, 4, 5, 6, None, 50]),
    (4, [1, 2, 3, 4, 5, 6, 7, None, 50]),
    (5, [1, 2, 3, 4, 5, 6, 7, 8, None, 50]),
    (6, [1, 2, 3, 4, 5, 6, 7, 8, 9, None, 50]),
    (7, [1, None, 4, 5, 6, 7, 8, 9, 10, None, 50]),
    (44, [1, None, 41, 42, 43, 44, 45, 46, 47, None, 50]),
    (45, [1, None, 42, 43, 44, 45, 46, 47, 48, 49, 50]),
    (46, [1, None, 43, 44, 45, 46, 47, 48, 49, 50]),
    (47, [1, None, 44, 45, 46, 47, 48, 49, 50]),
    (48, [1, None, 45, 46, 47, 48, 49, 50]),
    (49, [1, None, 46, 47, 48, 49, 50]),
    (50, [1, None, 47, 48, 49, 50]),
])
def test_calculate_range_3(page_num, expected):
    objects = ['foo'] * 50
    paginator = Paginator(objects, 1)
    page = paginator.page(page_num)

    result = calculate_pages(page.number, paginator.num_pages, distance=3)
    assert expected == result


@pytest.mark.parametrize("page_num, expected", [
    (1, [1]),
])
def test_calculate_1_page(page_num, expected):
    objects = ['foo'] * 1
    paginator = Paginator(objects, 1)
    page = paginator.page(page_num)

    result = calculate_pages(page.number, paginator.num_pages, distance=2)
    assert expected == result


@pytest.mark.parametrize("page_num, expected", [
    (1, [1, 2]),
    (2, [1, 2]),
])
def test_calculate_2_pages(page_num, expected):
    objects = ['foo'] * 2
    paginator = Paginator(objects, 1)
    page = paginator.page(page_num)

    result = calculate_pages(page.number, paginator.num_pages, distance=2)
    assert expected == result


@pytest.mark.parametrize("page_num, expected", [
    (1, [1, 2, 3, 4]),
    (2, [1, 2, 3, 4]),
    (3, [1, 2, 3, 4]),
    (4, [1, 2, 3, 4]),
])
def test_calculate_4_pages(page_num, expected):
    objects = ['foo'] * 4
    paginator = Paginator(objects, 1)
    page = paginator.page(page_num)

    result = calculate_pages(page.number, paginator.num_pages, distance=2)
    assert expected == result
