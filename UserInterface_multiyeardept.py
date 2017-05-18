import Weblib
import ReProcess
import prompt
import goody
import course_database
import collections

year_list = ['2017-92', '2017-76', '2017-51', '2017-39', '2017-25', '2017-14', '2017-03', '2016-92', '2016-76', '2016-51', '2016-39', '2016-25', '2016-14', '2016-03', '2015-92', '2015-76', '2015-51', '2015-39', '2015-25', '2015-14', '2015-03', '2014-92', '2014-76', '2014-51', '2014-39', '2014-25', '2014-14', '2014-03', '2013-92', '2013-76', '2013-51', '2013-39', '2013-25', '2013-14', '2013-03', '2012-92', '2012-76', '2012-51', '2012-39', '2012-25', '2012-14', '2012-03', '2011-51']
c_list = ['CHC/LAT','CLT&THY', 'AC ENG', 'AFAM', 'ANATOMY', 'ANESTH', 'ANTHRO', 'ARABIC', 'ART', 'ART HIS', 'ART STU', 'ARTS', 'ARTSHUM', 'ASIANAM', 'BANA', 'BATS', 'BIO SCI', 'BIOCHEM', 'BME', 'BSEMD', 'CAMPREC', 'CBEMS', 'CEM', 'CHEM', 'CHINESE', 'CLASSIC', 'COGS', 'COM LIT', 'COMPSCI', 'CRITISM', 'CRM/LAW', 'CSE', 'DANCE', 'DERM', 'DEV BIO', 'DRAMA', 'E ASIAN', 'EARTHSS', 'ECO EVO', 'ECON', 'ED AFF', 'EDUC', 'EECS', 'EHS', 'ENGLISH', 'ENGR', 'ENGRCEE', 'ENGRMAE', 'ENGRMSE', 'EPIDEM', 'ER MED', 'EURO ST', 'FAM MED', 'FIN', 'FLM&MDA', 'FRENCH', 'GEN&SEX', 'GERMAN', 'GLBL ME', 'GLBLCLT', 'GREEK', 'HEBREW', 'HINDI', 'HISTORY', 'HUMAN', 'HUMARTS', 'I&C SCI', 'IN4MATX', 'INT MED', 'INTL ST', 'ITALIAN', 'JAPANSE', 'KOREAN', 'LATIN', 'LAW', 'LINGUIS', 'LIT JRN', 'LPS', 'M&MG', 'MATH', 'MED', 'MED ED', 'MED HUM', 'MGMT', 'MGMT EP', 'MGMT FE', 'MGMT HC', 'MGMTMBA', 'MGMTPHD', 'MIC BIO', 'MOL BIO', 'MPAC', 'MUSIC', 'NET SYS', 'NEURBIO', 'NEUROL', 'NUR SCI', 'OB/GYN', 'OPHTHAL', 'PATH', 'PED GEN', 'PEDS', 'PERSIAN', 'PHARM', 'PHILOS', 'PHRMSCI', 'PHY SCI', 'PHYSICS', 'PHYSIO', 'PLASTIC', 'PM&R', 'POL SCI', 'PORTUG', 'PP&D', 'PSY BEH', 'PSYCH', 'PUB POL', 'PUBHLTH', 'color: gray', 'RAD SCI', 'RADIO', 'REL STD', 'ROTC', 'RUSSIAN', 'SOC SCI', 'SOCECOL', 'SOCIOL', 'SPANISH', 'SPPS', 'STATS', 'SURGERY', 'TAGALOG', 'TOX', 'UCDC', 'UNI AFF', 'UNI STU', 'VIETMSE', 'VIS STD', 'color: gray', 'WOMN ST', 'WRITING']
class user_req:
    def __init__(self):
        self.par_load()
        self.reslove_text()
        self.main_loop()
    def main_loop(self):
        while True:
            content = prompt.for_string("输入查询功能(else quit)", default='L')
            if content == 'quit':
                break
            if content == 'L':
                result_dict = {}
                for courses in self.courses_list:
                    for course in courses:
                        if not course.name in result_dict.keys():
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



    def par_load(self):


        self.div = prompt.for_string("Division?(ANY 0xx or 1xx)", default='ANY')
    def reslove_text(self):
        self.courses_list = []
        h_p_b = len(c_list)*len(year_list)
        h = 0

        for dep in c_list:
            per = h/h_p_b
            p_n = round(per*100,6)
            print(p_n,'%')
            for year in year_list:
                h += 1
                wl = Weblib.weblib(year=year, dept=dep, div=self.div)
                self.response = wl.get_response()
                webfile = open('web_content.txt','w')
                webfile.write(self.response)
                webfile.close()

                savepath = 'wb\\web_content{dp}-{y}.txt'.format(dp=dep,y=year).replace('/',' ')
                cache = open(savepath, 'w')
                cache.write(self.response)
                cache.close()

                webfile = open('web_content.txt','r')
                self.text_process = ReProcess.reprocess(webfile,dep)
                self.courses_list.append(self.text_process.get_data())


if __name__ == '__main__':
    ur = user_req()
