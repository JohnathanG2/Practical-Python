# report.py

from pcost import get_portfolio_cost
from pathlib import Path

print(get_portfolio_cost(Path("Data/portfolio.csv")))