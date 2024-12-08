def taxcal(pretax,rate):
    tax=round(pretax*rate,2)
    total=round(pretax+tax,2)
    return [pretax, tax, total]