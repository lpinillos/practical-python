#!/usr/bin/env python3
#report.py

from fileparse import parse_csv
import sys
import stock

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
    
    for stock in stock_list:
        old_price += stock.shares * stock.price
        current_price += price_dict[stock.name] * stock.shares

    return f'Current value of portfolio: {current_price} and the current {"gain" if (current_price - old_price) > 0 else "loss"} is: {current_price - old_price:0.2f}'

def make_report(stock_list, price_dict):
    '''Creates a structured report of the data'''
    report = []
    for stock in stock_list:
        change = price_dict[stock.name] - stock.price
        new_tuple = (stock.name,stock.shares,price_dict[stock.name],change)
        report.append(new_tuple)

    return report

def print_report(final_report):
    '''Prints a well structured report'''
    headers = ('Name', 'Shares', 'Price', 'Change')
    print(f'{headers[0]:>10s} {headers[1]:>10s} {headers[2]:>10s} {headers[3]:>10s}')
    print('---------- ---------- ---------- ----------')
    for name, shares, price, change in final_report:
        price = '$' + str(round(price,2))
        print(f'{name:>10s} {shares:>10d} {price:>10s} {change:>10.2f}')

def portfolio_report(filename_port, filename_price):
    '''Main function that calls all the other nested functions'''
    final_report = make_report(read_portfolio(filename_port),read_prices(filename_price))
    print_report(final_report)

def main(argv):
    if len(argv) != 3:
            raise SystemExit('Usage: %s portfile pricefile' % argv[0])
    portfolio_report(argv[1], argv[2])

if __name__ == '__main__':
    main(sys.argv)