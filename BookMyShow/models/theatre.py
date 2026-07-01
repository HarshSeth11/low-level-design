from models.screen import Screen

class Theatre:
    def __init__(self, theatre_id, name, screens):
        self.theatre_id = theatre_id
        self.name = name
        self.screens = screens or []

    def add_screen(self, screen: Screen):
        self.screens.append(screen)
        print(f"Screen {screen.screen_name} Added to the Theatre.")
