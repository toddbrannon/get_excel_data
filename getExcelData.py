import pandas as pd

#variables for source file, worksheets, and empty array for dataframes
spreadsheet_file = pd.ExcelFile('[filepath + filename]')
worksheets = spreadsheet_file.sheet_names
appended_data = []
 
for sheet_name in worksheets:
   #column header name
   month = 'August'
   #read all worksheets in source file
   df = pd.read_excel(spreadsheet_file, sheet_name, header=2)
   #limit columns and filter on values in month column
   df = df[['Store ID', month]].where(df[month]>3000)
   #remove 'NaN' values from dataframe
   df = df.dropna()
   #add column equal to sheet tab name
   df['Product ID'] = sheet_name
   #add product column and set column order
   df = df[['Product ID', 'Store ID', month]]
   #append each dataframe from worksheets to appended_data
   appended_data.append(df)
 
#join the elements (dataframes) of the appended_data array to create a single dataframe
appended_data = pd.concat(appended_data)
#export appended_data to new excel file, remove the index column, and save the file
appended_data.to_excel('[filepath + . filename]', index=False)
