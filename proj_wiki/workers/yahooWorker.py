import threading
import requests

from multiprocessing import Queue
from typing import List
from lxml import html


class YahooScheduler(threading.Thread):

    def __init__(self, queue: Queue, output_queues: List[Queue], **kwargs):
        self._queue = queue
        self._output_queues = output_queues
        super(YahooScheduler, self).__init__(**kwargs)
        self.start()

    def run(self):
        while True:
            symbol = self._queue.get()
            if symbol == "DONE":
                break

            price: float = YahooWorker(symbol=symbol).get_price()
            output_vaues = [symbol, price]
            print(f"GENERATED VALUES: {output_vaues}")
            for queue in self._output_queues:
                queue.put(output_vaues)

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
