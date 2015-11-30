import PageRank

def test_one():
    pages = [
        PageRank.Page('A', []),
    ]
    ranked_pages = PageRank.PageRank(pages)
    assert ranked_pages == ['A']

def test_two():
    pages = [
        PageRank.Page('A', []),
        PageRank.Page('B', ['A'])
    ]
    ranked_pages = PageRank.PageRank(pages)
    assert ranked_pages == ['A', 'B']

def test_four_easy():
    pages = [
        PageRank.Page('A', []),
        PageRank.Page('B', ['A']),
        PageRank.Page('C', ['A']),
        PageRank.Page('D', ['A']),
    ]
    ranked_pages = PageRank.PageRank(pages)
    assert ranked_pages[:1] == ['A']

def test_four_hard():
    pages = [
        PageRank.Page('A', []),
        PageRank.Page('B', ['A', 'C']),
        PageRank.Page('C', ['A']),
        PageRank.Page('D', ['A', 'B', 'C']),
    ]
    ranked_pages = PageRank.PageRank(pages)
    assert ranked_pages == ['A', 'C', 'B', 'D']
