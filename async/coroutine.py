# BASICS OF COROUTINES
import time
def searcher():
    """
        BASIC COROUTINE
        Reads a huge file at start and then searchs for the text that is being passed
    """
    print("Started....")
    time.sleep(4)
    book = "This is some random text from a huge book"
    print("BOOK IS READ FROM INTERNET")
    while True:
        # indicates that this is not a normal function but to be treated as coroutine
        text: str = (yield)
        print(f"You have passed: {text}")


search = searcher()
search.send(None) # performs basic operations before yield keyword
search.send("ashutosh")
search.send("apurva")
search.close()
