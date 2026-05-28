from receivers.fan import Fan
from commands.command import Command

class FanOnCommand(Command):
    def __init__(self, fan: Fan):
        self._fan = fan

    def execute(self):
        self._fan.on()