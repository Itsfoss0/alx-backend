#!/usr/bin/env python3

"""
This module contains the simple pagination class
And the helper functions to practice cursor based
API pagination
"""

import csv
import math
from typing import List, Tuple


class Server:
    """Server class to paginate a database of popular baby names.
    """
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        """
        The constructor
        """
        self.__dataset = None

    def dataset(self) -> List[List]:
        """
        Cached dataset
        """
        if self.__dataset is None:
            with open(self.DATA_FILE, "r", encoding="utf-8") as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]

        return self.__dataset

    @staticmethod
    def index_range(page: int, page_size: int) -> Tuple[int, int]:
        """
        The Actuall helper function
        Args:
            page (int):
            page_size (int):
        Returns:
            Returns an tupple of ints
        """
        if isinstance(page, int) and isinstance(page_size, int):
            return ((page - 1) * page_size, page_size * page)
        raise TypeError('Expected `page` and `page_size` to be ints')

    def get_page(self, page: int = 1, page_size: int = 10) -> List[List]:
        """
        Get paginated data
        Args:
            page (int)
            page_size (int)
        """
        assert isinstance(page, int) and page > 0
        assert isinstance(page_size, int) and page_size > 0

        data = self.dataset()

        try:
            (start, end) = index_range(page, page_size)
            return data[start:end]
        except IndexError:
            return []
