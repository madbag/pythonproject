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

# # 4. Summary of the results
def summary():
    data = read_data()

    sales_Sum = run()
    expenditure = []
    for row in data:
        exp = int(row['expenditure'])
        expenditure.append(exp)

    total = sum(expenditure)
    print('Summary of the result for the year 2018: {} sales, {} expenditure'. format(sales_Sum, total))
summary()

