
# 2022 Fortune List
# This list displays all 18 British companies in the Fortune Global 500, which ranks the world('s '
# largest companies by annual revenue. The figures below are given in millions of US dollars and are
# for the fiscal year 2021. Also listed are the headquarters location, net profit, number of employees
# worldwide and industry sector of each company.

from bs4 import BeautifulSoup
import requests

link = 'https://en.wikipedia.org/wiki/List_of_largest_companies_in_the_United_Kingdom'

web_page = requests.get(link)
soup_extractor = BeautifulSoup(web_page.text, 'html')

print(soup_extractor)

# ### Print the column labels of the first column

First_Table = soup_extractor.find_all('table')[0]
print(First_Table)

# From the table extracted, extract the table labels
Table_Column_Labels = First_Table.find_all('th')
print(Table_Column_Labels)

Fortune_List_column_Labels = [column_Labels.text for column_Labels in Table_Column_Labels]
print(Fortune_List_column_Labels)

# Split the text from other characters

Fortune_List_column_Labels = [column_Labels.text.strip() for column_Labels in Table_Column_Labels]
print(Fortune_List_column_Labels)

# Add the labels to a pandas dataframe as column names
import pandas as pd

df = pd.DataFrame(columns=Fortune_List_column_Labels)
print(df)

# Extract the row data from the table and add to the pandas dataframe
column_row_data = First_Table.find_all('tr')

for data in column_row_data:
    table_data = data.find_all('td')
    Each_row_data = [data.text.strip() for data in table_data]

    # print individual row data
    print(Each_row_data)

# append the information in the above dataframe.
# observe that the list above has its first row to be empty
for data in column_row_data[1:]:
    table_data = data.find_all('td')
    Each_row_data = [data.text.strip() for data in table_data]
    print(Each_row_data)

# ### Now append to the dataframe
for data in column_row_data[1:]:
    table_data = data.find_all('td')
    Each_row_data = [data.text.strip() for data in table_data]

    length = len(df)
    df.loc[length] = Each_row_data

print(df)

# export to a csv file but remove the index column
# Note that the r before the path is to ensure the escape character is not read as a string to pop error.
df.to_csv(r'/Users/lambertagunbiade/Desktop/WEB SCRAPPING/Fortune_List_England_revenue.csv', index=False)

data_set = pd.read_csv('/Users/lambertagunbiade/Desktop/WEB SCRAPPING/Fortune_List_England_revenue.csv', index_col=None)
