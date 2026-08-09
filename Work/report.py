# report.py
#
# Exercise 2.4
import csv
import sys

# def read_portfolio(filename):
#     '''Computes the total cost (shares*price) of a portfolio file'''
#     portfolio = []
#     with open(filename, 'rt') as f:
#         rows = csv.reader(f)
#         next(rows)
#         for row in rows:
#             try:
#                 holding = (row[0],int(row[1]),float(row[2]))
#                 portfolio.append(holding)
#             except ValueError:
#                 print('Could not convert string to float!', row) 
#     return portfolio

def read_portfolio(filename):
    '''Creates a list of dictionaries'''
    portfolio = []
    with open(filename, 'rt') as f:
        rows = csv.reader(f)
        next(rows)
        for row in rows:
            try:
                holding = {'name':row[0],'shares':int(row[1]),'price':float(row[2])}
                portfolio.append(holding)
            except ValueError:
                print('Could not convert string to float!', row) 
    return portfolio

if len(sys.argv) == 2:
    filename = sys.argv[1]
else:
    filename = 'Data/portfolio.csv'

result = read_portfolio(filename)
print(f'Result: {result}')

def read_prices(filename):
    prices = {}
    with open(filename, 'r') as file:
        rows = csv.reader(file)
        for row in rows:
            if len(row) == 0:
                pass
            else:
                prices[row[0]] = float(row[1])
    return prices

if len(sys.argv) == 2:
    filename = sys.argv[1]
else:
    filename = 'Data/prices.csv'

dict_result = read_prices(filename)
print(dict_result)

def calculate_gain_loss(stock_list,price_dict):
    old_price = 0.0
    current_price = 0.0

    for stock in stock_list:
        old_price += stock['shares'] * stock['price']
        current_price += price_dict[stock['name']] * stock['shares']

    return f'Current value of portfolio: {current_price} and the current {"gain" if (current_price - old_price) > 0 else "loss"} is: {current_price - old_price:0.2f}'