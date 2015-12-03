class Page:
    def __init__(self, links):
        self.links = links

def PageRank(pages):
    std_rank = 1.0 / len(pages)
    ranks = {}
    for key in pages:
        ranks[key] = std_rank
    delta_max = 0.5
    eps = 0.1
    d = 0.85

    while delta_max > eps:
        delta_max = 0
        ranks_new = {}
        for key in pages:
            ranks_new[key] = std_rank

        for key_from in pages:
            for key_to in pages[key_from].links:
                ranks_new[key_to] += ranks[key_from] / len(pages[key_from].links)

        for key in pages:
            ranks_new[key] = (1 - d) / len(pages) + d * ranks_new[key]
            delta_max = max(delta_max, abs(ranks[key] - ranks_new[key]) / ranks[key])
        ranks = ranks_new

    for key in pages:
        pages[key].rank = ranks[key]

    return sorted(pages, key = lambda x: pages[x].rank  , reverse = True)

def __main__():
    pages = {}
    with open('data.txt', 'r') as file:

        n = int(file.readline())
        for i in range(n):
            line = file.readline().split()
            name = line[0][:-1]
            links = line[1:]
            pages[name] = Page(links)

    pages_ranked = PageRank(pages)
    print pages_ranked

#__main__()