# report.py

from pcost import get_portfolio_cost
from pathlib import Path
from collections import namedtuple
import csv

Stock = namedtuple("Stock", ["name", "shares", "price"])

def read_portfolio(filename: Path) -> list[Stock]:
    """
    Reads a portfolio CSV file and converts the data into a Stock namedtuple list.

    Args:
        filename (Path): Path to the CSV file containing portfolio data.

    Returns:
        float: The total calculated cost.
    """

    # Declare the portflio list.
    portfolio = []

    # Open protfolio and skip headers.
    with filename.open('rt') as f:
        rows = csv.reader(f)
        next(rows)

        # Iterate over potofolio rows
        for row in rows:

            # Try to add cost of all stocks in row.
            try:
                stock = Stock(row[0], int(row[1]), float(row[2]))
                portfolio.append(stock)
            except:
                raise RuntimeError('Couldn\'nt parse row')
    
    # Return The portfolio.
    return portfolio