################################################################################
#
#  Permission is hereby granted, free of charge, to any person obtaining a
#  copy of this software and associated documentation files (the "Software"),
#  to deal in the Software without restriction, including without limitation
#  the rights to use, copy, modify, merge, publish, distribute, sublicense,
#  and/or sell copies of the Software, and to permit persons to whom the
#  Software is furnished to do so, subject to the following conditions:
#
#  The above copyright notice and this permission notice shall be included in
#  all copies or substantial portions of the Software.
#
#  THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS
#  OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
#  FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
#  AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
#  LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING
#  FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER
#  DEALINGS IN THE SOFTWARE.

import json
import random
import urllib.request

# Server API URLs
QUERY = "http://localhost:8080/query?id={}"

# 500 server request
N = 500


def getDataPoint(quote):
    """ Extract the relevant values from the quote and return a tuple (stock, bid_price, ask_price, price) """
    stock = quote['stock']
    bid_price = float(quote['top_bid']['price'])
    ask_price = float(quote['top_ask']['price'])
    price = (bid_price + ask_price) / 2
    return stock, bid_price, ask_price, price



def getRatio(price_a, price_b):
    """ Get the ratio of price_a to price_b """
    if price_b == 0:
        return None
    return price_a / price_b



# Main
def main():
    quotes = [
        {'top_ask': {'price': '121.2', 'size': 36}, 'timestamp': '2019-02-11 22:06:30.572453',
         'top_bid': {'price': '120.48', 'size': 109}, 'id': '0.109974697771', 'stock': 'ABC'},
        {'top_ask': {'price': '121.68', 'size': 4}, 'timestamp': '2019-02-11 22:06:30.572453',
         'top_bid': {'price': '120.68', 'size': 81}, 'id': '0.109974697771', 'stock': 'DEF'}
    ]

    for quote in quotes:
        stock, bid_price, ask_price, price = getDataPoint(quote)
        print(f"Quoted {stock} at (bid:{bid_price}, ask:{ask_price}, price:{price})")

    prices = {quote['stock']: (float(quote['top_bid']['price']) + float(quote['top_ask']['price'])) / 2 for quote in
              quotes}
    price_a = prices['ABC']
    price_b = prices['DEF']
    ratio = getRatio(price_a, price_b)
    print(f"Ratio {ratio}")


if __name__ == "__main__":
    main()

