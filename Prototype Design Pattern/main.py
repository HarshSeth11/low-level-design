from gamecharacter import GameCharacter

def main():
    warrior = GameCharacter(
        "Warrior",
        100,
        "Sword"
    )

    warrior_clone = warrior.clone()

    warrior_clone.weapon_setter("Axe")

    print("Original:")
    print(warrior)

    print()

    print("Clone:")
    print(warrior_clone)

if __name__ == "__main__":
    main()