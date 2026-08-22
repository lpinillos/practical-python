#!/usr/bin/env python3
#report.py

from fileparse import parse_csv
import sys
import stock
import tableformat

def read_portfolio(filename):
    '''Creates a list of dictionaries reading a portfolio.csv'''
    with open(filename,'rt') as file:
        portdicts = parse_csv(file, select=['name','shares','price'], types=[str,int,float])
    portfolio = [ stock.Stock(d['name'], d['shares'], d['price']) for d in portdicts]
    return portfolio

def read_prices(filename):
    '''Help reading the updated prices in a csv'''
    with open(filename,'rt') as file:
        prices = dict(parse_csv(file, types=[str,float], has_headers=False))
    return prices

def calculate_gain_loss(stock_list,price_dict):
    '''Calculates if there is a gain or loss in the portfolio of a person'''
    old_price = 0.0
    current_price = 0.0
    
    for s in stock_list:
        old_price += s.shares * s.price
        current_price += price_dict[s.name] * s.shares

    return f'Current value of portfolio: {current_price} and the current {"gain" if (current_price - old_price) > 0 else "loss"} is: {current_price - old_price:0.2f}'

def make_report(stock_list, price_dict):
    '''Creates a structured report of the data'''
    report = []
    for s in stock_list:
        change = price_dict[s.name] - s.price
        new_tuple = (s.name,s.shares,price_dict[s.name],change)
        report.append(new_tuple)

    return report

def print_report(final_report, formatter):
    '''Print a nicely formatted table from a list of (name, shares, price, change) tuples.'''
    formatter.headings(['Name', 'Shares', 'Price', 'Change'])
    for name, shares, price, change in final_report:
        rowdata = [name, str(shares), f'{price:0.2f}',f'{change:0.2f}']
        formatter.row(rowdata)

def portfolio_report(portfoliofile, pricefile, fmt='txt'):
    '''Main function that calls all the other nested functions'''
    portfolio = read_portfolio(portfoliofile)
    price = read_prices(pricefile)

    report = make_report(portfolio,price)

    formatter = tableformat.create_formatter(fmt)
    print_report(report, formatter)

def main(argv):
    if len(argv) > 4:
            raise SystemExit('Usage: %s portfile pricefile fmt' % argv[0])
    portfolio_report(argv[1], argv[2], argv[3])

if __name__ == '__main__':
    main(sys.argv)