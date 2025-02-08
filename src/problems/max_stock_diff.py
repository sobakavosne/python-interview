def max_price_difference(prices: list[int]) -> float:

    min_price: float = float('inf')
    print(min_price)
    max_diff: float = 0
    
    for price in prices:
        print(min_price)
        max_diff = max(max_diff, price - min_price)
        min_price = min(min_price, price)
    
    return max_diff

prices = [12, 7, 5, 8, 11, 9, 10, 6]

result = max_price_difference(prices)

print(f"Max difference: {result}")

assert result == 6, f"Expected 6 but got {result}"
