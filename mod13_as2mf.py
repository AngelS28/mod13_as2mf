import datetime 

def get_symbol():
    while True:
        symbol = input("Enter the symbol for stock visualizer: ")
        if symbol.isalpha() and symbol.isupper() and (1 <= len(symbol) <= 7):
            return symbol
        else:
            print("Symbol must be capitalized and consist of 1-7 alpha characters.")

def get_chart_type():
    while True:
        chart_type = input("Enter the chart type for stock visualizer (1 or 2): ")
        if chart_type in ['1', '2']:
            return chart_type
        else:
            print("Chart type must be 1 or 2.")

def get_time_series():
    while True:
        time_series = input("Enter the time series for stock visualizer (1-4): ")
        try:
            time_series = int(time_series)
            if 1 <= time_series <= 4:
                return time_series
            else:
                print("Time series must be between 1 and 4.")
        except ValueError:
            print("Please enter a valid integer for time series.")

def get_date(prompt):
    while True:
        date = input(prompt)
        try:
            datetime.datetime.strptime(date, '%Y-%m-%d')
            return date
        except ValueError:
            print("Date must be in the format YYYY-MM-DD.")

def main():
    try:
        symbol = get_symbol()
        chart_type = get_chart_type()
        time_series = get_time_series()
        start_date = get_date("Enter the start date for stock visualizer (YYYY-MM-DD): ")
        end_date = get_date("Enter the end date for stock visualizer (YYYY-MM-DD): ")

        print("Input is valid.")
    except KeyboardInterrupt:
        print("\nProgram terminated by user.")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()
