import requests
import urllib
import json
import sys
import traceback

from selenium import webdriver
from selenium.webdriver.chrome.options import Options

import traceback
import time

import psycopg2


class Sofra1:
    
    empCount = 0

    def __init__(self):
        pass
  
    def call_ws(self, url):      
        try: 

            response = requests.get(url)

            todos = json.loads(response.text)
            
            for todo in todos["roundMatches"]["tournaments"]:
                for event in todo["events"]:            
                    print( event["homeTeam"]["name"], ' vs ',  event["awayTeam"]["name"], ' - ', 
                           event["homeScore"]["normaltime"] , ' : ' , event["awayScore"]["normaltime"] )
            
        
            #return(json.dumps(todos, sort_keys=True, indent=4, separators=(',', ': ')))
        
        except Exception:
            return("Unexpected error:", sys.exc_info())
            raise   
        
    def popuniKladionicu(self):   
        print('starting browser')
        try:
            chrome_options = Options()  
            #chrome_options.add_argument('--headless')
            chrome_options.add_argument('--ignore-certificate-errors')
            chrome_options.add_argument("--test-type")
            chrome_options.binary_location = 'C:\Program Files (x86)\Google\Chrome\Application\chrome.exe'   
            
            chrome_options.add_argument("--disable-popup-blocking");         
             
            driver = webdriver.Chrome(chrome_options = chrome_options)
            
            driver.get('https://www.sofascore.com/hr/turnir/nogomet/italy/serie-a/23')
            
            pre = driver.find_element_by_class_name('js-event-list-tournament-events').text
            
            
            data = json.loads(pre)
            print(data)
                        
            try:
                alert = driver.switch_to_alert()
                alert.accept()
            except:
                print('No alert')
            
            unos=driver.find_element_by_id("B37164898911002989583")
            unos.click() 
            
            time.sleep(10) 
            
            
            trs = driver.find_element_by_class_name('t-Report-report').find_elements_by_tag_name('tr')
            
            
            
        except:
            print("Unexpected error:", sys.exc_info()) 
            traceback.print_exc()
            
            
    def test_db(self):      
        try: 
            conn = psycopg2.connect(database="sport", user = "python", password = "python", host = "127.0.0.1", port = "5432")

            print ('Opened database successfully')
            
            cur = conn.cursor()

            cur.execute("SELECT sport_id, sport_name  from sports")
            
            rows = cur.fetchall()
            for row in rows:
                print ("ID = ", row[0])
                print ("SPORT = ", row[1], "\n")

            print ("Operation done successfully")
            conn.close()            
  
        except Exception:
            return("Unexpected error:", sys.exc_info())
            raise             
            
            
if __name__ == '__main__':            
        try:           
            wst = Sofra1()
            
            #wst.popuniKladionicu()
            
            wst.test_db()
            
            print(wst.call_ws('https://www.sofascore.com/u-tournament/23/season/13768/matches/round/2?_=152641643'))
        except:
            print("Unexpected error:", sys.exc_info()[0])     
                       
                                