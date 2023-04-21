import random  # for random generation of parking data
import requests
from flask import Blueprint, render_template, request, jsonify

views = Blueprint('views', __name__)

button_color = ['#dc3545', '#28a745', '#dc3545',
                '#dc3545', '#28a745']  # initial button colors


# @views.route('/api/data/stm32', methods=['GET'])
@views.route('/parkingData', methods=['GET'])
def get_parking_data():
    # Read data from NodeMCU server and Update Google Sheets

    # Modfiy this code segment to read actual data.
    # url = "http://192.168.157.188/"  # put the node mcu generate url here.
    # response = requests.get(url)

    # if response.status_code == 200:
    #     print("yes!!")
    #     data_from_server = response.json()
    #     print("this is the data!", data_from_server['data'])
    #     print(jsonify(data_from_server), 200)
    # else:
    #     print("Failed to retrieve data", 500)

    # This code segment is to generate random example data for the parking
    # data = "10001"  # example data
    random_num = random.randint(129, 500)
    binary_num = bin(random_num)[2:]
    last_five_bits = binary_num[0:5]
    entry_bit = binary_num[5]
    exit_bit = binary_num[6]
    data = ''.join(['1' if bit == '1' else '0' for bit in last_five_bits])
    # print("parking data: ", data)

    # Modify button color based on data
    colors = ['#28a745', '#dc3545']  # red and green
    color = []
    for value in data:
        color.append(colors[int(value)])
        # script = f"document.getElementById('{btn_id}').style.backgroundColor='{color}'"
    return jsonify({'color': color, 'stm32': data, 'entryData': entry_bit, 'exitData': exit_bit})


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
