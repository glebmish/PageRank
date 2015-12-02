from PageRank import *

def test_one():
    pages = {
        'A': [],
    }
    ranked_pages = PageRank(pages)
    assert ranked_pages == ['A']

def test_two():
    pages = {
        'A': [],
        'B': ['A'],
    }
    ranked_pages = PageRank(pages)
    assert ranked_pages == ['A', 'B']

def test_four_easy():
    pages = {
        'A': [],
        'B': ['A'],
        'C': ['A'],
        'D': ['A'],
    }
    ranked_pages = PageRank(pages)
    assert ranked_pages[:1] == ['A']

def test_four_hard():
    pages = {
        'A': [],
        'B': ['A', 'C'],
        'C': ['A'],
        'D': ['A', 'B', 'C'],
    }
    ranked_pages = PageRank(pages)
    assert ranked_pages == ['A', 'C', 'B', 'D']