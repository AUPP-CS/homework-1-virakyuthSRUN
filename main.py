from currency_conversion import currency_conversion

# Print a welcome message and list of valid currencies
print("""\n\n\n\n\n\n\n
          _    _ _____  _____      _____                                         _____                          _            
     /\  | |  | |  __ \|  __ \    / ____|                                       / ____|                        | |           
    /  \ | |  | | |__) | |__) |  | |    _   _ _ __ _ __ ___ _ __   ___ _   _   | |     ___  _ ____   _____ _ __| |_ ___ _ __ 
   / /\ \| |  | |  ___/|  ___/   | |   | | | | '__| '__/ _ \ '_ \ / __| | | |  | |    / _ \| '_ \ \ / / _ \ '__| __/ _ \ '__|
  / ____ \ |__| | |    | |       | |___| |_| | |  | | |  __/ | | | (__| |_| |  | |___| (_) | | | \ V /  __/ |  | ||  __/ |   
 /_/    \_\____/|_|    |_|        \_____\__,_|_|  |_|  \___|_| |_|\___|\__, |   \_____\___/|_| |_|\_/ \___|_|   \__\___|_|   
                                                                        __/ |                                                
                                                                       |___/                                                 
      \n\n\n""")
print("🤖 Welcome to the AUPP Currency Convertion to RIEL APP 💵")
print("----------------------------------------------------------")
print("""\n📍 Instructions:
1. 💱 Enter the currency you want to convert from (USD, YAUN, BATH)
2. 💵 Enter the amount you want to convert.
3. ✨ The amount will be converted to RIEL (៛).""")
print("----------------------------------------------------------")

# Ask the user for the currency they want to convert from


while True:
    currency = input("\n👉 Enter the currency: ").upper()

    # Ask the user for the amount they want to convert
    if currency == "USD":
        amount = input("👉 Enter the amount: $")
    elif currency == "YAUN":
        amount = input("👉 Enter the amount: ¥")
    elif currency == "BATH":
        amount = input("👉 Enter the amount: ฿")
    else:
        print("😢 Invalid currency, please enter valid currency. Ex: usd, yaun, bath...")
        break

    if not amount.isnumeric():
        print("😢 Invalid amount, please enter a valid number. Example: 100, 200, 300, etc")
        break
    else:
        amount = float(amount)
        if amount < 0:
            print("😢 Amount cannot be negative!")
            break
        else:
            confirm = input(f"\n🤖 Do you want to convert {amount} {currency} to RIEL? (yes/no)\n> ")
            
            # Call the currency_conversion function with the user's currency and amount
            if confirm.lower() == "yes":
                convertedAmount = currency_conversion(currency, amount) 
                convertedAmount = "{:,}".format(convertedAmount)
            elif confirm.lower() == "no":
                print("😢 Okay, bye!")
                break
            else:
                print("😢 Invalid input!")
                break
                
            print("----------------------------------------------------------")
            print(f"\n🤖 Your total amount in RIEL is: {convertedAmount}៛ 💵!\n")
            print("----------------------------------------------------------")
            
            another = input("🤖 Do you want to convert another amount? (yes/no)\n> ")
            if another.lower() == "yes":
                continue
            elif another.lower() == "no":
                print("\n\n\n🤖 Thanks for using our app! Good bye!🫶\n\n\n")
                break
            else:
                print("😢 Invalid input!")
                break