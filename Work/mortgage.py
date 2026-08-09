# mortgage.py
#
# Exercise 1.7
principal = 500000
rate = 0.05
payment = 2684.11
total_paid = 0.0
months = 0
extra_payment_start_month = 61
extra_payment_end_month = 108
extra_payment = 1000

while principal > 0:
    months += 1
    if extra_payment_start_month <= months <= extra_payment_end_month:
        pay = payment + extra_payment
    else:
        pay = payment

    balance = principal * (1+rate/12)

    if pay > balance:
        pay = balance

    principal = balance - pay
    total_paid += pay
    print(f'{months:5d} {total_paid:12.2f} {principal:12.2f}')
            
print(f'The total payment of the mortgage is {total_paid:0.4f} and it took {months} months')