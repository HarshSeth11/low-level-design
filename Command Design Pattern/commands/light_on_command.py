from receivers.fan import Fan
from commands.command import Command
from receivers.light import Light

class LightOnCommand(Command):
    def __init__(self, light: Light):
        self._light = light

    def execute(self):
        self._light.on()