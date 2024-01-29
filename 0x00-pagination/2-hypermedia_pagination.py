#!/usr/bin/env python3


"""
Simple Pagination
"""


from typing import Tuple
import csv
import math
from typing import List, Dict


def index_range(page: int, page_size: int) -> Tuple[int, int]:
    """return a tuple of size two containing a start index and an end index"""
    startIndex = (page - 1) * page_size
    endIndex = startIndex + page_size
    return startIndex, endIndex


class Server:
    """Server class to paginate a database of popular baby names.
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

    def get_page(self, page: int = 1, page_size: int = 10) -> List[List]:
        assert isinstance(
            page, int) and page > 0
        assert isinstance(
            page_size, int) and page_size > 0
        startIndex = (page - 1) * page_size
        endIndex = startIndex + page_size
        with open(self.DATA_FILE) as f:
            reader = csv.reader(f)
            dataset = [row for row in reader]
        totalSize = 19419
        totalPages = math.ceil(totalSize / page_size)
        if page > totalPages:
            return []
        elif page_size > totalPages:
            return []
        else:
            return dataset[startIndex + 1: endIndex + 1]

    def get_hyper(self, page: int = 1, page_size: int = 10) -> Dict:
        totalSize = 19418
        totalPages = math.ceil(totalSize / page_size)
        flag = page_size
        if page - 1 == 0:
            prevPage = None
        else:
            prevPage = page - 1
        if self.get_page(page, page_size) == []:
            nextPage = None
            flag = 0
        else:
            nextPage = page + 1
        return {
            "page_size": flag, "page": page,
            "data": self.get_page(page, page_size),
            "next_page": nextPage, "prev_page": prevPage,
            "total_pages": totalPages
        }
