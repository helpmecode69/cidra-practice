def apply_discount(price, percent):
    """The price after a discount of `percent` percent, never below zero."""
    return max(price - price * percent / 100, 0)
