import pygame

def visualize_environment_pygame(environment, agent):
    pygame.init()
    grid_size = environment.grid_size
    cell_size = 20
    screen_size = (grid_size[1] * cell_size, grid_size[0] * cell_size)
    screen = pygame.display.set_mode(screen_size)
    pygame.display.set_caption("Agent-Environment Visualization")

    agent_color = (0, 0, 255)  # Blue
    goal_color = (255, 0, 0)   # Red
    battery_color = (0,255,0) # Green
    background_color = (255, 255, 255)  # White

    running = True
    recharge = []
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        screen.fill(background_color)

        # Draw the grid
        for x in range(0, screen_size[0], cell_size):
            for y in range(0, screen_size[1], cell_size):
                rect = pygame.Rect(x, y, cell_size, cell_size)
                pygame.draw.rect(screen, (200, 200, 200), rect, 1)

        # Draw the agent
        agent_pos = environment.agent_position
        agent_rect = pygame.Rect(agent_pos[1] * cell_size, agent_pos[0] * cell_size, cell_size, cell_size)
        pygame.draw.ellipse(screen, agent_color, agent_rect)

        # Draw the goal
        goal_pos = environment.goal_position
        goal_rect = pygame.Rect(goal_pos[1] * cell_size, goal_pos[0] * cell_size, cell_size, cell_size)
        pygame.draw.rect(screen, goal_color, goal_rect)

        # Draw the Recharge points
        for element in recharge:
            recharge_rect = pygame.Rect(element[1] * cell_size, element[0] * cell_size, cell_size, cell_size)
            pygame.draw.ellipse(screen, battery_color, recharge_rect)

        pygame.display.flip()
        pygame.time.delay(500)

        if environment.is_goal_reached():
            print("Goal reached!")
            running = False
        else:
            recharge_point = agent.act(environment) # return if recharge
            if recharge_point:
                recharge.append(recharge_point)

    pygame.quit()