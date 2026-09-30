print("Rozgar Update Bharat automatic updater started")

jobs = [
    {
        "title": "SSC Recruitment 2026",
        "category": "SSC",
        "qualification": "भर्ती की आधिकारिक अधिसूचना के अनुसार",
        "notification": "SSC की आधिकारिक भर्ती अधिसूचना देखें",
        "ageLimit": "आधिकारिक अधिसूचना के अनुसार",
        "lastDate": "आधिकारिक अधिसूचना के अनुसार",
        "applyLink": "https://ssc.gov.in/",
        "notificationLink": "https://ssc.gov.in/"
    }
]

for job in jobs:
    print("Job:", job["title"])
    print("Category:", job["category"])
    print("Qualification:", job["qualification"])
    print("Apply:", job["applyLink"])
    print("Notification:", job["notificationLink"])

print("Updater test completed")
