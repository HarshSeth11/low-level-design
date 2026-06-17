from prototype import Prototype
import copy

class GameCharacter(Prototype):
    def __init__(
        self,
        character_type,
        health,
        weapon
    ):
        self._character_type = character_type
        self._health = health
        self._weapon = weapon

    def clone(self):
        return copy.deepcopy(self)
    
    def character_type_setter(self, character_type):
        self._character_type = character_type

    def health_setter(self, health):
        self._health = health

    def weapon_setter(self, weapon):
        self._weapon = weapon
    
    def __str__(self):
        return (
            f"Type: {self._character_type}, "
            f"Health: {self._health}, "
            f"Weapon: {self._weapon}"
        )