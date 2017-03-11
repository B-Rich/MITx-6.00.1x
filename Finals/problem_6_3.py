class Person(object):
  def __init__(self, name):
    self.name = name
  def say(self, stuff):
    return self.name + ' says: ' + stuff
  def __str__(self):
    return self.name

class Lecturer(Person):
  def lecture(self, stuff):
    return 'I believe that ' + Person.say(self, stuff)

class Professor(Lecturer):
  def say(self, stuff):
    return 'Prof. ' + self.name + ' says: ' + self.lecture(stuff)

class ArrogantProfessor(Professor):
  def _say(self, stuff):
    return Person.say(self, stuff)
  def lecture(self, stuff):
    return 'It is obvious that ' + Lecturer.lecture(self, stuff)
  def say(self, stuff):
    return self._say(self.lecture(stuff))

ae = ArrogantProfessor('eric')
pe = Professor('eric')

assert pe.say('the sky is blue') == 'Prof. eric says: I believe that eric says: the sky is blue'
assert ae.lecture('the sky is blue') == 'It is obvious that I believe that eric says: the sky is blue'
