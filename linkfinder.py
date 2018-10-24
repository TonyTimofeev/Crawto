from html.parser import HTMLParser
from requests.compat import urljoin


class LinkFinder(HTMLParser):

    def __init__(self, base_url, page_url):
        super().__init__()
        self.base_url = base_url
        self.page_url = page_url
        self.links = set()

    def handle_starttag(self, tag, attrs):
        if tag == 'a':
            for (attribute, value) in attrs:
                if attribute == 'href':
                    if (len(value) > 0) and (value[0] != ' '):
                        url = urljoin(self.base_url, value)
                        self.links.add(url)

    def get_links(self):
        return self.links