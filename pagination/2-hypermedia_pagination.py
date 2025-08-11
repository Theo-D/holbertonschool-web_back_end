#!/usr/bin/env python3
import csv
import math
from typing import List, Tuple, Dict
"""
1-simple_pagination.py -
"""


def index_range(page: int, page_size: int) -> Tuple[int, int]:
    """
    index_range: receives two pos ints and calculates corresponding
    start and end indexes returned as a tuples
    """
    if (page_size > 0 and page > 0):
        start_index = (page - 1) * page_size
        end_index = page * page_size

        tuple_range = (start_index, end_index)

    return tuple_range


class Server:
    """
    Server class to paginate a database of popular baby names.
    """
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None

    def dataset(self) -> List[List]:
        """Cached dataset
        """
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]

        return self.__dataset

    def get_page(self, page: int = 1, page_size: int = 10) -> List[List[str]]:
        """
        get_page : Paginates the content of a dataset with start and end index
        and returns the paginated list of rows.
        """

        assert isinstance(page, int) and page > 0
        assert isinstance(page_size, int) and page_size > 0

        data_list: List[list] = self.dataset()
        index_tuple = index_range(page, page_size)

        if (index_tuple[1] >= len(data_list)):
            data_list = []
            return data_list

        return data_list[index_tuple[0]:index_tuple[1]]

    def get_hyper(self, page: int = 1, page_size: int = 10) -> Dict:
        """
        get_hyper : format the data as follow:
            page_size: the length of the returned dataset page
            page: the current page number
            data: the dataset page (equivalent to return from previous task)
            next_page: number of the next page, None if no next page
            prev_page: number of the previous page, None if no previous page
            total_pages: the total number of pages in the dataset as an integer
        """
        data_dict: Dict = {}
        data_set_size = len(self.dataset())
        data_list = self.get_page(page, page_size)
        next_page = None
        prev_page = None
        total_pages = math.ceil(data_set_size / page_size)

        if (page > 1):
            prev_page = page - 1

        if ((page_size * page) < data_set_size):
            next_page = page + 1
        else:
            next_page = None

        data_dict = {'page_size': page_size,
                     'page': page,
                     'data': data_list,
                     'next_page': next_page,
                     'prev_page': prev_page,
                     'total_pages': total_pages}

        return data_dict
