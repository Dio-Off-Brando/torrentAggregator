from bs4 import BeautifulSoup
import json
import requests
import os



class Search:
    def __init__(self, query, website=None):
        self.query = query.replace(' ', '+') 

        if website != None:
            with open(os.getcwd()+ "/websites/"+website+'.json', 'r') as file:
                website_config = json.loads(file.read())
                self.url = [website_config['url']]
                self.searchurl = [website_config['searchurl'].replace('{query}', self.query)]
        else:

            self.url = []
            self.searchurl = []

            for i in [os.getcwd()+"/websites/"+i for i in os.listdir(os.getcwd()+"/websites")]:
                with open(i, 'r') as configfile:
                    website_config = json.loads(configfile.read())
                    self.url.append(website_config['url'])
                    self.searchurl.append(website_config['searchurl'].replace('{query}', self.query))
            

            
    def QueryList(self):
        return [requests.get(i).text for i in self.searchurl]
        




# class QueryElement:
#      def __init__(self):
#         pass
    
