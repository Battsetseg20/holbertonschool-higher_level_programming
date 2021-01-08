#!/usr/bin/python3
"""Module contains function multiplying 2 matrices"""
import numpy as np


def lazy_matrix_mul(m_a, m_b):
    """Mulitplies two matrices"""
    return (np.matmul(m_a, m_b))
