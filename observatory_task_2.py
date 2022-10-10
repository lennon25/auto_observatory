#!/usr/bin/python3

import requests
import datetime


def get_after_tomorrow_humidity():
    host = "http://pda.weather.gov.hk"
    url = host + "/locspc/android_data/fnd_e.xml?1.686170828993217"
    # url = host + "/locspc/android_data/fnd_e.xml"
    header = {
        "User-Agent": "Dalvik/2.1.0 (Linux; U; Android 12; 2107119DC Build/SKQ1.211006.001)",
        "Content-Type": "text/xml"
    }
    try:
        response = requests.get(url, header)
        if response.status_code == 200:
            print("request weather api is success")
            resps = response.json()
            today = datetime.date.today()
            day_after_tomorrow = today + datetime.timedelta(+2)
            #print(resps)

            for rsp in resps["forecast_detail"]:
                if rsp["forecast_date"] == day_after_tomorrow.strftime("%Y%m%d"):
                    the_day_after_tomorrow_humidity = "{} - {}%".format(rsp["min_rh"], rsp["max_rh"])
                    print("The day after tomorrow humidity is: {}".format(the_day_after_tomorrow_humidity))
                    return the_day_after_tomorrow_humidity
 
        else:
            print("request failed")
    except Exception as ex:
        print(ex)


if __name__ == "__main__":
    get_after_tomorrow_humidity()
