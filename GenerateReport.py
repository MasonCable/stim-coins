# import openpyxl
# from CoinbaseClient import Client
# from argparse import ArgumentParser

# parser = ArgumentParser(description="This still needs to be written")

# parser.add_argument("-s", "--start-date", help="Start Date")
# parser.add_argument("-e", "--end-date", help="End Date")
# parser.add_argument("-g", "--granularity", help="Time Slice")
# parser.add_argument("-c", "--currency", help="Currency")
# args = parser.parse_args()
# startDate = args.start_date
# endDate = args.end_date
# timeslice = args.granularity
# productId = "{}-USD".format(args.currency)



# client = Client()
# # myWb = openpyxl.Workbook()
# # mySheet = myWb.active
# # accounts = client.accounts()
# # columnN = 1

# # for i in range(len(headers)):
# #     cell = mySheet.cell(row=1, column=columnN)
# #     cell.value = headers[i]
# #     columnN += 1
# # myWb.save('accounts.xlsx')

# # newWb = openpyxl.load_workbook('accounts.xlsx')
# # newSheet = newWb.active
# # print(newSheet)

# def store_historical_data():
#     headers = [ 'time', 'low', 'high', 'open', 'close', 'volume']
#     reportName = 'historical_data{}-{}'.format(startDate, endDate)
#     historicalData = client.get_historic_rates(productId, startDate, endDate, timeslice)
#     # Excel vars
#     workbook = openpyxl.Workbook()
#     sheet = workbook.active
#     colNum = 1
#     # Store the headers
#     for i in range(0,len(headers)):
#         cell = sheet.cell(row=1, column=colNum)
#         cell.value = headers[i]
#         colNum += 1
#     # Store the data
#     rowNum = 2
#     for item in historicalData:
#         for j in range(len(item)):
#             cell = sheet.cell(row=rowNum, column=j)
#             cell.value = item[j]

#         rowNum += 1
    
#     workbook.save('reports/{}.xlsx'.format(reportName))

# def store_ticker_data(headers, dataObj):
#     pass

# # store_historical_data()

