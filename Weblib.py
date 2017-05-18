import requests
import urllib



class weblib:
    def __init__(self,year:str,dept:str,div:str):
        url = r'https://www.reg.uci.edu/perl/WebSoc'
        data = {
            'YearTerm': year,
            "Breadth": 'ANY',
            "Dept": dept,
            'Division':div,
            'ShowFinals': 'on',
            'Submit': 'Display Text Results'

        }
        response = requests.post(url, data=data)
        self.response = requests.post(url, data=data)

    def get_response(self)->str:
        return self.response.text
