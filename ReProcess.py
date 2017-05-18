import re
from collections import defaultdict
import course_database
class reprocess:
    def __init__(self,text,deptname):

        self.deptname = deptname
        db = self.data_rough_process(text)

        self.re_match(db)
        self.data_process()
    def data_rough_process(self,text)->{str:[str]}:#粗处理数据，不过滤dis，该字典包括课号下所有行
        count = 0
        inner_text = []
        db = defaultdict(list)
        for line in text:
            line = line.rstrip().lstrip()
            if '_________________________________________________________________' in line:
                count+=1
                continue

            if 'Total Classes Displayed:' in line:
                break
            if count >= 2:
                if '#' in line:
                    break
                inner_text.append(line)
        inner_text_iter = iter(inner_text)
        temp_database = {}
        key_name = ''
        begin_write = False
        while True:
            try:
                line = next(inner_text_iter)
            except StopIteration:
                break

            line_text = line.rstrip().lstrip()

            if line_text.startswith('CCode'):continue
            if 'Same as' in line_text:continue
            if 'ON LINE' in line_text:continue

            if begin_write == True:
                if line_text == '':
                    begin_write = False
                    continue
                temp_database[key_name].append(line_text)


            if (self.deptname.lower() in line_text.lower())and not(',' in line_text.lower()):
                key_name = line_text
                temp_database[key_name] = []
                begin_write = True
        return  temp_database





    def re_match(self,db):
        #细处理数据，过滤dis,create a Course Object which contains all the lectures of this course,参数格式为[CCode,Unt,Instructor,Week,Time,Place,Final,Max,Enr,Req,Rstr,Status]
        rp = re.compile(r"([\d]{5})[\ ]*LEC[^\d]*([\d]*)[\ ]*([A-Za-z\,\ ]*.)[\ ]*([MWFTuTh]*)[\ ]*((?:1[0-2]|[0-9])(?:\:[0-5][0-9]){0,2}-[\ ]*(?:1[0-2]|[0-9])(?:\:[0-5][0-9]){0,2}p?\ ?)[\ ]*([\w]*[\ ]*[\d]*)[\ ]*((?:(?:[^,]*,[^,]*,)[\ ]*(?:(?:1[0-2]|[0-9])(?:\:[0-5][0-9]){0,2}-[\ ]*(?:1[0-2]|[0-9])(?:\:[0-5][0-9]){0,2}\ ?(?:(?:am|pm)?))\ ?(?:\@[A-Z\ ]*[\w]*)?)|TBA)[\ ]*(\d*)[\ ]*(\d*(?:\/?\d*))[\ ]*([\d]*)[\ ]*([A-Z&]*)[\ ]*([\w]*)")

        self.courses = []
        for item in db.items():
            course = course_database.Course(item[0])
            for info_str in item[1]:
                #Can you do it in 1 line?
                info_list = []
                info_re = rp.match(info_str)
                if info_re == None:
                    continue
                for info in info_re.groups():
                    info_list.append(info)
                course.add_lec(info_list)
            self.courses.append(course)


    def data_process(self):
        pass
    def get_data(self)->course_database:
        return self.courses