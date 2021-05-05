from cowin_api import CoWinAPI
import time
from datetime import date, timedelta
from playsound import playsound
import json
import os



def notify():
    cwd = os.getcwd()
    playsound(cwd + "/pristine-609.mp3")
    
i =1
while(True):

    print("Number of time searched: " + str(i))
    print("--------------------------\n")

    tom = date.today() + timedelta(1)

    cowin = CoWinAPI()

    district_id = '503'
    date = tom.strftime("%d-%m-%Y")
    print("Searched on: ")
    print(date)

    min_age_limit = 18
    
    total_centers = cowin.get_availability_by_district(district_id,date, min_age_limit)

    for center in total_centers["centers"]:
        if(int(center["pincode"]/1000) == 324):
            sessions = center["sessions"]
            for session in sessions:
                if(session["available_capacity"] == 0):
                    print("Vaccine available at :"+ center["name"])
                    print("\n")
                    notify()

    time.sleep(5)
    i = i+1

