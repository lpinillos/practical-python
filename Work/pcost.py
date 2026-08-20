# pcost.py
#
# Exercise 1.27
import csv
import sys
from report import read_portfolio
def portfolio_cost(filename):
    '''Computes the total cost (shares*price) of a portfolio file'''
    total_cost = 0.0

    records = read_portfolio(filename)

    for record in records:
        nshares = int(record['shares'])
        price = float(record['price'])
        total_cost += nshares * price

    return total_cost

if len(sys.argv) == 2:
    filename = sys.argv[1]
else:
    filename = 'Data/portfolio.csv'

cost = portfolio_cost(filename)
print(f'Total cost: {cost}')