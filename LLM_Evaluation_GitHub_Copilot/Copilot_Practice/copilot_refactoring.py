def calculate_total_price(
    unit_price: float,
    quantity: int,
    discount_percentage: float,
) -> float:
    """Calculate the price after applying a percentage discount."""
    subtotal = unit_price * quantity
    discount_amount = subtotal * discount_percentage / 100
    return subtotal - discount_amount