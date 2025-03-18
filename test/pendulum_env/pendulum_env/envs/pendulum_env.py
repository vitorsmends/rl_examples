import gym
from gym import spaces
import numpy as np
import rclpy
from rclpy.node import Node
from std_msgs.msg import String

class PendulumEnv(gym.Env):
    metadata = {"render_modes": ["human", "rgb_array"], "render_fps": 60}

    def __init__(self, render_mode=None, size=2):
        super().__init__('pendulumEnv')
        self.publisher_ = self.create_publisher(String, '/pendulum/cmd', 10)
        timer_period = 0.5  # seconds
        self.timer = self.create_timer(timer_period, self.timer_callback)
        self.i = 0