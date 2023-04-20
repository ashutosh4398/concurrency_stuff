import threading
import requests

from multiprocessing import Queue
from lxml import html


class YahooScheduler(threading.Thread):

    def __init__(self, queue: Queue, **kwargs):
        self._queue = queue
        super(YahooScheduler, self).__init__(**kwargs)
        self.start()

    def run(self):
        while True:
            symbol = self._queue.get()
            if symbol == "DONE":
                break

            price: float = YahooWorker(symbol=symbol).get_price()
            print(price)

class YahooWorker:
    
    BASE_URL = "https://finance.yahoo.com/quote"
    
    def __init__(self, symbol: str) -> None:
        self._symbol = symbol
        self._url = f"{self.BASE_URL}/{symbol.strip()}"

    def get_price(self) -> float:
        resp: requests.Response = requests.get(self._url)
        dom = html.fromstring(resp.text)
        try:
            raw_price:str = dom.xpath('//*[@id="quote-header-info"]/div[3]/div[1]/div/fin-streamer[1]')[0].text
        except IndexError:
            return None
        price:str = raw_price.replace(",", "")
        return float(price)
        

if __name__ == "__main__":
    yw = YahooWorker(symbol="MMM")
    print(yw.get_price())
