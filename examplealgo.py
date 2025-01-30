from datamodel import *

class Trader:
    last_price = 0
    def run(self, state):
        orders = []
        for product in state.products:
            listings = Listing(state.orderbook[product], product)

            highest_bid = list(listings.buy_orders.keys())[0]
            bid_quantities = list(listings.buy_orders.values())

            lowest_ask = list(listings.sell_orders.keys())[0]
            ask_quantities = list(listings.sell_orders.values())


            orders.append(Order(product, lowest_ask, 5)) #Buying
            orders.append(Order(product, highest_bid, -5)) #Selling
        return orders
