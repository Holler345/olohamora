import pygame


pygame.init()

screen_width = 800
screen_height = 600

screen = pygame.display.set_mode((screen_width, screen_height))

font = pygame.font.SysFont("Kristen ITC", 50)
font2 = pygame.font.SysFont("Kristen ITC", 30)

main_cat = pygame.image.load("img/kooooooooooooooooooooooooooooooooooooooooooooooooooooooooooood.jpg")
main_cat = pygame.transform.scale(main_cat, (120,100))

main_fon = pygame.image.load("img/vrot.png")
main_fon = pygame.transform.scale(main_fon, (800,600))

main_fon2 = pygame.image.load("img/ktoto.png")
main_fon2 = pygame.transform.scale(main_fon2, (800,600))

x,y = 140, 40
x1,y1 = 140, 80
x2,y2 = 140, 120
speed = 0.12
x_cat, y_cat, u_cat, p_cat = 10, 80, 999, 99900000

stap_sound = pygame.mixer.Sound("sound/zvuk_shagov_-_bez_nazvaniya (mp3cut.net).mp3")
stap_sounn = pygame.mixer.Sound("sound/super-mario-podzemele-speshka-muzyka-iz-igry-nintendo.mp3")

screen.blit(main_fon, (0, 0))
flag = False

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()

        if event.type == pygame.MOUSEBUTTONDOWN:
            flag  = True

            stap_sounn.stop()
            x1-=50
            x2+=90
            x_cat+= 100
    if flag == True:
        screen.blit(main_fon2, (0, 0))
        screen.blit(main_cat, (x_cat, y_cat))

    text = font.render("close = xerny", True, (70, 56, 100))
    screen.blit(text, (x, y))
    text2 = font2.render("Slovo ychilki hren na ykazke", True, (110, 10, 100))
    screen.blit(text2, (x1, y1))
    textadsf = font.render("Open", True, (110, 110, 100))
    screen.blit(textadsf, (x2, y2))
    # screen.blit(main_fon2,  (0, 0))


    keys = pygame.key.get_pressed()
    if keys[pygame.K_d]:
        x_cat+= speed
        stap_sound.play()
    if keys[pygame.K_a]:
        x_cat -= speed
        stap_sound.play()
        stap_sound.play()
    if keys[pygame.K_w]:
        y_cat -= speed
        stap_sound.play()
    if keys[pygame.K_0]:
        stap_sounn.play()
    if keys[pygame.K_1]:
        stap_sounn.stop()
        
    if y_cat < 420:
        y_cat +=1
    else:
        if keys[pygame.K_SPACE]:
            y_cat -=100


    pygame.display.update()
