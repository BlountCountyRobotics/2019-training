 import wpilib
 import commandbased
 
 class Arm(wpilib.command.Subsystem):
     def __init__(self):
         super().__init__("Arm")
         self.solenoid = wpilib.Solenoid(0)
 
     def toggle(self):
         self.solenoid.set(not self.solenoid.get())
 