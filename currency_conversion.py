def currency_conversion(currency, amount):
    # Add your code here
    if not isinstance(amount, (float, int)):
        return 'Invalid Amount'
    
    if currency == 'USD':
        return amount * 4075
    elif currency == 'YAUN':
        return amount * 575
    elif currency == 'BATH':
        return amount * 115
    else:
        print(f"Unsupported currency: {currency}")
        return "Not Found"
    # Reminders: 
    # - currency is a string that tells us what currency to change to. It can be 'usd', 'yuan', or 'baht'.
    # - amount is a number that tells us how much money to change into riel.
    
    # 1. add a check to ensure that 'amount' is a number.
    # 2. convert the 'amount' to the right 'currency'.
