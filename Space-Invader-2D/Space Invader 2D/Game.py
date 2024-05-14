import pygame
import random
import math

# Initialize the Pygame
pygame.init()

# Create a display
# NameOfScreen = pygame.display.set_mode((Width, Height))
Display = pygame.display.set_mode((800, 600))

backgroundImage = pygame.image.load("whiteBackground.jpg")

keepDisplay = True

# Title and icon
# Name of the game
pygame.display.set_caption("Space Invader")

# Logo / icon of the game (icon size: 32 x 32 pixels)
icon = pygame.image.load('outer-space-alien.png')

# Display game name / title.
pygame.display.set_icon(icon)

# Player / Get Player Image
playerImage = pygame.image.load('spaceship.png')
# Set player initial position at the start of game.
# These exact value(s) will set the player at the middle of the screen.
playerX = 370  # Player position x-coordinate
playerY = 480  # Player position y-coordinate
playerX_change = 0
playerY_change = 0

# Introducing the enemies and multiple enemies
enemyImage = []
enemyX = []
enemyY = []
enemyX_change = []
enemyY_change = []
score = 0
number_of_enemies = 6

for index in range(number_of_enemies + 1):
    enemyImage.append(pygame.image.load('alien-pixelated-shape-of-a-digital-game-64px.png'))
    enemyX.append(random.randint(0, 736))  # Enemy spawn random position x-coordinate
    enemyY.append(random.randint(50, 150))  # Enemy spawn random position y-coordinate
    enemyX_change.append(1)
    enemyY_change.append(12)

# Introducing the bullet / ammunition
# Ready - you cant see the bullet on the screen
# Fire - Bullet currently moving
bulletImage = pygame.image.load('bullet.png')
bulletX = 0
bulletY = 480
# bulletImage = pygame.transform.rotate(bulletImage, 45)  # ROTATE ANY IMAGE
bullet_state = "ready"
bulletX_change = 5
bulletY_change = 5


def player(x, y):
    # x and y are coordinates
    # Display.blit - Draw on surface of your display
    Display.blit(playerImage, (x, y))


def enemy(x, y, z):
    Display.blit(enemyImage[z], (x, y))


def shoot(x, y):
    global bullet_state
    bullet_state = "fire"
    Display.blit(bulletImage, (x + 19, y + 10))


def isCollision(enemy_x, enemy_y, bullet_x, bullet_y):
    distance = math.sqrt(math.pow((enemy_x - bullet_x), 2) + math.pow((enemy_y - bullet_y), 2))
    if distance < 27:
        return True
    else:
        return False


def isCollisionPlayer(enemy_x, enemy_y, player_x, player_y):
    distance = math.sqrt(math.pow((enemy_x - player_x), 2) + math.pow((enemy_y - player_y), 2))
    if distance < 27:
        return True
    else:
        return False


# Game Loop
# Move player / Move object / All events that take place in the game
while keepDisplay:
    # Change screen color
    # RGB - red, green, blue. RANGE is 0 - 255
    Display.fill((0, 0, 0))

    # Background Image
    Display.blit(backgroundImage, (0, 0))

    for event in pygame.event.get():
        # QUIT all capital letter
        if event.type == pygame.QUIT:
            keepDisplay = False

        # If player click key is pressed check whether it is right or left
        if event.type == pygame.KEYDOWN:  # Check if any key is pressed down

            # Left key pressed
            if event.key == pygame.K_LEFT:  # Check if left key pressed
                playerX_change = -1.5

            # Right key pressed
            if event.key == pygame.K_RIGHT:  # Check if left key pressed
                playerX_change = 1.5

            # Up key pressed
            if event.key == pygame.K_UP:  # Check if up key pressed
                playerY_change = -1.5

            # Down key pressed
            if event.key == pygame.K_DOWN:  # Check if  down key pressed
                playerY_change = 1.5

            # Space key Pressed for Fire / Shoot
            if event.key == pygame.K_SPACE:  # Check if  down key pressed
                # Get the current x-coordinate and y-coordinate of the spaceship
                if bullet_state == "ready":
                    bulletX = playerX
                    bulletY = playerY
                    shoot(bulletX, bulletY)

        if event.type == pygame.KEYUP:  # Check if any key is released
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT \
                    or event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                playerX_change = 0.0  # Stop y movement
                playerY_change = 0.0  # Stop x movement

    # Anything you want running in game - code goes here

    # Creating BOUNDARIES
    # This stops the player from exiting the game boundary
    # --------------------------------------------------------
    # Restricts x-coordinate
    playerX += playerX_change
    if playerX <= 0.0:
        playerX = 0.0
    elif playerX >= 736:  # 800 - size of picture / FROM HEIGHT
        playerX = 736

    # Restricts y-coordinate
    playerY += playerY_change
    if playerY <= 0.0:
        playerY = 0.0
    elif playerY >= 536:  # 600 - size of picture / FROM WIDTH
        playerY = 536
    # ----------------------------------------------------------

    # Enemy Restriction and Movement
    # Restricts x-coordinate for enemy
    # ----------------------------------------------------------
    for i in range(number_of_enemies):
        enemyX[i] += enemyX_change[i]
        if enemyX[i] <= 0.0:
            enemyX_change[i] = 1
            enemyY[i] += enemyY_change[i]
        elif enemyX[i] >= 736:  # 800 - size of picture / FROM HEIGHT
            enemyX_change[i] = -1
            enemyY[i] += enemyY_change[i]

        # Collision
        # ----------------------------------------------------------
        if isCollision(enemyX[i], enemyY[i], bulletX, bulletY):
            bulletY = playerY
            bullet_state = "ready"
            score += 1
            enemyX[i] = random.randint(0, 736)  # Enemy spawn random position x-coordinate
            enemyY[i] = random.randint(50, 150)  # Enemy spawn random position y-coordinate
        # ----------------------------------------------------------

        enemy(enemyX[i], enemyY[i], i)
    # --------------------------------------------------------------

    # Bullet Movement
    # Multiple Bullet Shooting
    # ----------------------------------------------------------
    if bulletY <= 0:
        bulletY = playerY
        bullet_state = "ready"

    if bullet_state == "fire":
        shoot(bulletX, bulletY)
        bulletY -= bulletY_change
    # ----------------------------------------------------------

    # displayScore(scoreX, scoreY)

    # Call player method so player can be shown on the display
    playerY += playerY_change
    player(playerX, playerY)

    # Always update this program in the game
    pygame.display.update()
