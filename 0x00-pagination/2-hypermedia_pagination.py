#!/usr/bin/env python3
"""Contains a class for interacting with a dataset"""

import csv
import math
from typing import Any, List, Tuple, Dict


class Server:
    """Server class to paginate a database of popular baby names."""

    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None

    def dataset(self) -> List[List]:
        """Cached dataset"""
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]

        return self.__dataset

    def get_page(self, page: int = 1, page_size: int = 10) -> List[List]:
        """Returns a page given the page's index and size"""
        assert isinstance(page, int) and isinstance(
            page_size, int
        ), "Values must be integers"
        assert page > 0 and page_size > 0, "Values must be greater than zero"

        start, end = index_range(page, page_size)

        data = self.dataset()

        if max(start, end) >= len(data):
            return []

        return data[start:end]

    def get_hyper(self, page: int = 1, page_size: int = 10) -> Dict[str, Any]:
        """Returns a dictionary for pagination with the data
        and pagination metadata."""
        data = self.get_page(page, page_size)
        max_page = math.ceil(len(self.dataset()) / page_size)
        next = None if page >= max_page else page + 1
        prev = None if page == 1 else page - 1

        return {
            "page_size": len(data),
            "page": page,
            "data": data,
            "next_page": next,
            "prev_page": prev,
            "total_pages": max_page,
        }


def index_range(page: int, page_size: int) -> Tuple[int, int]:
    """Returns a start index and an end index for given
    pagination parameters.

    Args
        page: the page number(1-indexed)
        page_size: the number of results per page

    Returns
        (start, end)
    """
    start = page_size * (page - 1)
    end = page_size * page

    return (start, end)
