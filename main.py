import pygame 


def main():
   import pygame

# Initialize pygame and set up the window
pygame.init()
window = pygame.display.set_mode((500, 500))

# Load the two images for the animation
image1 = pygame.image.load("img/moving.png")
image2 = pygame.image.load("img/standard.png")

# Set up the starting position of the image
x = 250
y = 250

# Initialize the index for the animation frames
frame = 0

# Main game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    # Get the current pressed keys
    keys = pygame.key.get_pressed()
    
    # Move the image based on the WASD inputs
    if keys[pygame.K_w]:
        y -= 0.1
    if keys[pygame.K_a]:
        x -= 0.1
    if keys[pygame.K_s]:
        y += 0.1
    if keys[pygame.K_d]:
        x += 0.1
    
    # Update the animation frame
    frame = (frame + 1) % 2
    
    # Clear the screen and draw the current frame of the animation
    window.fill((255, 255, 255))
    if frame == 0:
        window.blit(image1, (x, y))
    else:
        window.blit(image2, (x, y))
    
    # Update the display
    pygame.display.update()

# Quit pygame
pygame.quit()















if __name__ == '__main__':
    main()