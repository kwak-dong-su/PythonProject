class Worker:
    name=''
    age=0
    gender=''
    m_worker=0
    f_worker=0
    t_worker=0
    t_info=''

    def __init__(self, name, age, gender):
        self.name=name
        self.age=age
        self.gender=gender
        if gender=='남':
            Worker.m_worker+=1
        else:
            Worker.f_worker+=1
        Worker.t_worker+=1
        Worker.age+=age
        Worker.t_info += self.name + ', ' + str(self.age) + ', ' + self.gender + '\n'
        print(Worker.t_worker)
