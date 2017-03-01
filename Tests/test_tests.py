def load_src(name, fpath):
    import os, imp
    p = fpath if os.path.isabs(fpath) \
        else os.path.join(os.path.dirname(__file__), fpath)
    return imp.load_source(name, p)

load_src('PageRank', "../PageRank.py")
from PageRank import *


def test_one():
    pages = {
        'A': Page('A', []),
    }
    ranked_pages = page_rank(pages)
    assert ranked_pages == ['A']


def test_two():
    pages = {
        'A': Page('A', []),
        'B': Page('B', ['A']),
    }
    ranked_pages = page_rank(pages)
    assert ranked_pages == ['A', 'B']


def test_four_easy():
    pages = {
        'A': Page('A', []),
        'B': Page('B', ['A']),
        'C': Page('C', ['A']),
        'D': Page('D', ['A']),
    }
    ranked_pages = page_rank(pages)
    print(ranked_pages)
    assert ranked_pages == ['A', 'B', 'C', 'D']


def test_four_hard():
    pages = {
        'A': Page('A', []),
        'B': Page('B', ['A', 'C']),
        'C': Page('C', ['A']),
        'D': Page('D', ['A', 'B', 'C']),
    }
    ranked_pages = page_rank(pages)
    assert ranked_pages == ['A', 'C', 'B', 'D']