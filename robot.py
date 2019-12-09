class Robot(commandbased.CommandBasedRobot):
     def robotInit(self):
         self.arm = Arm()
         wpilib.command.Command.getRobot = lambda: self
         self.oi()
     
     def oi(self):
         self.joystick = wpilib.Joystick(0)
         wpilib.buttons.JoystickButton(self.joystick, ds4["x"]).toggleWhenPressed(Toggle())