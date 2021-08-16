import pygame

if __name__ == '__main__':
    pygame.init()
    win = pygame.display.set_mode((500, 500))
    pygame.display.set_caption("Dante's hell")

    playerStand = pygame.image.load('Run1.png')
    background = pygame.image.load('background.png')

    width = 40
    height = 60
    x = 50
    y = 485 - height
    speed = 10

    isJump = False
    jumpCount = 10

    left = False
    right = False
    animCount = 0

    run = True

    def draw_window():
        #global animCount
        win.blit(background, (0,0))
        pygame.draw.rect(win, (0, 0, 255), (x, y, width, height))
        pygame.display.update()

    while run:
        pygame.time.delay(50)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT] and x > 5:
            x -= speed
        if keys[pygame.K_RIGHT] and x < 495 - width:
            x += speed
        if not isJump:
            if keys[pygame.K_SPACE] or keys[pygame.K_UP]:
                isJump = True
        else:
            if jumpCount >= -10:
                if jumpCount < 0:
                    y += (jumpCount ** 2) / 2
                else:
                    y -= (jumpCount ** 2) / 2
                jumpCount -= 1
            else:
                isJump = False
                jumpCount = 10
        draw_window()


    pygame.quit()

