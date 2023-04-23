import time
import random
from threading import Lock

from customers_list import customers
from shop import Shop
from customer import Customer
from barber import Barber


def main():
    lock = Lock()

    shop = Shop(lock=lock)
    # as soon as all the customers are resolved, clear the barber thread
    barber = Barber(shop.waiting_queue, lock=shop.lock, daemon=True)

    customer_threads = []
    for customer in customers:
        cus = Customer(**customer)
        # here we will decide whether to consume a customer or move him/her to
        # other queue for round robin approach
        cus.visit(shop)
        customer_threads.append(cus)
        time.sleep(random.randint(4, 6))


    for cus in customer_threads:
        cus.join()

    # barber.join()


if __name__ == "__main__":
    main()

    