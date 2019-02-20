import requests
import urllib
import json
import sys
import traceback

from selenium import webdriver
from selenium.webdriver.chrome.options import Options

import traceback
import time


class Wst:
    
    empCount = 0

    def __init__(self):
        pass
  
    def call_ws(self, url):      
        try: 

            response = requests.get(url)

            todos = json.loads(response.text)
        
            return(json.dumps(todos, sort_keys=True, indent=4, separators=(',', ': ')))
        
            #for todo in todos["teams"]:
            #    self.responseEdit.append(todo["name"] ) 
            #    self.responseEdit.append(todo["_links"]["self"]["href"])  
            #    self.responseEdit.append(todo["_links"]["fixtures"]["href"])  
            #    self.responseEdit.append(todo["_links"]["players"]["href"])  
            #    self.responseEdit.append(todo["crestUrl"])
            #    self.responseEdit.append("") 
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
            
            driver.get('https://apex.oracle.com/pls/apex/f?p=51345:LOGIN_DESKTOP:17023163753850:::::&tz=2:00')
            
            emailid=driver.find_element_by_id("P101_USERNAME")
            emailid.send_keys("branko")


            passw=driver.find_element_by_id("P101_PASSWORD")
            passw.send_keys("kkk")
            
            signin=driver.find_element_by_id("B27311205195543441998")
            signin.click()   
            
            try:
                alert = driver.switch_to_alert()
                alert.accept()
            except:
                print('No alert')
            
            unos=driver.find_element_by_id("B37164898911002989583")
            unos.click() 
            
            time.sleep(10) 
            
            
            trs = driver.find_element_by_class_name('t-Report-report').find_elements_by_tag_name('tr')
            
            #h = driver.find_element_by_class_name('t-Body-contentInner').text
            
            #print(h)
            
            print( len(trs) )
            
            for tr in trs:
                print('node:', tr)
                
                tds = tr.find_elements_by_tag_name('td')
                
                
                for td in tds:
                    header = td.get_attribute('headers')
                    txt    = td.get_attribute('textContent')
                    
                    txt = txt.encode('utf-8')
                    
                    print(header, ': ', txt)
                    
                    if header == 'HOME_REZ':
                        inp = td.find_element_by_tag_name('input')
                        inp_value = inp.get_attribute('value')
                        if inp_value == '':
                            inp.send_keys('2')
                            
                        #inp.send_keys('\b')
                        #inp.send_keys('\b')
                        
                        
                    if header == 'GUEST_REZ':
                        inp = td.find_element_by_tag_name('input')
                        inp_value = inp.get_attribute('value')
                        if inp_value == '':
                            inp.send_keys('1')                        
                            
                        #inp.send_keys('\b')
                        #inp.send_keys('\b')           
                    
            
            save=driver.find_element_by_id("B37172830720567434957")
            save.click()             
            
            
        except:
            print("Unexpected error:", sys.exc_info()) 
            traceback.print_exc()                    