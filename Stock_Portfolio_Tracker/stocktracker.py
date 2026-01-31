stock_prices = {
    "AAPL": 180,
    "TSLA": 250,
    "GOOGL": 140,
    "MSFT": 320,
    "AMZN": 130
}

portfolio = {}
total_investment = 0

def show_menu():
    print("\n=== Stock Portfolio Tracker ===")
    print("1. Add Stock")
    print("2. View Portfolio")
    print("3. Save Portfolio")
    print("4. Exit")

def add_stock():
    global total_investment
    symbol = input("Enter stock symbol: ").upper()

    if symbol not in stock_prices:
        print("Stock not available")
        return

    quantity = input("Enter quantity: ")

    if not quantity.isdigit():
        print("Quantity must be a number")
        return

    quantity = int(quantity)
    price = stock_prices[symbol]
    value = price * quantity

    if symbol in portfolio:
        portfolio[symbol]["quantity"] += quantity
        portfolio[symbol]["value"] += value
    else:
        portfolio[symbol] = {
            "price": price,
            "quantity": quantity,
            "value": value
        }

    total_investment += value
    print("Stock added successfully")

def view_portfolio():
    if not portfolio:
        print("Portfolio is empty")
        return

    print("\n--- Portfolio Summary ---")
    for stock, data in portfolio.items():
        print(stock,
              "| Price:", data["price"],
              "| Quantity:", data["quantity"],
              "| Value:", data["value"])
    print("Total Investment:", total_investment)

def save_portfolio():
    file = open("portfolio.csv", "w")
    file.write("Stock,Price,Quantity,Value\n")

    for stock, data in portfolio.items():
        line = stock + "," + str(data["price"]) + "," + str(data["quantity"]) + "," + str(data["value"])
        file.write(line + "\n")

    file.write("Total,,, " + str(total_investment))
    file.close()

    print("Portfolio saved to portfolio.csv")

while True:
    show_menu()
    choice = input("Enter your choice: ")

    if choice == "1":
        add_stock()
    elif choice == "2":
        view_portfolio()
    elif choice == "3":
        save_portfolio()
    elif choice == "4":
        print("Exiting program")
        break
    else:
        print("Invalid choice")
