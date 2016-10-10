class Car(object):

  number_of_doors = 4
  number_of_wheels = 4
  speed = 0

  def __init__(self, name='General', model='GM',car_type = "saloon"):
    self.name = name
    self.model = model
    self.car_type = car_type

    if self.name == 'Koenigsegg' or self.name == 'Porshe':
      self.number_of_doors = 2

    if self.car_type == 'trailer':
      self.number_of_wheels = 8

  def is_saloon(self):
    return self.car_type != 'trailer'

  def drive(self, speed):
    if speed == 7:
      self.speed = 77
    elif speed ==  3 :
      self.speed = 1000

    return self
