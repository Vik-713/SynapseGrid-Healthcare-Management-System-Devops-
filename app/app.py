import psycopg2
import os
# pyrefly: ignore [missing-import]
from flask import Flask, jsonify, render_template


app = Flask(__name__)
conn = psycopg2.connect(
    host=os.getenv("DB_HOST", "localhost"),
    port=os.getenv("DB_PORT", "5433"),
    database=os.getenv("DB_NAME", "synapsegrid"),
    user=os.getenv("DB_USER", "admin"),
    password=os.getenv("DB_PASSWORD", "admin123")
)

#API endpoints

patients = [
    {
        "id": 1,
        "name": "Rahul Sharma",
        "age": 32
    },
    {
        "id": 2,
        "name": "Priya Patel",
        "age": 28
    }
]

appointments = [
    {
        "id": 1,
        "patient": "Rahul Sharma",
        "doctor": "Dr. Mehta"
    },
    {
        "id": 2,
        "patient": "Priya Patel",
        "doctor": "Dr. Singh"
    }
]

medicines = [
    {
        "id": 1,
        "name": "Paracetamol",
        "stock": 100
    },
    {
        "id": 2,
        "name": "Amoxicillin",
        "stock": 50
    }
]

doctors = [
    {
        "id": 1,
        "name": "Dr. Mehta",
        "specialization": "Cardiology"
    },
    {
        "id": 2,
        "name": "Dr. Singh",
        "specialization": "Orthopedics"
    }
]

emergency = [
    {
        "id":1,
        "ambulance":"Available",
        "hospital":"City Hospital"
    },
    {
        "id":2,
        "ambulance":"Busy",
        "hospital":"General Hospital"
    }
]

#API routes

@app.route("/")
def home():
    return render_template("index.html")

@app.route('/patients')
def get_patients():
    return jsonify(patients)

@app.route('/appointments')
def get_appointments():
    return jsonify(appointments)

@app.route('/pharmacy')
def get_medicines():
    return jsonify(medicines)

@app.route('/doctors')
def get_doctors():
    return jsonify(doctors)


@app.route('/emergency')
def get_emergency():
    return jsonify(emergency)


@app.route('/status')
def status():
    return jsonify({
        "system":"SynapseGrid Healthcare",
        "status":"Running",
        "version":"1.0"
    })
    


@app.route('/dbtest')
def dbtest():
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM patients;")
    data = cursor.fetchall()
    cursor.close()
    return str(data)



@app.route('/dbstatus')
def dbstatus():
    try:
        cursor = conn.cursor()
        cursor.execute("SELECT 1;")
        cursor.close()

        return jsonify({
            "database": "Connected",
            "status": "Healthy"
        })

    except Exception as e:
        return jsonify({
            "database": "Disconnected",
            "status": "Unhealthy",
            "error": str(e)
        })
        

@app.route('/patientsdb')
def patientsdb():
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM patients;")

    rows = cursor.fetchall()
    cursor.close()

    result = []

    for row in rows:
        result.append({
            "id": row[0],
            "name": row[1],
            "age": row[2]
        })
    return jsonify(result)

        
@app.route('/appointmentsdb')
def appointmentsdb():
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM appointments;")

    rows = cursor.fetchall()
    cursor.close()

    result = []

    for row in rows:
        result.append({
            "id": row[0],
            "patient": row[1],
            "doctor": row[2]
        })
        
    return jsonify(result)


@app.route('/pharmacydb')
def pharmacydb():
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM pharmacy;")

    rows = cursor.fetchall()
    cursor.close()

    result = []

    for row in rows:
        result.append({
            "id": row[0],
            "medicine": row[1],
            "stock": row[2]
        })
    return jsonify(result)


@app.route('/doctorsdb')
def doctorsdb():
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM doctors;")

    rows = cursor.fetchall()
    cursor.close()

    result = []

    for row in rows:
        result.append({
            "id": row[0],
            "doctor": row[1],
            "specialization": row[2]
        })
    return jsonify(result)


@app.route('/emergencydb')
def emergencydb():
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM emergency;")

    rows = cursor.fetchall()
    cursor.close()

    result = []

    for row in rows:
        result.append({
            "id": row[0],
            "ambulance": row[1],
            "hospital": row[2]
        })

    return jsonify(result)



if __name__ == "__main__":
    app.run(
        host="0.0.0.0",
        port=5000,
        debug=True
    )