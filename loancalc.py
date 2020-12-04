import math

cal = input("""What do you want to calculate?
type "n" for number of monthly payments,
type "a" for annuity monthly payment amount,
type "p" for loan principal:""")
if cal == 'n':
    principal = float(input("Enter the loan principal:\n"))
    monthly = float(input("Enter the monthly payment:\n"))
    interest = float(input("Enter the loan interest:\n")) / 100
    i = interest / 12 * 1
    n = math.ceil(math.log(float(monthly) / (float(monthly) - i * float(principal)), i + 1))
    years, months = (n // 12, n % 12)

    if years == 0:
        if months == 1:
            print(f'It will take {months} month')
        else:
            print(f'It will take {months} months to repay this loan!')

    elif months == 0:
        if years == 1:
            print(f'It will take {years} year to repay this loan!')
        else:
            print(f'It will take {years} years to repay this loan!')
    else:
        print(f'It will take {years} years and {months} months to repay this loan!')
elif cal == 'a':
    principal = float(input("Enter the loan principal:\n"))
    periods = float(input("Enter the number of periods:\n"))
    interest = float(input("Enter the loan interest:\n")) / 100
    i = interest / 12 * 1
    payment = math.ceil(principal * ((i * math.pow(1 + i, periods)) / (math.pow(1 + i, periods) - 1)))
    print(f'Your monthly payment = {payment}!')
elif cal == 'p':
    annuity = float(input("Enter the annuity payment:\n"))
    periods = float(input("Enter the number of periods:\n"))
    interest = float(input("Enter the loan interest:\n"))
    i = interest / 12 / 100
    principal = round(annuity / ((i * math.pow(1 + i, periods)) / (math.pow(1 + i, periods) - 1)))
    print(f'Your loan principal = {principal}!')

