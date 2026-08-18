import csv
import sys

def read_portfolio(filename):
    '''Creates a list of dictionaries reading a portfolio.csv'''
    portfolio = []
    with open(filename, 'rt') as f:
        rows = csv.reader(f)
        headers = next(rows)
        for n, row in enumerate(rows,start=1):
            try:
                record = dict(zip(headers,row))
                record['shares'] = int(record['shares'])
                record['price'] = float(record['price'])
                portfolio.append(record)
            except ValueError:
                print('Could not convert string to float!', row) 
    return portfolio

def read_prices(filename):
    '''Help reading the updated prices in a csv'''
    prices = {}
    with open(filename, 'r') as file:
        rows = csv.reader(file)
        for row in rows:
            if len(row) == 0:
                pass
            else:
                prices[row[0]] = float(row[1])
    return prices

def calculate_gain_loss(stock_list,price_dict):
    '''Calculates if there is a gain or loss in the portfolio of a person'''
    old_price = 0.0
    current_price = 0.0
    
    for stock in stock_list:
        old_price += stock['shares'] * stock['price']
        current_price += price_dict[stock['name']] * stock['shares']

    return f'Current value of portfolio: {current_price} and the current {"gain" if (current_price - old_price) > 0 else "loss"} is: {current_price - old_price:0.2f}'

def make_report(stock_list, price_dict):
    '''Creates a structured report of the data'''
    report = []

    for stock in stock_list:
        change = price_dict[stock['name']] - stock['price']
        new_tuple = (stock['name'],stock['shares'],price_dict[stock['name']],change)
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

portfolio_report('Data/portfolio.csv', 'Data/prices.csv')

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

# if len(sys.argv) == 2:
#     filename_port = sys.argv[1]
# else:
#     filename_port = 'Data/portfolio.csv'

# result = read_portfolio(filename_port)

# if len(sys.argv) == 2:
#     filename_price = sys.argv[1]
# else:
#     filename_price = 'Data/prices.csv'

# dict_result = read_prices(filename_price)