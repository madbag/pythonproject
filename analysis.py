# getting functionality of CSV module into the program
import csv

def read_data():
    data = []
    # # 1. Read the data from the spreadsheet
    with open('sales.csv', 'r') as sales_csv:
        # iterating rows as dictionaries.
        # Rows = values and columns = keys
        spreadsheet = csv.DictReader(sales_csv)
        # # 2. Collect all of the sales from each month into a single list
        for row in spreadsheet:
            data.append(row)
    return data
print(read_data())

# # 3. Output the total sales across all months
def run():
    data = read_data()

    sales = []
    for row in data:
        sale = int(row['sales'])
        sales.append(sale)

    total = sum(sales)
    print('Total sale:{}'.format(total))
    return total
    run()


#
# # # 5.1 Monthly changes as a percentage
# def monthly_Changes():
#     data = read_data()
#
#     sales = []
#     expenditure = []
#     for column in data:
#         sales_column = int(column['2018'])
#         sales.append(sales_column)
#
#         expenditure_column = int(column['2018'])
#         expenditure.append(expenditure_column)
#
#     result = (sales, expenditure)
#     # return (result)
#     print(result)
#     # monthly_Changes()

def calculate_monthly_changes(data):
    monthly_changes = []
    for i in range(1,13):
        sales_month = int(data['2018_{:02d}'.format(i)])
        expenditure_month = int(data['2018_{:02d}_expenditure'.format(i)])
        monthly_changes.append({'month': i, 'sales_change': sales_month, 'expenditure_change': expenditure_month})
    return monthly_changes

def calculate_percent(current, previous):
    return ((current - previous) / previous) * 100 if previous != 0 else 0

# # 4. Summary of the results
def summary():
    data = read_data()
    sales_Sum = run()
    expenditure = [int(row['expenditure']) for row in data]
    total_expenditure = sum(expenditure)
    print('Summary of the result for the year 2018: {} sales, {} expenditure'. format(sales_Sum, total_expenditure))


