# report.py

from pathlib import Path
from collections import namedtuple
import csv

def read_portfolio(filename: Path = Path("Data/portfolio.csv")) -> list[dict]:
    """
    Reads a portfolio CSV file and converts the data into a list of stock dictionaries.

    Args:
        filename (Path): Path to the CSV file containing portfolio data.

    Returns:
        float: The total calculated cost.
    """

    # Declare the portfolio list.
    portfolio = []

    # Open portfolio and skip headers.
    with filename.open('rt') as f:
        rows = csv.reader(f)
        next(rows)

        # Iterate over portfolio rows
        for row in rows:

            # Try to add cost of all stocks in row.
            try:
                stock = {"name" : row[0], "shares": int(row[1]), "price": float(row[2])}
                portfolio.append(stock)
            except:
                raise RuntimeError("Couldn't parse row")
    
    # Return The portfolio.
    return portfolio

def read_prices(filename: Path = Path("Data/prices.csv")) -> dict:
    """
    Reads a prices CSV file and converts the data into a dict of stock name to price.

    Args:
        filename (Path): Path to the CSV file containing portfolio data.

    Returns:
        Dict[str, float]: Dictionary of stock names to their prices.
    """
    
    # Declare return var.
    prices = {}
    
    # Open portfolio and skip headers.
    with filename.open('r') as f:
        rows = csv.reader(f)

        # For each row, add name as key and price as value to the dict.
        for row in rows:

            # Try to get the stock in case line is empty.
            try: prices[row[0]] = float(row[1])
            except IndexError: pass
    return prices

TableRow = namedtuple('TableRow', ["name", "shares", "price", "change"])

def make_report(portfolio: list[dict] = read_portfolio(), prices: dict = read_prices()) -> list[TableRow]:
    """
    Makes a report about a portfolio gains and losses for each stock it has.

    Args:
        portfolio list[dict]: The portfolio.
        prices dict: Current prices of each share.

    Returns:
        list[TableRow]: List of all the shares, and relevant information about each one.
    """

    # Declare the table.
    table = []

    # Iterate over each stock and add it to the table.
    for stock in portfolio:

        # Calculate change.
        change = prices[stock['name']] - stock['price']

        # Add row to table.
        row = TableRow(name=stock['name'], shares=stock['shares'], price=prices[stock['name']], change=change)
        table.append(row)
    return table

if __name__ == "__main__":

    # Print headers.
    WIDTH = 10
    print(' '.join(f'{header:>{WIDTH}s}' for header in TableRow._fields))
    print(' '.join('-' * WIDTH for header in TableRow._fields))

    # Print
    for r in make_report():
        print(f'{r.name:>{WIDTH}s} {r.shares:>{WIDTH}d} {f"${r.price}":>{WIDTH}s} {r.change:>{WIDTH}.2f}')

