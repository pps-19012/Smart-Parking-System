# import random  # for random generation of parking data
# import requests
# from flask import Blueprint, render_template, request, jsonify


# from googleapiclient.discovery import build

# from google.oauth2 import service_account

# SERVICE_ACCOUNT_FILE = 'keys.json'
# SCOPES = ['https://www.googleapis.com/auth/spreadsheets']

# creds = None
# # global_entry_data = "0"
# # global_exit_data = "0"
# # curr_parking_data = ["0", "0", "0", "0", "0"]
# # time_remaining = [-1, -1, -1, -1, -1]
# time = [0, 0, 0, 0, 0]

# creds = service_account.Credentials.from_service_account_file(
#     SERVICE_ACCOUNT_FILE, scopes=SCOPES)

# # The ID and range of a sample spreadsheet.
# SAMPLE_SPREADSHEET_ID = '138K6l-Z_gsva38rQHpHxcx8Z5zo9CbQ_Hrwm8WrbDco'
# SAMPLE_RANGE_NAME1 = 'Sheet1!A1'
# SAMPLE_RANGE_NAME2 = 'Sheet1!A2'
# SAMPLE_RANGE_NAME3 = 'Sheet1!A3'
# SAMPLE_RANGE_NAME4 = 'Sheet1!A4'


# views = Blueprint('views', __name__)

# button_color = ['#dc3545', '#28a745', '#dc3545',
#                 '#dc3545', '#28a745']  # initial button colors

# service = build('sheets', 'v4', credentials=creds)

# # Call the Sheets API
# sheet = service.spreadsheets()

# # parking = ["0", "0", "0", "0", "0"]  # initial parking data


# @views.route('/parkingData', methods=['GET'])
# def get_parking_data():
#     # read parking data
#     # res1 = sheet.values().get(spreadsheetId=SAMPLE_SPREADSHEET_ID,
#     #   range=SAMPLE_RANGE_NAME1).execute()
#     # readParkingData = res1.get('values', [])
#     # if readParkingData == []:
#     #     readParkingData = [["00000"]]

#     # # read entry data
#     # res2 = sheet.values().get(spreadsheetId=SAMPLE_SPREADSHEET_ID,
#     #                           range=SAMPLE_RANGE_NAME2).execute()
#     # readEntry = res2.get('values', [])
#     # if readEntry == []:
#     #     readEntry = [["0"]]

#     # # read exit data
#     # res3 = sheet.values().get(spreadsheetId=SAMPLE_SPREADSHEET_ID,
#     #                           range=SAMPLE_RANGE_NAME3).execute()
#     # readExit = res3.get('values', [])
#     # if readExit == []:
#     #     readExit = [["0"]]

#     # Read data from NodeMCU server and Update Google Sheets

#     # Modfiy this code segment to read actual data.
#     url = "http://192.168.91.188/"  # put the node mcu generate url here.
#     response = requests.get(url)
#     print('crossed1')
#     if response.status_code == 200:
#         # print("yes!!")
#         data_from_server = response.json()
#         # print("this is the data!", data_from_server['data'])
#         # print(jsonify(data_from_server), 200)
#         # curr_parking_data = readParkingData[0][0]
#         # print("current parking data: ", curr_parking_data)
#         if curr_parking_data[0] == '2':
#             if str(data_from_server['data0']) == '0':
#                 parkingspot1 = '0'
#         else:
#             parkingspot1 = str(data_from_server['data0'])

#         if curr_parking_data[1] == '2':
#             if str(data_from_server['data1']) == '0':
#                 parkingspot2 = '0'
#         else:
#             parkingspot2 = str(data_from_server['data1'])

#         if curr_parking_data[2] == '2':
#             if str(data_from_server['data2']) == '0':
#                 parkingspot3 = '0'
#         else:
#             parkingspot3 = str(data_from_server['data2'])

#         if curr_parking_data[3] == '2':
#             if str(data_from_server['data3']) == '0':
#                 parkingspot4 = '0'
#         else:
#             parkingspot4 = str(data_from_server['data3'])

#         if curr_parking_data[4] == '2':
#             if str(data_from_server['data4']) == '0':
#                 parkingspot5 = '0'
#         else:
#             parkingspot5 = str(data_from_server['data4'])

#         parkingspot1 = str(data_from_server['data0'])
#         parkingspot2 = str(data_from_server['data1'])
#         parkingspot3 = str(data_from_server['data2'])
#         parkingspot4 = str(data_from_server['data3'])
#         parkingspot5 = str(data_from_server['data4'])
#         entry_bit = str(data_from_server['data5'])
#         exit_bit = str(data_from_server['data6'])
#     else:
#         print("Failed to retrieve data", 500)

