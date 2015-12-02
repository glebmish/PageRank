class Page:
    """Page contains name and list of outcome links"""

    def __init__(self, links, rank):
        self.links = links
        self.rank = rank

def PageRank(pages):
    delta_max = 0.5
    while delta_max > 0.1:
        delta_max = 0
        pages_new = {}
        for i in pages:
            pages_new[i] = Page(pages[i].links, 0)

        for i in pages:
            for j in pages[i].links:
                pages_new[j].rank += pages[i].rank / len(pages[j].links)

        for i in pages:
            delta_max = max(delta_max, pages_new[i].rank / pages[i].rank)
        pages = pages_new

    return sorted(pages, key=lambda x: pages[x].rank)

pages = {}
file = open('data.txt', 'r')

n = int(file.readline())
for i in range(n):
    line = file.readline().split()
    name = line[0][:-1]
    links = line[1:]
    pages[name] = Page(links, 1/n)

pages_ranked = PageRank(pages)
print pages_ranked