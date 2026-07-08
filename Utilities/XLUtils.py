# import openpyxl

# def getRowCount(file,sheetName):
#     workbook = openpyxl.load_workbook(file)
#     sheet = workbook[sheetName]
#     return(sheet.max_row)

# def getColumnCount(file,sheetName):
#     workbook = openpyxl.load_workbook(file)
#     sheet = workbook[sheetName]
#     return(sheet.max_column)

# def readData(file,sheetName,rownum,columnno):
#     workbook = openpyxl.load_workbook(file)
#     sheet = workbook[sheetName]
#     return sheet.cell(row=rownum, column=columnno).value

# def writeData(file,sheetName,rownum,columnno,data):
#     workbook = openpyxl.load_workbook(file)
#     sheet = workbook[sheetName]
#     sheet.cell(row=rownum, column=columnno).value = data
#     workbook.save(file)


import pandas as pd

def getRowCount(file, sheetName):
    df = pd.read_excel(file, sheet_name=sheetName)
    return len(df.index)


def getColumnCount(file, sheetName):
    df = pd.read_excel(file, sheet_name=sheetName)
    return len(df.columns)


def readData(file, sheetName, rownum, columnno):
    df = pd.read_excel(sheet_name=sheetName, io=file)

    # Convert Excel-style row/column numbers to DataFrame indices
    # rownum starts from 2 because row 1 is assumed to be the header
    return df.iloc[rownum - 2, columnno - 1]


def writeData(file, sheetName, rownum, columnno, data):
    # Read all sheets
    sheets = pd.read_excel(file, sheet_name=None)

    df = sheets[sheetName]

    # Update the required cell
    df.iloc[rownum - 2, columnno - 1] = data

    # Save all sheets back to the Excel file
    with pd.ExcelWriter(file, engine='openpyxl', mode='w') as writer:
        for name, sheet_df in sheets.items():
            if name == sheetName:
                df.to_excel(writer, sheet_name=name, index=False)
            else:
                sheet_df.to_excel(writer, sheet_name=name, index=False)
