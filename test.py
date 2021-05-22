
import requests
import datetime
import json
from fake_useragent import UserAgent
import pyttsx3
import time

def vaccineChecker():
    engine  =pyttsx3.init()

    temp_user_agent = UserAgent()
    browser_header = {'User-Agent': temp_user_agent.random}  
    base = datetime.datetime.today()
    date_list = [base + datetime.timedelta(days=x) for x in range(10)]
    date_str = [x.strftime("%d-%m-%Y") for x in date_list]
    print ("Checking for available capacity and age limit  " , datetime.datetime.now().strftime("%H:%M:%S"))
    flag =0
    for INP_DATE in date_str:
        URL1 = "https://cdn-api.co-vin.in/api/v2/appointment/sessions/public/calendarByDistrict?district_id={}&date={}".format(294, INP_DATE)
    
        response = requests.get(URL1,headers=browser_header )
        if response.ok:
            resp_json = response.json()
             #print(json.dumps(resp_json, indent = 1))
           
            for center in resp_json["centers"]:
                for session in center["sessions"]:
                    if session["min_age_limit"] == 18 and session["available_capacity_dose1"] >0 :
                        flag = 1
                        print("\t", session["date"])
                        print("\t", session["min_age_limit"])
                        print("\t", center["name"])
                        print("\t", center["address"])
                        print("\t", center["block_name"])
                        print("\t Price: ", center["fee_type"])
                        print("\t Available Capacity: ", session["available_capacity"])
                        if(session["vaccine"] != ''):
                            print("\t Vaccine: ", session["vaccine"])
                            print("\n\n")
        else:
            print ("Error in the Response " )
    if flag == 1:
            engine.say('Vaccine Available  Rush  ')
            engine.runAndWait()
            flag = 0


def main():
    while True:
        vaccineChecker()
        time.sleep(30)
        



if __name__ == "__main__":
    main()