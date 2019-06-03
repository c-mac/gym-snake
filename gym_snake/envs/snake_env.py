import gym
import pyglet
from gym import spaces
# from gym.envs.classic_control import rendering
# from gym.utils import seeding

WINDOW_W = 1000
WINDOW_H = 800


class Window(pyglet.window.Window):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)


class SnakeEnv(gym.Env):
    # metadata = {'render.modes': ['human']}

    def __init__(self):
        print('init')
        # Left, up, right, down
        self.action_space = spaces.Discrete(4)

    def step(self, action):
        return
        # super().step(action)

    def reset(self):
        print('reset')

    def render(self):
        print('render')
        self.viewer = Window(WINDOW_W, WINDOW_H)
        # self.viewer = rendering.SimpleImageViewer()
        # self.viewer = rendering.Viewer(WINDOW_W, WINDOW_H)
        # super().render()

    def close(self):
        print('close')
