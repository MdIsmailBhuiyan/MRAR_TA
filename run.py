import random
import pygame
from environment import Environment
from agent import Agent
from visualization import visualize_environment_pygame

#python -m venv myenv
#myenv\Scripts\activate
#pip install pydicom numpy matplotlib opencv-python tensorflow scikit-learn Pillow
#python run.py

def main():
    # Main loop to simulate agent-environment interaction with visualization using Pygame
    env = Environment((25,25))
    agent = Agent()
    visualize_environment_pygame(env, agent)

if __name__ == "__main__":
    main()