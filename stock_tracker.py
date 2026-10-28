import csv
from pathlib import Path


# These are fixed example prices in USD, not live market prices.
STOCK_PRICES = {
    "AAPL": 180,
    "TSLA": 250,
    "GOOGL": 140,
    "MSFT": 400,
    "AMZN": 185,
}


def show_portfolio(holdings):
    total = 0
    print("\nYour portfolio (USD)")
    print(f"{'Stock':<10}{'Shares':>8}{'Price':>12}{'Value':>14}")
    print("-" * 44)

    for symbol, quantity in holdings.items():
        price = STOCK_PRICES[symbol]
        value = price * quantity
        total += value
        print(f"{symbol:<10}{quantity:>8}{price:>12.2f}{value:>14.2f}")

    print("-" * 44)
    print(f"Total investment: ${total:,.2f}")
    return total


def save_portfolio(holdings, total):
    output_file = Path(__file__).resolve().parent / "portfolio.csv"

    if output_file.exists():
        answer = input("portfolio.csv already exists. Replace it? (y/n): ")
        if answer.strip().lower() != "y":
            print("Save cancelled.")
            return

    try:
        with output_file.open("w", newline="", encoding="utf-8") as file:
            writer = csv.writer(file)
            writer.writerow(["Stock", "Quantity", "Price (USD)", "Value (USD)"])
            for symbol, quantity in holdings.items():
                price = STOCK_PRICES[symbol]
                writer.writerow([symbol, quantity, f"{price:.2f}", f"{price * quantity:.2f}"])
            writer.writerow(["TOTAL", "", "", f"{total:.2f}"])
        print(f"Saved to: {output_file}")
    except OSError as error:
        print(f"Could not save the portfolio: {error}")


def main():
    holdings = {}
    print("Stock Portfolio Tracker")
    print("Prices are fixed examples in USD.")
    for symbol, price in STOCK_PRICES.items():
        print(f"  {symbol}: ${price:.2f}")
    print("\nEnter 'done' when you have finished adding stocks.")

    while True:
        symbol = input("\nStock symbol: ").strip().upper()
        if symbol == "DONE":
            break
        if symbol not in STOCK_PRICES:
            print("Please choose a stock from the list.")
            continue

        try:
            quantity = int(input("Number of shares: ").strip())
        except ValueError:
            print("Please enter a whole number.")
            continue

        if quantity <= 0:
            print("The quantity must be greater than zero.")
            continue

        holdings[symbol] = holdings.get(symbol, 0) + quantity
        print(f"Added {quantity} share(s) of {symbol}.")

    if not holdings:
        print("No stocks were added.")
        return

    total = show_portfolio(holdings)
    if input("\nSave this portfolio as CSV? (y/n): ").strip().lower() == "y":
        save_portfolio(holdings, total)


if __name__ == "__main__":
    main()
