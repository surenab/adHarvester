import requests
from souppage import SoupPage, Selector


class Harvester:
    _selectors: dict = {}
    _rules: dict = {}

    def __init__(self, rules: dict = None):
        self._rules = rules

    def init_rules(self):
        for key in self._rules.keys():
            self._selectors[key] = Selector(self._rules[key].get('name'),
                                            self._rules[key].get('selector_type'),
                                            attr=self._rules[key].get('attr'),
                                            required_attr=self._rules[key].get('required_attr'))

    @property
    def get_selectors(self):
        return self._selectors

    @property
    def get_rules(self):
        return self._rules

    def set_rules(self, rules):
        self._rules = rules

    def scrap_from_html(self, html):
        soup_page = SoupPage(html)
        data = {}
        for key in self._selectors.keys():
            data[key] = soup_page.select(self._selectors.get(key))
        return data

    def scrap_from_url(self, url):
        response = requests.get(url)
        return self.scrap_from_html(response.text)

