class Course:
    def __init__(self,name):
        self.name = name
        self.leces = []
    def add_lec(self,datalist):
        key_temp = ['CCode','Unt','Instructor','Week','Time','Place','Final','Max','Enr','Req','Rstr','Status']
        data_temp =dict(zip(*(key_temp,key_temp)))
        for key,value in zip(key_temp,datalist):
            data_temp[key] = value
        self.leces.append(data_temp)
