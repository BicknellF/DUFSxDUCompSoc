# Durham University Finance Society trading simulator

This project aims to aid the education of DUFS Quant Fund members in financial markets by providing users an OOP environment to create strategies and test them on artificial market data.

### Getting Started:
Algorithms should be created in `examplealgo.py`, these can then be backtested by running `main.py`. Data analysis is recommended in a Jupyter Notebook before implementing an algorithm, you should think about ways in which options theory could be applied. Algorithms can send orders on every timestamp. However, imagine there is a finite period between timestamps in which bots on the exchange submit orders. This could mean that if your order is added to the order book, having not matched with an existing order, it may still be filled by a bot before the next timestamp. With each new timestamp, all outstanding orders are cancelled.

### Products:
This simulation allows users to trade three products; `Call`, `Put`, and `Underlying`. 
- `Underlying`: This represents a stock or commodity.
- `Call`: This represents a European call option on `Underlying` with a strike price of `1000` in 365 days.
- `Put`: This represents a European put option on `Underlying` with a strike price of `1000` in 365 days.

This simulation's timescale can be considered negligible relative to expiry with all timesteps within the same day.

### Accessing Market Data:
Each product has an order book, this will change every timestep. To access the order book for `Underlying`, the code would be as follows
```
state.orderbook[product] # dict of buy order book dict and sell order book dict
state.orderbook[product]["BUY"] # dict of buy orders in the form {price: quantity}
state.orderbook[product]["SELL"] # dict of sell orders in the form {price: quantity}
```

You can also access your current position in a given product using
```
state.positions[product]
```

### Sending orders:
On each timestep, `Trader.run()` returns a list of orders. Each order in this list is an object of the class `Order`. The `Order` class requires a product, price, and quantity in the form `Order(product, price, quantity)`. Orders are "bids" (buying) when the quantity is positive, or "asks" (selling) when the quantity is negative. e.g to place an order to buy 1 unit of a call option at price 10, you should create an Order using `Order("Call", 10, 1)`.

