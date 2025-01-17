from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/calculate', methods=['POST'])
def calculate():
    data = request.get_json()
    operation = data['operation']
    num1 = data['num1']
    num2 = data['num2']

    if operation == 'add':
        result = num1 + num2
    elif operation == 'subtract':
        result = num1 - num2
    elif operation == 'multiply':
        result = num1 * num2
    elif operation == 'divide' and num2 != 0:
        result = num1 / num2
    else:
        return jsonify({'error': 'Invalid operation or division by zero'}), 400

    return jsonify({'result': result})

if __name__ == '__main__':
   app.run (host='0.0.0.0', port=80)
