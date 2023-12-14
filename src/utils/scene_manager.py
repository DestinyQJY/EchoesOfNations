class SceneManager:
    def __init__(self):
        self.scenes = {}
        self.current_scene = None

    def add_scene(self, name, scene):
        self.scenes[name] = scene

    def switch_to(self, name):
        self.current_scene = self.scenes.get(name)

    def update(self, event):
        if self.current_scene:
            self.current_scene.handle_event(event)

    def draw(self):
        if self.current_scene:
            self.current_scene.draw()
