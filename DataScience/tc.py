
def tc(subtotal): 
    tax = round(subtotal * 0.06, 2)  # Calculate tax (6%)
    total = round(subtotal + tax, 2) # Calculate total
    return [subtotal, tax, total]    # Return the values as a list
