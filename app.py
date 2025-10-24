from flask import Flask, render_template, request

app = Flask(__name__)

# Plant care data
plant_care = {
    "flowering": {
        "watering": "Water every 2–3 days. Keep the soil moist but not soggy.",
        "sunlight": "Needs at least 4–6 hours of sunlight daily."
    },
    "cactus": {
        "watering": "Water once every 10–14 days. Allow soil to dry completely.",
        "sunlight": "Prefers bright, direct sunlight for most of the day."
    },
    "indoor": {
        "watering": "Water once a week. Avoid overwatering.",
        "sunlight": "Thrives in indirect sunlight or shaded areas."
    },
    "herbs": {
        "watering": "Water every 3 days. Keep soil slightly moist.",
        "sunlight": "Needs at least 5–6 hours of sunlight daily."
    },
    "succulent": {
        "watering": "Water every 2 weeks. Ensure good drainage.",
        "sunlight": "Enjoys bright, indirect light."
    }
}


@app.route('/')
def home():
    return render_template('index.html')


@app.route('/result', methods=['POST'])
def result():
    plant_type = request.form['plant']
    if plant_type in plant_care:
        care = plant_care[plant_type]
        return render_template('result.html', plant=plant_type.capitalize(), care=care)
    else:
        return render_template('result.html', plant=plant_type, care=None)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
