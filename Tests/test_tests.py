from PageRank import *

def test_one():
    pages = {
        'A': Page([]),
    }
    ranked_pages = PageRank(pages)
    assert ranked_pages == ['A']

def test_two():
    pages = {
        'A': Page([]),
        'B': Page(['A']),
    }
    ranked_pages = PageRank(pages)
    assert ranked_pages == ['A', 'B']

def test_four_easy():
    pages = {
        'A': Page([]),
        'B': Page(['A']),
        'C': Page(['A']),
        'D': Page(['A']),
    }
    ranked_pages = PageRank(pages)
    assert ranked_pages[:1] == ['A']

def test_four_hard():
    pages = {
        'A': Page([]),
        'B': Page(['A', 'C']),
        'C': Page(['A']),
        'D': Page(['A', 'B', 'C']),
    }
    ranked_pages = PageRank(pages)
    assert ranked_pages == ['A', 'C', 'B', 'D']