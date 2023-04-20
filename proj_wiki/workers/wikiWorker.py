
import requests
import bs4

from typing import Generator

class WikiWorker():
    def __init__(self):
        self._url = "https://en.wikipedia.org/wiki/List_of_S%26P_500_companies"


    @staticmethod
    def _clean_data(resp: requests.Response) -> Generator:
        soup = bs4.BeautifulSoup(resp.text, "lxml")
        table: bs4.Tag = soup.find(id="constituents")
        table_rows: bs4.ResultSet = table.find_all("tr")
        
        # ignored the first entry as it is table header
        for row in table_rows[1:]:
            symbol:str = row.find("td").text.strip()
            yield symbol

    def extract_companies(self):
        headers={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.0.0 Safari/537.36'}
        resp = requests.get(self._url, headers=headers)
        if resp.status_code != 200:
            return ""

        yield from self._clean_data(resp)

if __name__ == "__main__":
    print("hellooooo")
    wk = WikiWorker()
    x = wk.extract_companies()
    
    print(next(x))
    print(next(x))
    print(next(x))
    print(next(x))