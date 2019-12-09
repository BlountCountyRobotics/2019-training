import wpilib
import commandbased
import subsystems
import robot_map
import commands.arm as arm

class Robot(commandbased.CommandBasedRobot):
     def robotInit(self):
         self.arm = subsystems.Arm()
         wpilib.command.Command.getRobot = lambda: self
         self.oi()
     
     def oi(self):
         self.joystick = wpilib.Joystick(0)
         wpilib.buttons.JoystickButton(self.joystick, robot_map.ds4["x"]).toggleWhenPressed(Toggle())