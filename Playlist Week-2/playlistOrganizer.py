import pandas as pd

df = pd.read_csv('playlist.csv')
print(df)


def sortBy(df):
    column_name = input(f'Enter the name of the column you want to sort by: ').strip()
    order_of_sort = input(f'Do you want to sort ascending? Type True or False: ').strip().lower()

    if order_of_sort == 'true':
        order_of_sort = True
    elif order_of_sort == 'false':
        order_of_sort = False
    else:
        print("Invalid input for sorting order. Defaulting to ascending (True).")
        order_of_sort = True

    # Sort the DataFrame
    sorted_df = df.sort_values(by=column_name, ascending=order_of_sort)
    print(sorted_df)


i = False
while not i:
    user_input = input('Do you want to sort your playlist? Y/N: ').lower()
    if user_input == 'y':
        sortBy(df)
    elif user_input == 'n':
        i = True
    else:
        print("Invalid input. Please type 'Y' or 'N'.")
