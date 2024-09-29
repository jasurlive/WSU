def tc(subtotal):
    tax=round(subtotal*0.06,2)
    total=round(subtotal+tax,2)
    return [subtotal, tax, total]