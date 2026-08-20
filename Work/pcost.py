#!/usr/bin/env python3
#pcost.py

import sys
from report import read_portfolio
def portfolio_cost(filename):
    '''Computes the total cost (shares*price) of a portfolio file'''
    total_cost = 0.0

    records = read_portfolio(filename)

    for record in records:
        total_cost += record.cost()

    print(f'Total cost: {total_cost}')

def main(argv):
    portfolio_cost(argv[1])

if __name__ == '__main__':
    main(sys.argv)