class Environment:
    def __init__(self, grid_size=(5, 5)):
        self.grid_size = grid_size
        self.agent_position = [0, 0]  # Initialize agent at top-left corner of the grid [x,y]
        self.goal_position = [grid_size[0] - 1, grid_size[1] - 1]  # Goal is at bottom-right corner

    def get_state(self):
        # Return the current state of the environment (agent's position)
        return tuple(self.agent_position)

    def is_goal_reached(self):
        # Check if the agent has reached the goal
        return self.agent_position == self.goal_position

    def move_agent(self, action):
        # Move the agent based on the given action ("up", "down", "left", "right")
        if action == "up" and self.agent_position[0] > 0:
            self.agent_position[0] -= 1
        elif action == "down" and self.agent_position[0] < self.grid_size[0] - 1:
            self.agent_position[0] += 1
        elif action == "left" and self.agent_position[1] > 0:
            self.agent_position[1] -= 1
        elif action == "right" and self.agent_position[1] < self.grid_size[1] - 1:
            self.agent_position[1] += 1

    def reset(self):
        # Reset the environment to the initial state
        self.agent_position = [0, 0]