class Page:
    """Page contains name and list of outcome links"""

    def __init__(self, name, out_links):
        self.name = name
        self.out_links = out_links

class PageInTime(Page):
    """PageInTime contains all Page fields, time and number of income links at that time"""

    def __init__(self, page, time):
        self.name = page.name
        self.out_links = page.out_links
        self.time = time
        self.in_links = 0

def PageRank(pages):
    pass
