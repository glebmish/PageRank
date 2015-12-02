from PageRank import *

def test_one():
    pages = {
        'A': Page([], 1)
    }
    ranked_pages = PageRank(pages)
    assert ranked_pages == ['A']

def test_two():
    pages = {
        'A': Page([], 1/2),
        'B': Page(['A', 1/2]),
    }
    ranked_pages = PageRank(pages)
    assert ranked_pages == ['A', 'B']

def test_four_easy():
    pages = {
        'A': Page([], 1/4),
        'B': Page(['A'], 1/4),
        'C': Page(['A'], 1/4),
        'D': Page(['A'], 1/4),
    }
    ranked_pages = PageRank(pages)
    assert ranked_pages[:1] == ['A']

def test_four_hard():
    pages = {
        'A': Page([], 1/4),
        'B': Page(['A', 'C'], 1/4),
        'C': Page(['A'], 1/4),
        'D': Page(['A', 'B', 'C'], 1/4),
    }
    ranked_pages = PageRank(pages)
    assert ranked_pages == ['A', 'C', 'B', 'D']