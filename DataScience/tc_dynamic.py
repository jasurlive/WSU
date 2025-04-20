def tc(subtotal, taxrate):
    tax = round(subtotal * taxrate, 2)  # Calculate tax (6%)
    total = round(subtotal + tax, 2)  # Calculate total
    return [subtotal, tax, total]  # Return the values as a list
