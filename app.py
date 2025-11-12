from flask import Flask, render_template


app = Flask(__name__)

JOBS = [
    {
        'id': 1,
        'company': 'ABC-Corp',
        'position': 'Security',
        'salary': '$100'
    },
    {
        'id': 2,
        'company': 'Umbrella-Corp',
        'position': 'Umbrella-Maker',
        'salaray': '$400'
    },
    {
        'id': 3,
        'company': 'Skynet',
        'position': 'Terminator',
        'salary': '$2',
    }
]


@app.route("/")
def hello_world():
    return render_template('index.html', jobs=JOBS)

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug = True)

