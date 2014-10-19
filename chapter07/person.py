
class Person:
    """
    Class represents a person
    """
    jobs = {}

    def __init__(self, name, job=None, pay=0):
        """
        Constructor method
        """
        self.name = name
        self.job = job
        self.pay = pay

        if job in self.jobs:
            self.jobs[job] += 1
        else:
            self.jobs[job] = 1

    def __del__(self):
        """
        Deconstructor: it will be called when gc recycle this object, or *del* called.
        """

    def last_name(self):
        """
        The first argument of instance methods is *self*.
        It's the reference to current instance, just like *this* in C++ and Java.
        """
        return self.name.split()[-1]

    def give_raise(self, percent):
        self.pay = int(self.pay * (1 + percent))

    def __str__(self):
        return self.name

    def __repr__(self):
        return '[%s: %s, %s]' % (self.__class__.__name__, self.name, self.pay)

    @classmethod
    def display_jobs(cls):
        for job, count in cls.jobs.items():
            print('%s: %d' % (job, count))

    @staticmethod
    def help():
        print("Person is a basic class")


class Manager(Person):

    def __init__(self, name, pay):
        super().__init__(name, 'manager', pay)

    def give_raise(self, percent, bonus=.1):
        Person.give_raise(self, percent + bonus)


if __name__ == '__main__':
    bob = Person('Bob Smith')
    sue = Person('Sue Jones', 'engineer', 8000)
    tom = Manager('Tom Jones', 5000)

    print(bob.last_name(), bob.pay)
    sue.give_raise(.1)
    print(sue.last_name(), sue.pay)
    print(bob)

    tom.give_raise(.1)
    print(repr(tom))

    Person.display_jobs()
    Person.help()
