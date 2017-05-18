import Weblib
import ReProcess
import prompt
import goody
import course_database
import collections

class user_req:
    def __init__(self):
        self.par_load()
        self.send_request()
        self.reslove_text()
        self.main_loop()
    def main_loop(self):
        while True:
            content = prompt.for_string("输入查询功能(else quit)", default='L')
            if content == 'quit':
                break
            if content == 'L':
                result_dict = {}
                for course in self.courses:
                    result_dict[course.name] = [0,0]#Enr,Max
                    for lec_info in course.leces:
                        if '/' in lec_info['Enr']:
                            enr = lec_info['Enr'].split('/')[1]
                            result_dict[course.name][0] += int(enr)
                        else:
                            result_dict[course.name][0] += int(lec_info['Enr'])
                        result_dict[course.name][1] += int(lec_info['Max'])
                result_list = sorted([(item,round(item[1][0]/item[1][1],3) ) for item in result_dict.items()if item[1][1] != 0 ],key = lambda x:(x[1],x[0][0] ))
                for item in result_list:
                    print(item)
        self.__init__()


    def send_request(self):
        wl = Weblib.weblib(year=self.year,dept=self.dep,div=self.div)
        self.response = wl.get_response()
    def par_load(self):
        self.year = prompt.for_string("Year?",default='2017-14')
        self.dep = prompt.for_string("Department?",default='I&C Sci')
        self.div = prompt.for_string("Division?(ANY 0xx or 1xx)", default='ANY')
    def reslove_text(self):
        webfile = open('web_content.txt','w')
        webfile.write(self.response)
        webfile.close()
        webfile = open('web_content.txt','r')
        self.text_process = ReProcess.reprocess(webfile,self.dep)
        self.courses = self.text_process.get_data()


if __name__ == '__main__':
    ur = user_req()
