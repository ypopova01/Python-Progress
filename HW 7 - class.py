class Student:
    def __init__(self, name, favorite_subjects):
        self.name = name
        self.favorite_subjects = favorite_subjects

    def greet(self):
        print('''Hello, I'am {}. My favorite subjects are: 
                         {} 
                         {}'''.format(self.name,self.favorite_subjects[0], self.favorite_subjects[1]))

ivan = Student("Ivan Ivanov", ["maths", "physics"])
alex = Student("Alex Petrov", ["arts", "music"])
maria = Student("Maria Popova", ["chemistry", "biology"])

ivan.greet()