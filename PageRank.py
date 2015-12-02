def PageRank(pages):
    std_rank = 1.0 / len(pages)
    ranks = {}
    for i in pages:
        ranks[i] = std_rank
    delta_max = 0.5

    while delta_max > 0.1:
        delta_max = 0
        ranks_new = {}
        for i in pages:
            ranks_new[i] = std_rank

        for i in pages:
            for j in pages[i]:
                ranks_new[j] += ranks[i] / len(pages[i])

        for i in pages:
            delta_max = max(delta_max, abs(ranks[i] - ranks_new[i]) / ranks[i])
        ranks = ranks_new

    return sorted(ranks, key = lambda x: ranks[x], reverse = True)

def __main__():
    pages = {}
    with open('data.txt', 'r') as file:

        n = int(file.readline())
        for i in range(n):
            line = file.readline().split()
            name = line[0][:-1]
            links = line[1:]
            pages[name] = links

    pages_ranked = PageRank(pages)
    print pages_ranked

#__main__()