import csv

def read_data():
    data = []
    with open('sales.csv', 'r') as sales_csv:
        spreadsheet = csv.DictReader(sales_csv)
        for row in spreadsheet:
            data.append(row)
    return data

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

# # 5.1 Monthly changes as a percentage
def calculate_percentage_change(old_value, new_value):
    if old_value == 0:
        return 0
    percentage_change = ((new_value - old_value) / abs(old_value)) * 100
    return percentage_change

def find_highest_lowest(data, column):
    values = [int(row[column]) for row in data]
    return min(values), max(values)

def run_data():
    data = read_data()
    min_sales, max_sales = find_highest_lowest(data, 'sales')
    min_expenditure, max_expenditure = find_highest_lowest(data, 'expenditure')

    print('Lowest Sales: {}'.format(min_sales))
    print('Highest Sales: {}'.format(max_sales))
    print('Lowest Expenditure: {}'.format(min_expenditure))
    print('Highest Expenditure: {}'.format(max_expenditure))

run_data()

