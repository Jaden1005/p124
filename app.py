from flask import Flask,jsonify, request

app = Flask(__name__)

contacts = [
    {
        'id': 1,
        'name': 'Dylan',
        'number': '8189258927', 
        'done': False
    },
    {
        'id': 2,
        'name': 'Sidd',
        'number': '8058372819', 
        'done': False
    }
]

@app.route("/add-data", methods=["POST"])
def add_contact():
    if not request.json:
        return jsonify({
            "status":"error",
            "message": "Please provide the data!"
        },400)

    contact = {
        'id': contacts[-1]['id'] + 1,
        'name': request.json['name'],
        'number': request.json.get('number', ""),
        'done': False
    }
    contacts.append(contact)
    return jsonify({
        "status":"success",
        "message": "contact added succesfully!"
    })
    

@app.route("/get-data")
def get_contact():
    return jsonify({
        "data" : contacts
    }) 

if (__name__ == "__main__"):
    app.run(debug=True)