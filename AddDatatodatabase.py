import firebase_admin
from firebase_admin import credentials
from firebase_admin import db

cred = credentials.Certificate("serviceAccountKey.json")
firebase_admin.initialize_app(cred,{
    'databaseURL':"https://facerecog-attendance-sys-default-rtdb.firebaseio.com/"
})

ref = db.reference('Students')
data = {
    "3426":
        {
            "name": "Suraj S",
            "major": "B.tech in AIML",
            "Semester":5,
            "total_attendance":5,
            "standing":"g",
            "last_attended_time":"2023-01-05 12:07:34"
        },
    "3457":
{
            "name": "APJ Abdul Kalam",
            "major": "physics and aerospace engineering",
            "Semester":6,
            "total_attendance":100,
            "standing":"g",
            "last_attended_time":"2023-01-05 12:07:34"
        },
    "7888":
{
            "name": "Elon Musk",
            "major": "physics",
            "Semester":6,
            "total_attendance":90,
            "standing":"g",
            "last_attended_time":"2023-01-05 12:07:34"
        },

}

for key,value in data.items():
    ref.child(key).set(value)
