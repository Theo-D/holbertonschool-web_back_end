#!/usr/bin/env python3
import csv
import math
from typing import List, Tuple
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
