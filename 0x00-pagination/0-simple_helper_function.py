#!/usr/bin/env python3


"""
Simple Helper Function
"""


from typing import Tuple


def index_range(page: int, page_size: int) -> Tuple[int, int]:
    """return a tuple of size two containing a start index and an end index"""
    startIndex = (page - 1) * page_size
    endIndex = startIndex + page_size
    return startIndex, endIndex
