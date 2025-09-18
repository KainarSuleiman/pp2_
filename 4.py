class Student:
    def __init__(self, university):
        self.university = university


class Worker:
    def __init__(self, salary):
        self.salary = salary


class Children:
    def __init__(self, school):
        self.school = school
        


class Society:
    def __init__(self, peoples: list):
        self.people = peoples

    def getCountStudents(self):
        pass

    def getCountWorkers(self):
        pass

    def getCountChild(self):
        pass




student1 = Student('NU')
student2 = Student('MUIT')
worker1 = Worker(45000)
worker2 = Worker(67000)
children1 = Children('Nazarbayev School')
children2 = Children('KTL')
society1 = Society([student1, student2, 
                    worker1, worker2, children1, children2])

