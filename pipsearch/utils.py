# -*- coding:utf-8 -*-
"""pipsearch

 Module  from pipsearch.

 - Package:
 - Author: godmin
 - Created; 21/6/24
"""
import random
import time


def wait(min_time: float = 0.5, max_time: float = 1.5):
    """Wait for a random time between min_time and max_time.

    :param min_time: Minimum time to wait in seconds.
    :param max_time: Maximum time to wait in seconds.
    """
    time.sleep(random.uniform(min_time, max_time))
