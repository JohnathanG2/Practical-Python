# pcost.py
from pathlib import Path
import csv
import argparse

def get_portfolio_cost(filename: Path) -> float:
    """Gets a path to an csv file of a portfolio, and returns total cost of all of the stocks."""

    # Save total cost.
    total_cost = 0.0

    # Open protfolio and skip headers.
    with filename.open('rt') as f:
        rows = csv.reader(f)
        next(rows)

        # Iterate over potofolio
        for row in rows:

            # Try to add cost of all stocks in row.
            try:
                total_cost += int(row[1]) * float(row[2])
            except:
                raise RuntimeError('Couldn\'nt parse row')
    
    # Return cost.
    return total_cost

def main():
    parser = argparse.ArgumentParser(description="Calculate the total cost of a portfolio file.")
    parser.add_argument("filename", type=Path, help="Path to the input CSV file")
    args = parser.parse_args()
    print(get_portfolio_cost(filename=args.filename))

if __name__ == "__main__":
    main()