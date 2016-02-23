#!/usr/bin/python
# -*- coding: utf-8 -*-

import time
from progressbar import ProgressBar

TIME_WINDOW_SECONDS = 3


def calculate(loops):
    sleep_value = float(TIME_WINDOW_SECONDS) / loops
    pbar = ProgressBar().start()
    for i in range(loops):
        time.sleep(sleep_value)
        # Do your stuff here!
        pbar.update((i + 1) * 100 / loops)
    pbar.finish()


if __name__ == '__main__':
    print("1% percent progression:")
    calculate(100)
    print("10% percent progression:")
    calculate(10)
