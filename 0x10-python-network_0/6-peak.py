#!/usr/bin/python3
# find the peak(mode) in a list of unsorted integers


def find_peak(list_of_integers):
    """Return a peak in a list of unsorted integers."""
    if list_of_integers == []:
        return None
    else:
        list_of_integers.sort()
        return list_of_integers[-1]
