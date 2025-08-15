#!/usr/bin/env python3
import csv
import math
from typing import List, Tuple
"""
1-simple_pagination.py -
"""


def index_range(page: int, page_size: int) -> Tuple[int, int]:
    """
    Calculate the start and end index for pagination.

    Args:
        page (int): current page number (1-indexed)
        page_size (int): number of items per page

    Returns:
        Tuple[int, int]: tuple containing start and end index
    """
    start = (page - 1) * page_size
    end = page * page_size
    return start, end


class Server:
    """
    Server class to paginate a dataset from a CSV file.
    """
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None

    def dataset(self) -> List[List[str]]:
        """
        Load and cache dataset from the CSV file.

        Returns:
            List[List[str]]: dataset excluding the header row
        """
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]
        return self.__dataset

    def get_page(self, page: int = 1, page_size: int = 10) -> List[List[str]]:
        """
        Get a page of the dataset based on pagination parameters.

        Args:
            page (int): page number (1-indexed)
            page_size (int): number of items per page

        Returns:
            List[List[str]]: the paginated data rows
        """
        assert isinstance(page, int)
        assert isinstance(page_size, int)
        assert page > 0
        assert page_size > 0

        data = self.dataset()
        start, end = index_range(page, page_size)

        results: List[List[str]] = []

        if start < len(data) and end < len(data):
            for i in range(end - start):
                results.append(data[start + i + 1])

        return results
