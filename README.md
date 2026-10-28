# CodeAlpha-StockPortfolioTracker
# Stock Portfolio Tracker

A Python console program that calculates stock holdings using fixed example prices and optionally saves the results as a CSV file.

## Requirements

- Python 3 installed on your computer.
- No additional packages are needed.

Check your installation with `python --version`. If Python is missing, install it from https://www.python.org/downloads/ . On Windows, select the option to add Python to PATH during installation, then reopen your terminal.

## How to run

1. Download and extract `CodeAlpha_StockPortfolioTracker.zip`.
2. Open the extracted folder containing `stock_tracker.py`.
3. Open a terminal in that folder. On Windows, open the folder in File Explorer, type `cmd` in the address bar, and press Enter.
4. Run:

```sh
python stock_tracker.py
```

If needed, use `py stock_tracker.py` on Windows or `python3 stock_tracker.py` on macOS/Linux.

## How to use

1. Enter a stock symbol from the displayed list.
2. Enter a positive whole number of shares.
3. Repeat to add more stocks. Adding the same symbol again increases its quantity.
4. Enter `done` at the stock-symbol prompt to display your portfolio.
5. Enter `y` to save a CSV file, or another answer to skip saving.

Example inputs:

```text
Stock symbol: AAPL
Number of shares: 2
Stock symbol: TSLA
Number of shares: 1
Stock symbol: done
```

With the program's fixed sample prices, the total is **$610.00**: two AAPL shares at $180 and one TSLA share at $250.

## Output

The program displays each stock, its quantity, price, value, and the overall total. If you choose to save, `portfolio.csv` is created beside `stock_tracker.py`. Open it in Excel or a text editor. If the file already exists, the program asks before replacing it.

## Notes

- Prices are fixed examples in USD, not live market prices.
- Only the displayed stock symbols are supported.
- Quantities must be positive whole numbers.
- Entering `done` without adding stocks exits without creating a portfolio.

## Troubleshooting

- **Python is not recognized:** try `py` on Windows or `python3` on macOS/Linux, or check your Python installation.
- **Cannot open the script:** extract the ZIP first and open your terminal in the folder containing `stock_tracker.py`.
- **Cannot save the CSV:** use a writable folder and close the CSV in other applications before trying again.
