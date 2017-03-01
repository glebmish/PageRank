from collections import defaultdict
import functools


class Page:
    def __init__(self, name, links):
        self.name = name
        self.links = links


def page_rank(pages, eps=0.1, d=0.85):
    std_rank = 1.0 / len(pages)
    ranks = defaultdict(lambda: std_rank)
    delta_max = eps + 0.1

    while delta_max > eps:
        delta_max = 0
        ranks_new = defaultdict(lambda: std_rank)

        for key_from in pages:
            for key_to in pages[key_from].links:
                ranks_new[key_to] += ranks[key_from] / len(pages[key_from].links)
            # ranks_new = defaultdict(
            #    zip(pages[key_from].links, map(lambda key_to: ranks_new[key_to] + ranks[key_from] / len(pages[key_from].list),
            #                                   pages[key_from].links)))

        # ranks_new = map(lambda key: ranks_new[key] = (1 - d) / len(pages) + d * ranks_new[key], ranks_new)
        for key in pages:
            ranks_new[key] = (1 - d) / len(pages) + d * ranks_new[key]
            delta_max = max(delta_max, abs(ranks[key] - ranks_new[key]) / ranks[key])
        ranks = ranks_new

    for key in pages:
        pages[key].rank = ranks[key]

    def compare(p1, p2):
        a = pages[p2].rank, pages[p1].name
        b = pages[p1].rank, pages[p2].name
        return (a>b)-(a<b)

    return sorted(pages, key=functools.cmp_to_key(compare))


def __main__():
    pages = {}
    with open('data.txt', 'r') as file:
        n = int(file.readline())
        for i in range(n):
            line = file.readline().split()
            name = line[0][:-1]
            links = line[1:]
            pages[name] = Page(name, links)

    pages_ranked = page_rank(pages)
    print(pages_ranked)

# __main__()