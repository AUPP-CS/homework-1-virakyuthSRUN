# currency_conversion.py

def currency_conversion(currency, amount):
    # Check if the amount is a valid number
    if isinstance(amount, (float, int)):
        return 'invalid amount'  
    # Perform currency conversion
    if currency.upper() == 'USD':
        return amount * 4075
    elif currency.upper() == 'YUAN':
        return amount * 575
    elif currency.upper() == 'BAHT':
        return amount * 115
    else:
        return 'not found'
