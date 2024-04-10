import pandas as pd
from openpyxl.styles import Font

# Assuming df is your DataFrame containing the data

# Replace 'pivot_table.xlsx' with the path where you want to save the Excel file
excel_file = 'pivot_table.xlsx'

# Write the DataFrame to an Excel file with custom styling
with pd.ExcelWriter(excel_file, engine='openpyxl') as writer:
    df.to_excel(writer, index=False, sheet_name='Sheet1')

    # Access the workbook and worksheet objects
    workbook = writer.book
    worksheet = writer.sheets['Sheet1']

    # Define the font for unbolding
    font_unbold = Font(bold=False)

    # Set the font for columns A, B, and C to unbold
    for column in ['A', 'B', 'C']:
        for cell in worksheet[column]:
            cell.font = font_unbold

# Now, your data will be written to the Excel file with the specified style
