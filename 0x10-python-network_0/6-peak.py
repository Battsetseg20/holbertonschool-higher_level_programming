#!/usr/bin/python3
# find the peak(mode) in a list of unsorted integers


def find_peak(list_of_integers):
    """Return a peak in a list of unsorted integers."""
    size = len(list_of_integers)
    if size == 0:
        return None
    else:
        n = int(list_of_integers[0])
        p = list_of_integers[n]
        if (list_of_integers[n - 1] <= p and list_of_integers[n + 1] <= p):
            return p
        else:
            return find_peak(list_of_integers[n+1])

