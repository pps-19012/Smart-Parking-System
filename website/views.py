import random  # for random generation of parking data

from flask import Blueprint, render_template, request, jsonify

views = Blueprint('views', __name__)

button_color = ['#dc3545', '#28a745', '#dc3545',
                '#dc3545', '#28a745']  # initial button colors


@views.route('/api/data/stm32', methods=['GET'])
def get_stm32_data():
    # Read data from STM32
    # data = request.args.get('data')

    # This code segment is to generate random example data for the parking
    # data = "10001"  # example data
    random_num = random.randint(50, 500)
    binary_num = bin(random_num)[2:]
    last_five_bits = binary_num[-5:]
    data = ''.join(['1' if bit == '1' else '0' for bit in last_five_bits])
    print("parking data: ", data)

    # Modify button color based on data
    colors = ['#28a745', '#dc3545']  # red and green
    color = []
    for value in data:
        color.append(colors[int(value)])
        # script = f"document.getElementById('{btn_id}').style.backgroundColor='{color}'"
    return jsonify({'color': color, 'stm32': data})


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