#     # trial data - modify this
#     # parkingspot1 = '1'
#     # parkingspot2 = '0'
#     # parkingspot3 = '1'
#     # parkingspot4 = '0'
#     # parkingspot5 = '1'
#     # entry_bit = '1'
#     # exit_bit = '0'

#     # ----------------------------------------------xxxxxxxxxxxxxxxxx---------------------------------------------
#     # This code segment is to generate random example data for the parking
#     # data = "10001"  # example data
#     # random_num = random.randint(129, 500)
#     # binary_num = bin(random_num)[2:]
#     # last_five_bits = binary_num[0:5]
#     # entry_bit = binary_num[5]
#     # exit_bit = binary_num[6]
#     # data = ''.join(['1' if bit == '1' else '0' for bit in last_five_bits])
#     # print("parking data: ", data)
#     # ----------------------------------------------xxxxxxxxxxxxxxxxx---------------------------------------------

#     parking_data = parkingspot1 + parkingspot2 + \
#         parkingspot3 + parkingspot4 + parkingspot5
#     # entry_exit = entry_bit + exit_bit

#     if global_entry_data == "0" and entry_bit == "1":
#         entryval = "1"
#     if global_exit_data == "0" and exit_bit == "1":
#         exitval = "1"

#     # lst1 = [[parking_data]]
#     # lst2 = [[entry_bit]]
#     # lst3 = [[exit_bit]]

#     # if readEntry[0][0] == "0" and entry_bit == "1":
#     #     entryval = "1"
#     # else:
#     #     entryval = "0"

#     # if readExit[0][0] == "0" and exit_bit == "1":
#     #     exitval = "1"
#     # else:
#     #     exitval = "0"

#     # # write parking data
#     # request1 = sheet.values().update(spreadsheetId=SAMPLE_SPREADSHEET_ID, range=SAMPLE_RANGE_NAME1,
#     #                                  valueInputOption="RAW", body={"values": lst1}).execute()

#     # # write entry/exit data
#     # request2 = sheet.values().update(spreadsheetId=SAMPLE_SPREADSHEET_ID, range=SAMPLE_RANGE_NAME2,
#     #                                  valueInputOption="RAW", body={"values": lst2}).execute()
#     # request3 = sheet.values().update(spreadsheetId=SAMPLE_SPREADSHEET_ID, range=SAMPLE_RANGE_NAME3,
#     #                                  valueInputOption="RAW", body={"values": lst3}).execute()
#     # print(request1, request2, request3)

#     # print(readParkingData, readEntry, readExit)
#     # print(res1, res2, res3)

#     # Modify button color based on data
#     # colors = ['#28a745', '#dc3545']  # red and green
#     colors = ['#dc3545', '#28a745']  # red and green
#     color = []
#     for value in parking_data:
#         color.append(colors[int(value)])
#         # script = f"document.getElementById('{btn_id}').style.backgroundColor='{color}'"
#     # return jsonify({'color': color, 'stm32': readParkingData[0][0], 'entryData': entryval, 'exitData': exitval})
#     return jsonify({'color': color, 'stm32': parking_data, 'entryData': entryval, 'exitData': exitval})


# @views.route('/api/reservation', methods=['POST'])
# def reserve_parking():
#     # res1 = sheet.values().get(spreadsheetId=SAMPLE_SPREADSHEET_ID,
#     #                           range=SAMPLE_RANGE_NAME1).execute()
#     # readParkingData = res1.get('values', [['00000']])
#     # # print(readParkingData[0][0])
#     # parking_data = readParkingData[0][0]
#     button_id = request.json['id']  # extract button_id from JSON data
#     # # get the index of the button
#     button_index = int(button_id[3]) - 1
#     curr_parking_data[button_index] = '2'
#     time[button_index] = 100
#     # # print("This is the OG button: ", button_index)
#     # new_parking_data = parking_data[:button_index] + \
#     #     "2" + parking_data[button_index + 1:]
#     # # write parking data
#     # lst1 = [[new_parking_data]]
#     # # lst1 = [[button_index]]
#     # request1 = sheet.values().update(spreadsheetId=SAMPLE_SPREADSHEET_ID, range=SAMPLE_RANGE_NAME1,
#     #                                  valueInputOption="RAW", body={"values": lst1}).execute()
#     # print('successfully reserved')
#     return jsonify({'success': True})


# # curr_parking_data = ["0", "0", "0", "0", "0"]
# # time_remaining = [-1, -1, -1, -1, -1]
# # t0 =
# # for i in range(5):
# #     if curr_parking_data[i] == "2":
# #         time_remaining[i] -= t0


# @ views.route('/')
# def home():
#     return render_template("home.html")
