from flask import Flask, request, render_template, send_file

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/generate_config', methods=['POST'])
def generate_config():
    xsuit_type = request.form['xsuit_type']
    xsuit_color = request.form['xsuit_color']
    zero_recoil = request.form['zero_recoil']
    aim_assist = request.form['aim_assist']
    aim_sensitivity = request.form['aim_sensitivity']

    config_content = f"""[ZeroRecoil]
Value={zero_recoil}

[AimAssist]
Value={aim_assist}

[AimSensitivity]
Value={aim_sensitivity}

[XSuit]
Type={xsuit_type}
Color={xsuit_color}
"""

    filename = "PUBGConfig.ini"
    with open(filename, "w") as file:
        file.write(config_content)

    return send_file(filename, as_attachment=True)

if __name__ == '__main__':
    app.run(debug=True)
