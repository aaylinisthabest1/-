from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/calculate', methods=['POST'])
def calculate():
    transport = float(request.form['transport'])
    electricity = float(request.form['electricity'])
    plastic = float(request.form['plastic'])
    
    # Простая формула для расчета углеродного следа
    carbon_footprint = (transport * 0.21) + (electricity * 0.527) + (plastic * 6)

    return render_template('result.html', carbon_footprint=carbon_footprint)

if __name__ == '__main__':
    app.run(debug=True)

