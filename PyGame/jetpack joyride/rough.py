import pygame
import sys

pygame.init()

# Set up the display
SCREEN_WIDTH, SCREEN_HEIGHT = 800, 600
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("User Input Box")

# Set up fonts
font = pygame.font.SysFont(None, 36)

# Set up colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GRAY = (200, 200, 200)

# Set up input box
input_box = pygame.Rect(100, 100, 200, 40)
color_inactive = pygame.Color("lightskyblue3")
color_active = pygame.Color("dodgerblue2")
color = color_inactive
text = ""
text_surface = font.render(text, True, color, WHITE)  # Set the background color to WHITE
width = max(200, text_surface.get_width() + 10)
input_box.w = width

# Set up submit button
submit_button = pygame.Rect(100, 160, 200, 40)
submit_color = GRAY

# Set up cursor variables
cursor_visible = True
cursor_timer = 0

active = False
submit_active = False

clock = pygame.time.Clock()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            if input_box.collidepoint(event.pos):
                active = not active
            else:
                active = False
            if submit_button.collidepoint(event.pos):
                print(f"Submitted: {text}")
                text = ""
            color = color_active if active else color_inactive
            submit_active = submit_button.collidepoint(event.pos)
        if event.type == pygame.KEYDOWN:
            if active:
                if event.key == pygame.K_RETURN:
                    print(f"Submitted: {text}")
                    text = ""
                elif event.key == pygame.K_BACKSPACE:
                    text = text[:-1]
                elif len(text) < 12:
                    text += event.unicode
                width = max(200, font.size(text)[0] + 10)
                input_box.w = width
                text_surface = font.render(text, True, color, WHITE)
                cursor_timer = 0  # Reset cursor timer when a key is pressed

    screen.fill(BLACK)

    # Draw input box
    pygame.draw.rect(screen, color_inactive, input_box)
    pygame.draw.rect(screen, WHITE, (input_box.x + 5, input_box.y + 5, width - 10, 30))
    screen.blit(text_surface, (input_box.x + 5, input_box.y + 5))

    # Draw cursor if the input box is active
    if active:
        cursor_timer += clock.get_rawtime()
        if cursor_timer // 500 % 2 == 0:  # Blink every 500 milliseconds
            cursor_rect = pygame.Rect(input_box.x + 5 + text_surface.get_width(), input_box.y + 5, 2, 30)
            pygame.draw.rect(screen, color, cursor_rect)

    # Draw submit button
    submit_button_color = submit_color if not submit_active else color_active
    pygame.draw.rect(screen, submit_button_color, submit_button)
    submit_text = font.render("Submit", True, WHITE)
    screen.blit(submit_text, (submit_button.x + 5, submit_button.y + 5))

    pygame.display.flip()
    clock.tick(30)
