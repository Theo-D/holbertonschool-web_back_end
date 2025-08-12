#!/usr/bin/env python3
"""
Deletion-resilient hypermedia pagination
"""

import csv
import math
from typing import List, Dict



class Server:
    """Server class to paginate a database of popular baby names.
    """
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None
        self.__indexed_dataset = None

    def dataset(self) -> List[List]:
        """Cached dataset
        """
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]

        return self.__dataset

    def indexed_dataset(self) -> Dict[int, List]:
        """Dataset indexed by sorting position, starting at 0
        """
        if self.__indexed_dataset is None:
            dataset = self.dataset()
            truncated_dataset = dataset[:1000]
            self.__indexed_dataset = {
                i: dataset[i] for i in range(len(dataset))
            }
        return self.__indexed_dataset

    def get_hyper_index(self, index: int, page_size: int = 10) -> Dict:
        data_dict: Dict = self.indexed_dataset()
        data_list = []
        item_count = len(self.dataset())
        curr_index = index
        valid_index = 0
        max_index = max(data_dict.keys())

        assert index + page_size < item_count

        while valid_index < page_size and curr_index <= max_index:
            if curr_index in data_dict:
                data_list.append(data_dict[curr_index])
                valid_index += 1
            curr_index += 1

        if (curr_index <= max_index):
            next_index = curr_index
        else:
            next_index = None

        return {
            'index': index,
            'data': data_list,
            'page_size': len(data_list),
            'next_index': next_index
        }
