 import wpilib
 import commandbased


 
 class Toggle(wpilib.command.InstantCommand):
     def __init__(self):
         super().__init__("Toggle")
         self.requires(self.getRobot().arm)
     
     def execute(self):
         self.getRobot().arm.toggle()
