import requests
import urllib
import json
import sys
import traceback

from selenium import webdriver
from selenium.webdriver.chrome.options import Options

import time

import psycopg2

class SofaHelper:
    

    def setDriver(self):   
        print('setting browser')
        try:
            chrome_options = Options()  
            chrome_options.add_argument('--headless')
            chrome_options.add_argument('--ignore-certificate-errors')
            chrome_options.add_argument("--test-type")
            chrome_options.binary_location = 'C:\Program Files (x86)\Google\Chrome\Application\chrome.exe'   
            chrome_options.add_argument("--disable-popup-blocking");         
            driver = webdriver.Chrome(chrome_options = chrome_options)
            
            return driver
        except:
            print("Unexpected error:", sys.exc_info()) 
            traceback.print_exc()
            
    def setDb(self):      
        try: 
            conn = psycopg2.connect(database="sport", user = "python", password = "python", host = "127.0.0.1", port = "5432")
            print ('Opened database successfully')    
            return conn
        except Exception:
            return("Unexpected error:", sys.exc_info())
            raise                                 
            
    def getTournamentSeasons(self, tournament_url, tournament_id, driver, conn):
        #open tournament and fetch season list from http response
        driver.get(tournament_url)    
        trs = driver.find_element_by_class_name('js-uniqueTournament-page-seasons-select').find_elements_by_class_name('pointer')
        
        #parsed seasons write to database
        for tr in trs:
            season_id = tr.get_attribute('data-season-id')
            season_name    = tr.get_attribute('textContent')
            print(season_id, ': ', season_name.strip() )  
            
            #get season json
            season_json = requests.get('https://www.sofascore.com/u-tournament/%s/season/%s/json' % (tournament_id, season_id))
            
            season_url = 'https://www.sofascore.com/u-tournament/23/season/13768/matches/round/%s'
            
            x = conn.cursor()
            
            #find if season is already inserted to db
            x.execute("select * from season where ss_season_id = %s" % (season_id)) 
            row= x.fetchone()
            
            if row == None:                         
                query =  "insert into season(season_name, competition_id, ss_season_id, ss_season_json ) values (%s, %s, %s, %s) ;"
                data = (season_name.strip(), tournament_id, season_id, season_json.text )
                x.execute(query, data)
            else:
                query =  "update season set season_name = %s, competition_id = %s, ss_season_id = %s, ss_season_json = %s;"
                data = (season_name.strip(), tournament_id, season_id, season_json.text )
                x.execute(query, data)            
            
        conn.commit()    
                 

if __name__ == '__main__':            
        try:           
            wst = SofaHelper()
            driver = wst.setDriver()
            conn = wst.setDb()
            
            wst.getTournamentSeasons('https://www.sofascore.com/hr/turnir/nogomet/italy/serie-a/23', 23, driver, conn)
            
            #===================================================================
            # driver.get('https://www.sofascore.com/hr/turnir/nogomet/italy/serie-a/23')
            # 
            # trs = driver.find_element_by_class_name('js-uniqueTournament-page-seasons-select').find_elements_by_class_name('pointer')
            # 
            # for tr in trs:
            #     #print('node:', tr)
            #     header = tr.get_attribute('data-season-id')
            #     txt    = tr.get_attribute('textContent')
            #     print(header, ': ', txt.strip() )            
            #===================================================================
            
        except:
            print("Unexpected error:", sys.exc_info() ) 
            traceback.print_exc()

                                   