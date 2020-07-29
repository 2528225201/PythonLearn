'''学生教师输入输出程序'''


class Person(object):
    def __init__(self, id, name=''):
        self.setId(id)
        self.setName(name)

    def setId(self, id):
        self.__id = id

    def setName(self, name):
        if not isinstance(name, str):
            raise Exception('name must be string.')
        self.__name = name

    def show(self):
        print('编号为：', self.__id, '姓名为：', self.__name)


class Student(Person):
    def __init__(self, id, class_id, grade, name=''):
        super(Student, self).__init__(id, name)
        self.setClass_id(class_id)
        self.setGrade(grade)

    def setClass_id(self, class_id):
        self.__class_id = class_id

    def setGrade(self, grade):
        self.__grade = grade

    def show(self):
        super(Student, self).show()
        print('班号为：', self.__class_id)
        print('学生成绩为：', self.__grade)


class Teacher(Person):
    def __init__(self, id, job_title, department, name=''):
        super(Teacher, self).__init__(id, name)
        self.setJob_title(job_title)
        self.setDepartment(department)

    def setJob_title(self, job_title):
        self.__job_title = job_title

    def setDepartment(self, department):
        self.__department = department

    def show(self):
        super(Teacher, self).show()
        print('教师职称为：', self.__job_title)
        print('教师工作部门为：', self.__department)


if __name__ == '__main__':
    mengchao = Student(0, 0, 0, '')
    id = input('请输入学生编号：')
    name = str(input('请输入学生姓名：'))
    class_id = input('请输入学生班号：')
    grade = input('请输入学生成绩：')
    mengchao.setId(id)
    mengchao.setName(name)
    mengchao.setClass_id(class_id)
    mengchao.setGrade(grade)
    mengchao.show()
    print('=' * 30)

    MC = Teacher(0, '', '', '')
    id = input('请输入教师编号：')
    name = str(input('请输入教师姓名：'))
    job_title = str(input('请输入教师职称：'))
    department = str(input('请输入教师部门：'))
    MC.setId(id)
    MC.setName(name)
    MC.setJob_title(job_title)
    MC.setDepartment(department)
    MC.show()
    print('=' * 30)