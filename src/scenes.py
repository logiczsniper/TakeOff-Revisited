from resources import Resources


class SceneBase:
    def __init__(self):
        self.next = self
        self.resources = Resources()

    def render(self, screen):
        pass

    def switch_to_scene(self, next_scene):
        self.next = next_scene

    def terminate(self):
        self.switch_to_scene(None)


class TitleScene(SceneBase):
    def __init__(self):
        SceneBase.__init__(self)

    def render(self, screen):
        screen.blit(self.resources.TITLE_BG, (0, 0))


class VictoryScene(SceneBase):
    def __init__(self):
        SceneBase.__init__(self)

    def render(self, screen):
        screen.blit(self.resources.VICTORY_BG, (0, 0))


class CrashScene(SceneBase):
    def __init__(self):
        SceneBase.__init__(self)

    def render(self, screen):
        screen.blit(self.resources.CRASH_BG, (0, 0))


class PauseScene(SceneBase):
    def __init__(self):
        SceneBase.__init__(self)

    def render(self, screen):
        screen.blit(self.resources.PAUSE_BG, (0, 0))


class MidLevelScene(SceneBase):
    def __init__(self):
        SceneBase.__init__(self)

    def render(self, screen):
        screen.blit(self.resources.MIDLEVEL_BG, (0, 0))


class FirstLevelScene(SceneBase):
    def __init__(self):
        SceneBase.__init__(self)

    def render(self, screen):
        screen.blit(self.resources.FIRST_BG, (0, 0))


class SecondLevelScene(SceneBase):
    def __init__(self):
        SceneBase.__init__(self)

    def render(self, screen):
        screen.blit(self.resources.SECOND_BG, (0, 0))


class ThirdLevelScene(SceneBase):
    def __init__(self):
        SceneBase.__init__(self)

    def render(self, screen):
        screen.blit(self.resources.THIRD_BG, (0, 0))
