from flask import Flask, request, render_template, abort
import re

app = Flask(__name__)

## This part is only used, if we would like to use HTML template for our converter application.
@app.route('/')
def home():
    return render_template('index.html')

## This part belongs to normal converter processing '/convert/<value>/<input_format>/<output_format>'
def convert_value(value, input_format, output_format):
    try:
        if input_format == 'dec':
            if not value.isdigit():
                abort(400, description="Invalid decimal value. It should only contain digits.")
            number = int(value)
        elif input_format == 'bin':
            if not re.fullmatch(r'[01]+', value):
                abort(400, description="Invalid binary value. It should only contain '0' or '1'.")
            number = int(value, 2)
        elif input_format == 'hex':
            if not re.fullmatch(r'[0-9a-fA-F]+', value):
               abort(400, description="Invalid hexadecimal value. Must contain only 0-9 and a-f/A-F.")
            number = int(value, 16)
        else:
            abort(400, description="Ups, something went wrong, please contact with kissge83@gmail.com")

        if output_format == 'dec':
            return str(number)
        elif output_format == 'bin':
            return bin(number)[2:]
        elif output_format == 'hex':
            return hex(number)[2:]

        else:
            abort(400, description="Invalid output format. Supported formats are: dec, bin, hex.")
    except ValueError:
        abort(400, description="Conversion error. Please ensure the value matches the input format.")

## Processing the normal converter
@app.route('/convert/<value>/<input_format>/<output_format>', methods=['GET'])
def convert(value, input_format, output_format):
    result = convert_value(value, input_format, output_format)
    return result, 200, {'Content-Type': 'text/plain'}

## Health check for application
@app.route('/health', methods=['GET'])
def health_check():
    return "OK", 200, {'Content-Type': 'text/plain'}

## Process for HTML converter
@app.route('/convert', methods=['POST'])
def convert_form():
    value = request.form['value']
    input_format = request.form['input_format']
    output_format = request.form['output_format']

    try:
        if input_format == 'dec':
            if not value.isdigit():
                return render_template('index.html', error="Invalid decimal value. Must contain only digits (0-9).")
            num = int(value)
        elif input_format == 'bin':
            if not re.fullmatch(r'[01]+', value):
                return render_template('index.html', error="Invalid binary value. Must contain only 0 and 1.")
            num = int(value, 2)
        elif input_format == 'hex':
            if not re.fullmatch(r'[0-9a-fA-F]+', value):
                return render_template('index.html', error="Invalid hexadecimal value. Must contain only 0-9 and a-f/A-F.")
            num = int(value, 16)
        else:
            return render_template('index.html', error="Ups, something went wrong, please contact with kissge83@gmail.com")

        if output_format == 'dec':
            result = str(num)
        elif output_format == 'bin':
            result = bin(num)[2:]
        elif output_format == 'hex':
            result = hex(num)[2:]
        else:
            return render_template('index.html', error="Invalid output format")

        return render_template('index.html', result=result)

    except ValueError:
        return render_template('index.html', error="Invalid value for the given input format")


## Run application from anyhost on port 8080
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)

