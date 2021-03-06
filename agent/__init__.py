import gym
from gym import wrappers, logger


class RandomAgent(object):
    """The world's simplest agent!"""

    def __init__(self, action_space):
        self.action_space = action_space

    def act(self, observation, reward, done):
        return self.action_space.sample()


if __name__ == '__main__':
    logger.set_level(logger.DEBUG)
    done = False
    env = gym.make('gym_snake:snake-v0')
    outdir = '/tmp'
    env = wrappers.Monitor(env, directory=outdir, force=True)
    agent = RandomAgent(env.action_space)
    reward = 0
    action = agent.act(None, reward, done)

    for i in range(100):
        ob = env.reset()
        while True:
            ob, reward, done, _ = env.step(action)
    env.close()
