import requests
import urllib
import json
import sys
import traceback


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