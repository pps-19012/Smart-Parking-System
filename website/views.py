import random  # for random generation of parking data
import requests
from flask import Blueprint, render_template, request, jsonify


from googleapiclient.discovery import build

from google.oauth2 import service_account

SERVICE_ACCOUNT_FILE = 'keys.json'
SCOPES = ['https://www.googleapis.com/auth/spreadsheets']

creds = None

creds = service_account.Credentials.from_service_account_file(
    SERVICE_ACCOUNT_FILE, scopes=SCOPES)

# The ID and range of a sample spreadsheet.
SAMPLE_SPREADSHEET_ID = '138K6l-Z_gsva38rQHpHxcx8Z5zo9CbQ_Hrwm8WrbDco'
SAMPLE_RANGE_NAME1 = 'Sheet1!A1'
SAMPLE_RANGE_NAME2 = 'Sheet1!A2'
SAMPLE_RANGE_NAME3 = 'Sheet1!A3'


views = Blueprint('views', __name__)

button_color = ['#dc3545', '#28a745', '#dc3545',
                '#dc3545', '#28a745']  # initial button colors

service = build('sheets', 'v4', credentials=creds)

# Call the Sheets API
sheet = service.spreadsheets()


@views.route('/parkingData', methods=['GET'])
def get_parking_data():
    # Read data from NodeMCU server and Update Google Sheets

    # Modfiy this code segment to read actual data.
    # url = "http://192.168.157.188/"  # put the node mcu generate url here.
    # response = requests.get(url)

    # if response.status_code == 200:
    #     print("yes!!")
    #     data_from_server = response.json()
    #     # print("this is the data!", data_from_server['data'])
    #     print(jsonify(data_from_server), 200)
    #     parkingspot1 = data_from_server['p1']
    #     parkingspot2 = data_from_server['p2']
    #     parkingspot3 = data_from_server['p3']
    #     parkingspot4 = data_from_server['p4']
    #     parkingspot5 = data_from_server['p5']
    #     entry_bit = data_from_server['entry']
    #     exit_bit = data_from_server['exit']
    # else:
    #     print("Failed to retrieve data", 500)

    # trial data
    parkingspot1 = '1'
    parkingspot2 = '0'
    parkingspot3 = '1'
    parkingspot4 = '0'
    parkingspot5 = '1'
    entry_bit = '1'
    exit_bit = '0'

    # ----------------------------------------------xxxxxxxxxxxxxxxxx---------------------------------------------
    # This code segment is to generate random example data for the parking
    # data = "10001"  # example data
    # random_num = random.randint(129, 500)
    # binary_num = bin(random_num)[2:]
    # last_five_bits = binary_num[0:5]
    # entry_bit = binary_num[5]
    # exit_bit = binary_num[6]
    # data = ''.join(['1' if bit == '1' else '0' for bit in last_five_bits])
    # print("parking data: ", data)
    # ----------------------------------------------xxxxxxxxxxxxxxxxx---------------------------------------------

    parking_data = parkingspot1 + parkingspot2 + \
        parkingspot3 + parkingspot4 + parkingspot5
    # entry_exit = entry_bit + exit_bit

    lst1 = [[parking_data]]
    lst2 = [[entry_bit]]
    lst3 = [[exit_bit]]
    print(lst1)
    print(lst2)
    print(lst3)

    # write parking data
    request1 = sheet.values().update(spreadsheetId=SAMPLE_SPREADSHEET_ID, range=SAMPLE_RANGE_NAME1,
                                     valueInputOption="RAW", body={"values": lst1}).execute()

    # write entry/exit data
    request2 = sheet.values().update(spreadsheetId=SAMPLE_SPREADSHEET_ID, range=SAMPLE_RANGE_NAME2,
                                     valueInputOption="RAW", body={"values": lst2}).execute()
    request3 = sheet.values().update(spreadsheetId=SAMPLE_SPREADSHEET_ID, range=SAMPLE_RANGE_NAME3,
                                     valueInputOption="RAW", body={"values": lst3}).execute()
    # print(request1, request2, request3)

    # read parking data
    res1 = sheet.values().get(spreadsheetId=SAMPLE_SPREADSHEET_ID,
                              range=SAMPLE_RANGE_NAME1).execute()
    readParkingData = res1.get('values', [])

    # read entry data
    res2 = sheet.values().get(spreadsheetId=SAMPLE_SPREADSHEET_ID,
                              range=SAMPLE_RANGE_NAME2).execute()
    readEntry = res2.get('values', [])

    # read exit data
    res3 = sheet.values().get(spreadsheetId=SAMPLE_SPREADSHEET_ID,
                              range=SAMPLE_RANGE_NAME3).execute()
    readExit = res3.get('values', [])

    # print(readParkingData, readEntry, readExit)
    # print(res1, res2, res3)
    # Modify button color based on data
    colors = ['#28a745', '#dc3545']  # red and green
    color = []
    for value in parking_data:
        color.append(colors[int(value)])
        # script = f"document.getElementById('{btn_id}').style.backgroundColor='{color}'"
    return jsonify({'color': color, 'stm32': readParkingData[0][0], 'entryData': readEntry[0][0], 'exitData': readExit[0][0]})


@views.route('/api/reservation', methods=['POST'])
def reserve_parking():
    # button_id = request.form['button_id']
    # button_index = int(button_id.split('btn')[1]) - 1
    # current_color = button_color[button_index]

    # if current_color == '#28a745':
    #     # change to yellow
    #     button_color[button_index] = '#ffc107'
    #     # send post request to reservation API
    #     # reservation_response = requests.post('api/reservation', data={'button_id': button_id})

    return 'successfully reserved'


@views.route('/')
def home():
    return render_template("home.html")
