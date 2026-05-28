from commands.light_on_command import LightOnCommand
from commands.light_off_command import LightOffCommand
from commands.fan_on_command import FanOnCommand
from commands.fan_off_command import FanOffCommand

from invoker.remote_control import RemoteControl
from receivers.light import Light
from receivers.fan import Fan

def main():
    # Create receivers
    light = Light()
    fan = Fan()

    # Create Commands
    light_on = LightOnCommand(light)
    light_off = LightOffCommand(light)
    fan_on = FanOnCommand(fan)
    fan_off = FanOffCommand(fan)

    # Create Invoker
    remote = RemoteControl()

    # Execute Commands
    remote.set_command(light_on)
    remote.execute_command()
    remote.set_command(light_off)
    remote.execute_command()
    remote.set_command(fan_on)
    remote.execute_command()
    remote.set_command(fan_off)
    remote.execute_command()

if __name__ == "__main__":
    main()