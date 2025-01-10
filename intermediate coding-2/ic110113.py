def best_time_to_sell(prices):
    if len(prices) < 2:
        return None  # We need at least two days to make a transaction

    min_price = float('inf')
    max_profit = 0
    buy_day = 0
    sell_day = 0

    for i in range(len(prices)):
        if prices[i] < min_price:
            min_price = prices[i]
            buy_day = i
        # Check the profit if selling on the current day
        profit = prices[i] - min_price
        if profit > max_profit:
            max_profit = profit
            sell_day = i

    return (buy_day, sell_day)

# Example usage
prices = [7, 1, 5, 3, 6, 4]
buy_day, sell_day = best_time_to_sell(prices)
print(f"Buy on day {buy_day + 1}, Sell on day {sell_day + 1}")  # Days are 1-indexed
