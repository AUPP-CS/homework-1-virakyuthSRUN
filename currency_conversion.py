# currency_conversion.py

def currency_conversion(currency, amount):
    """
    Converts the given amount from the specified currency to RIEL.

    Parameters:
    - currency (str): The currency code (USD, YUAN, BAHT).
    - amount (float or int): The amount to be converted.

    Returns:
    - float or str: The converted amount in RIEL or an error message.
    """
    # Check if the amount is a valid number
    if not isinstance(amount, (float, int)):
        return 'Invalid Amount'
    
    # Perform currency conversion
    if currency.upper() == 'USD':
        return amount * 4075
    elif currency.upper() == 'YUAN':
        return amount * 575
    elif currency.upper() == 'BAHT':
        return amount * 115
    else:
        return "Not Found"
