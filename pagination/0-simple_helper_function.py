#!/usr/bin/env python3
"""
Main file blabla blabl bla blabla blabla
"""
import typing


def index_range(page: int, page_size: int) -> typing.Tuple[int, int]:
    """
    Main file blabla blabl bla blabla blabla
    """
    start_index = (page - 1) * page_size
    end_index = page_size * page
    return (start_index, end_index)
