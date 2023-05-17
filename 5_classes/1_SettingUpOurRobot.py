"""
Challenges

You have decided to use your programming knowledge to create a new robotics company.
Your idea for micro driving robots which are able to pick up and deliver objects was promising and now you want to start programming the logic.
These code challenges will use your knowledge of Classes to solve some example scenarios.
Try solving the five challenge problems below!

1. Setting Up Our Robot

Let’s begin by creating the class for our robot.
We will begin by setting up the instance variables to keep track of important data related to the robot.
Here are the steps we need to do:

    Create a new class called DriveBot
    Set up a basic constructor (no parameters needed)
    Initialize three instance variables within our constructor which all default to 0: motor_speed, direction, and sensor_range



"""
# Define the DriveBot class here!
class DriveBot:
  def __init__(self,motor_speed, direction, sensor_range):
    self.motor_speed = motor_speed
    self.motor_speed = 0
    self.sensor_range = sensor_range
    self.sensor_range = 0
    self.direction = direction
    self.direction = 0

robot_1 = DriveBot(5,10,90)

print(robot_1.motor_speed)
print(robot_1.direction)
print(robot_1.sensor_range)

########### step 2 ###############

class DriveBot:
    def __init__(self):
        self.motor_speed = 0
        self.direction = 0
        self.sensor_range = 0

    def control_bot(self,new_speed,new_direction):
      self.motor_speed = new_speed
      self.direction = new_direction

    def adjust_sensor(self, new_sensor_range):
      self.sensor_range = new_sensor_range

robot_1 = DriveBot()
# Use the methods here!
robot_1.control_bot(10,180)
robot_1.adjust_sensor(20)

print(robot_1.motor_speed)
print(robot_1.direction)
print(robot_1.sensor_range)
