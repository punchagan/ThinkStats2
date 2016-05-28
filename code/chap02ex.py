"""This file contains code for use with "Think Stats",
by Allen B. Downey, available from greenteapress.com

Copyright 2014 Allen B. Downey
License: GNU GPLv3 http://www.gnu.org/licenses/gpl.html
"""

from __future__ import print_function

import sys
from operator import itemgetter

import first
import thinkstats2


def Mode(hist):
    """Returns the value with the highest frequency.

    hist: Hist object

    returns: value from Hist
    """

    return max(hist.Items(), key=lambda x: x[1])[0]


def AllModes(hist):
    """Returns value-freq pairs in decreasing order of frequency.

    hist: Hist object

    returns: iterator of value-freq pairs
    """

    return sorted(hist.Items(), key=lambda x: x[1], reverse=True)

def compute_Cohen_d(column_name, live, first, others):
    """Compute Cohen's Coefficient d for the given column."""

    s = live[column_name].std()
    d = abs(first[column_name].mean() - others[column_name].mean())/s
    return d

def main(script):
    """Tests the functions in this module.

    script: string script name
    """
    live, firsts, others = first.MakeFrames()
    hist = thinkstats2.Hist(live.prglngth)

    # test Mode
    mode = Mode(hist)
    print('Mode of preg length', mode)
    assert(mode == 39)

    # test AllModes
    modes = AllModes(hist)
    assert(modes[0][1] == 4693)

    for value, freq in modes[:5]:
        print(value, freq)

    print('%s: All tests passed.' % script)

    d = compute_Cohen_d('totalwgt_lb', live, firsts, others)
    print('%s: d for totalwgt_lb' % d)

    d = compute_Cohen_d('prglngth', live, firsts, others)
    print('%s: d for prglngth' % d)

if __name__ == '__main__':
    main(*sys.argv)
