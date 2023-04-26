import random  # for random generation of parking data
import requests
from flask import Blueprint, render_template, request, jsonify

views = Blueprint('views', __name__)

button_color = ['#dc3545', '#28a745', '#dc3545',
                '#dc3545', '#28a745']  # initial button colors
curr_parking_data = ["0", "0", "0", "0", "0"]  # initial parking data
entry_exit = ["1", "1"]
timer = [0, 0, 0, 0, 0]  # timer for each parking spot
# parkingspot1 = "0"
# parkingspot2 = "0"
# parkingspot3 = "0"
# parkingspot4 = "0"
# parkingspot5 = "0"


@views.route('/parkingData', methods=['GET'])
def get_parking_data():
    # Read data from NodeMCU server and Update Google Sheets
    # Modfiy this code segment to read actual data.
    url = "http://192.168.17.188/"  # put the node mcu generate url here.
    response = requests.get(url)
    if response.status_code == 200:
        print("yes!!")
        data_from_server = response.json()
        if curr_parking_data[0] == '2':
            if str(data_from_server['data0']) == '0':
                # parkingspot1 = '0'
                curr_parking_data[0] = '0'
        else:
            # parkingspot1 = str(data_from_server['data0'])
            curr_parking_data[0] = str(data_from_server['data0'])

        if curr_parking_data[1] == '2':
            if str(data_from_server['data1']) == '0':
                # parkingspot2 = '0'
                curr_parking_data[1] = '0'
        else:
            # parkingspot2 = str(data_from_server['data1'])
            curr_parking_data[1] = str(data_from_server['data1'])

        if curr_parking_data[2] == '2':
            if str(data_from_server['data2']) == '0':
                # parkingspot3 = '0'
                curr_parking_data[2] = '0'
        else:
            # parkingspot3 = str(data_from_server['data2'])
            curr_parking_data[2] = str(data_from_server['data2'])

        if curr_parking_data[3] == '2':
            if str(data_from_server['data3']) == '0':
                # parkingspot4 = '0'
                curr_parking_data[3] = '0'
        else:
            # parkingspot4 = str(data_from_server['data3'])
            curr_parking_data[3] = str(data_from_server['data3'])

        if curr_parking_data[4] == '2':
            if str(data_from_server['data4']) == '0':
                # parkingspot5 = '0'
                curr_parking_data[4] = '0'
        else:
            # parkingspot5 = str(data_from_server['data4'])
            curr_parking_data[4] = str(data_from_server['data4'])

        # parkingspot1 = str(data_from_server['data0'])
        # parkingspot2 = str(data_from_server['data1'])
        # parkingspot3 = str(data_from_server['data2'])
        # parkingspot4 = str(data_from_server['data3'])
        # parkingspot5 = str(data_from_server['data4'])
        entry_bit = str(data_from_server['data5'])
        exit_bit = str(data_from_server['data6'])

        if entry_exit[0] == "1" and entry_bit == "0":
            entry_val = "1"
        else:
            entry_val = "0"
        entry_exit[0] = entry_bit

        if entry_exit[1] == "1" and exit_bit == "0":
            exit_val = "1"
            entry_exit[1] = "0"
        else:
            exit_val = "0"
        entry_exit[1] = exit_bit

        for i in range(len(timer)):
            if timer[i] > 0:
                print("Reserved: ", i, " Timer: ", timer[i])
                if curr_parking_data[i] == '2':
                    if timer[i] - 10 <= 0:
                        curr_parking_data[i] = '1'
                        timer[i] = 0
                timer[i] -= 10

    else:
        print("Failed to retrieve data", 500)

    # parking_data = parkingspot1 + parkingspot2 + \
    #     parkingspot3 + parkingspot4 + parkingspot5

    parking_data = "".join(curr_parking_data)
    print("Parking Data:", parking_data)
    # Modify button color based on data
    colors = ['#dc3545', '#28a745']  # red and green
    color = []
    for value in parking_data:
        if int(value) != 2:
            color.append(colors[int(value)])
    return jsonify({'color': color, 'stm32': parking_data, 'entryData': entry_val, 'exitData': exit_val})


@views.route('/api/reservation', methods=['POST'])
def reserve_parking():
    button_id = request.json['id']  # extract button_id from JSON data
    # # get the index of the button
    button_index = int(button_id[3]) - 1
    curr_parking_data[button_index] = '2'

    # update timer
    timer[button_index] = 50
    return jsonify({'success': True})


@ views.route('/')
def home():
    return render_template("home.html")
