import random
import pygame

class Agent:
    def __init__(self, actions=("up", "down", "left", "right")):
        self.battery_level=100
        self.total_recharge=0
        self.actions = actions

    def choose_action(self):
        action = "right"
        print("Please press arrow -> keys ")
        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_LEFT:  # Left arrow
                        action  = "left"
                        running = False
                    elif event.key == pygame.K_RIGHT:  # Right arrow
                        action  = "right"
                        running = False
                    elif event.key == pygame.K_UP:  # Up arrow
                        action  = "up"
                        running = False
                    elif event.key == pygame.K_DOWN:  # Down arrow
                        action  = "down"
                        running = False

        return action

        # Randomly choose an action from the list of possible actions
        # return random.choice(self.actions)

    def act(self, environment):
        # Choose an action and interact with the environment
        action = self.choose_action()
        environment.move_agent(action)
        print(f"Agent moved {action}, new position: {environment.get_state()}")
        if self.battery_level < 1:
            self.recharge_battery()
            self.total_recharge = self.total_recharge + 1
            return environment.get_state()
        else:
            self.battery_level = self.battery_level - 10
            return False
    
    def recharge_battery(self):
        self.battery_level=100
    