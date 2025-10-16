import requests
import json
from pathlib import Path

SOCKET_ADDRESS = "192.168.178.75:8000"



def upload_file():
    mime_type = "application/vnd.android.package-archive" 
    url = f"http://{SOCKET_ADDRESS}/api/v1/upload"
    headers = {
        "Authorization": "a956188aacc6b3f7d81262b2d5ef8b43d777c50c59722fd055b2ee77ebae3264"
    }
    file_path = Path("/Users/cihan.sa/Coding/Damn-Vulnerable-Bank/dvba.apk")

    with open(file_path, "rb") as f:   
        files = {"file": (file_path.name, f, mime_type)}
        r = requests.post(url, headers=headers, files=files)
        r.raise_for_status()

    #TODO initial upload in DATENBANK speichern mit hash und file_name. beides kommt als response zurück

    print("Status Code Upload:", r.status_code)
    #print("Response:", r.text)



def scan_file():
    url = f"http://{SOCKET_ADDRESS}/api/v1/scan"
    headers = {
        "Authorization": "a956188aacc6b3f7d81262b2d5ef8b43d777c50c59722fd055b2ee77ebae3264"
    }

    #TODO Hash dynamisch machen kommt von upload_file() zurück 

    data = {"hash": "5b40b49cd80dbe20ba611d32045b57c6"}
    r = requests.post(url, headers=headers, data=data)
    r.raise_for_status()

    try:
        parsed = r.json()
        with open("report.json", "w", encoding="utf-8") as f:
            json.dump(parsed, f, indent=2, ensure_ascii=False, sort_keys=True)
    except ValueError:
        # Falls die Antwort kein JSON ist (z. B. PDF oder Fehlertext)
        with open("report.json", "wb") as f:
            f.write(r.content)
    #TODO JSON in DATENBANK speichern
    
    #print("Keine gültige JSON-Antwort – Rohdaten gespeichert.")
    print("Status Code Scan:", r.status_code)
   


def generate_pdf():
    url = f"http://{SOCKET_ADDRESS}/api/v1/download_pdf"
    headers = {
        "Authorization": "a956188aacc6b3f7d81262b2d5ef8b43d777c50c59722fd055b2ee77ebae3264"
    }
    data = {"hash": "5b40b49cd80dbe20ba611d32045b57c6"}
    r = requests.post(url, headers=headers, data=data)
    r.raise_for_status()
    with open("report.pdf", "wb") as f:
        f.write(r.content)

    print("Status Code:", r.status_code)
    