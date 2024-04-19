import datetime 

def get_symbol(symbol):
    if not symbol.isalpha() or not symbol.isupper() or not (1 <= len(symbol) <= 7):
        return False
    else:
        return True 
    
def get_chart_type(chart_type):
    if chart_type not in ['1', '2']:
        return False 
    else:
        return True
    
def get_time_series(time_series):
    try:
        time_series = int(time_series)
        if not (1 <= time_series <= 4):
            return False
        else:
            return True
    except ValueError:
        return False

def get_date(date):
    try:
        datetime.datetime.strptime(date, '%Y-%m-%d')
    except ValueError:
        return False
    
    return True

def main():
    symbol = input("Enter the symbol for stock visualizer: ")
    chart_type = input("Enter the chart type for stock visualizer: ")
    time_series = input("Enter the time series for stock visualizer: ")
    start_date = input("Enter the start date for stock visualizer: ")
    end_date = input("Enter the end date for stock visualizer: ")

    errors = []

    if not get_symbol(symbol):
        errors.append("Symbol must be capitalized and consist of 1-7 alpha characters.")

    if not get_chart_type(chart_type):
        errors.append("Chart type must be 1 or 2.")
    
    if not get_time_series(time_series):
        errors.append("Time series must be between 1 and 4.")
    
    if not get_date(start_date):
        errors.append("Start date must be in the format YYYY-MM-DD.")

    if not get_date(end_date):
        errors.append("End date must be in the format YYYY-MM-DD.")

    if errors:
        print("Input errors:")
        for error in errors:
            print("- ", error)

    else:
        print("Input is valid.")

if __name__ == "__main__":
    main()
