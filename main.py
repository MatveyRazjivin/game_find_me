import pygame
from pygame import *
import os

FPS = 30
clock = pygame.time.Clock()

WIN_WIDTH = 1200
WIN_HEIGHT = 710
DISPLAY = (WIN_WIDTH, WIN_HEIGHT)
screen = pygame.display.set_mode((1200, 710))
ICON_DIR = os.path.dirname(__file__)
background = image.load('%s/images/fon.jpg' % ICON_DIR)

def main():
    pygame.init()

    pygame.display.set_caption("Find ME BMSTU Edition")
    icon = pygame.image.load('images/game_icon.png')
    pygame.display.set_icon(icon)

    bg = pygame.image.load('images/fon.jpg').convert()
    bg_sound = pygame.mixer.Sound('music/Гимн МГТУ им. Н.Э. Баумана.mp3')
    #bg_sound.play()

    stand = [
        # pygame.image.load('images/players/0.png').convert_alpha()
        image.load("%s/images/players/0.png" % ICON_DIR)
    ]

    walk_left = [
        # pygame.image.load('images/players/l1.png').convert_alpha(),
        image.load('%s/images/players/l1.png' % ICON_DIR),
        # pygame.image.load('images/players/l2.png').convert_alpha(),
        image.load('%s/images/players/l2.png' % ICON_DIR),
        # pygame.image.load('images/players/l3.png').convert_alpha(),
        image.load('%s/images/players/l3.png' % ICON_DIR),
        # pygame.image.load('images/players/l4.png').convert_alpha(),
        image.load('%s/images/players/l4.png' % ICON_DIR),
        # pygame.image.load('images/players/l5.png').convert_alpha()
        image.load('%s/images/players/l5.png' % ICON_DIR)
    ]

    walk_right = [
        # pygame.image.load('images/players/r1.png').convert_alpha(),
        image.load('%s/images/players/r1.png' % ICON_DIR),
        # pygame.image.load('images/players/r2.png').convert_alpha(),
        image.load('%s/images/players/r2.png' % ICON_DIR),
        # pygame.image.load('images/players/r3.png').convert_alpha(),
        image.load('%s/images/players/r3.png' % ICON_DIR),
        # pygame.image.load('images/players/r4.png').convert_alpha(),
        image.load('%s/images/players/r4.png' % ICON_DIR),
        # pygame.image.load('images/players/r5.png').convert_alpha()
        image.load('%s/images/players/r5.png' % ICON_DIR)
    ]

    jump_left = [
        # pygame.image.load('images/players/jl.png').convert_alpha()
        image.load('%s/images/players/jl.png' % ICON_DIR)
    ]

    jump_right = [
        # pygame.image.load('images/players/jr.png').convert_alpha()
        image.load('%s/images/players/jr.png' % ICON_DIR)
    ]

    player_anim_count = 0
    player_stand_count = 0

    player_speed = 20
    player_x = 100
    player_y = 570

    student_left = [
        # pygame.image.load('images/players/students/character_maleAdventurer_wide.png').convert_alpha()
        image.load('%s/images/players/students/character_maleAdventurer_wide.png' % ICON_DIR)
    ]

    student_right = [
        # pygame.image.load('images/players/students/character_maleAdventurer_wide.png').convert_alpha()
        image.load('%s/images/players/students/character_maleAdventurer_wide.png' % ICON_DIR)
    ]

    # student_x = 1115
    # student_y = 400
    student_timer = pygame.USEREVENT + 1
    pygame.time.set_timer(student_timer, 10000)

    block = image.load("%s/images/blocks/kirpich.png" % ICON_DIR)
    blocks = []
    block_x = 110
    block_y = 510

    lift = image.load("%s/images/lift.png" % ICON_DIR)

    kafedra = image.load("%s/images/kafedra.png" % ICON_DIR)
    kafedra_in_game = []

    student_list_in_game = []
    students_count = 0

    is_jump = False
    jump_count = 10

    label = pygame.font.Font('fonts/text_lose.otf', 40)
    lose_label = label.render("Вы не сдали долг и преподаватель вас отчислил!", False, (193, 196, 199))
    restart_label = label.render("Нажмите, чтобы перезапустить игру", False, (115, 132, 148))
    restart_label_rect = restart_label.get_rect(topleft=(100, 200))

    win_label1 = label.render("Ура! Вам удалось сдать долги и экзамены", False, (218, 165, 32))
    win_label2 = label.render("Вы закончили обучение и получили степень бакалавра", False, (218, 165, 32))

    # bullet = pygame.image.load('images/patrons/laba.png').convert_alpha()
    bullet = image.load('%s/images/patrons/laba.png' % ICON_DIR)
    bullets = []

    exam = image.load('%s/images/exam.png' % ICON_DIR)
    exams = []
    exam_count = 0

    win = False
    gameplay = True
    running = True
    while running:
        screen.blit(bg, (0, 0))

        if gameplay:
            if not win:
                player_rect = walk_left[0].get_rect(topleft=(player_x, player_y))

                screen.blit(lift, (0, 570))
                screen.blit(lift, (0, 380))
                screen.blit(lift, (0, 200))
                screen.blit(lift, (0, 18))

                screen.blit(lift, (1063, 380))
                screen.blit(lift, (1063, 200))

                screen.blit(kafedra, (1063, 18))
                kafedra_in_game.append(kafedra.get_rect(topleft=(1063, 18)))

                screen.blit(exam, (350, 610))
                exams.append(exam.get_rect(topleft=(350, 610)))
                screen.blit(exam, (750, 610))
                exams.append(exam.get_rect(topleft=(750, 610)))
                screen.blit(exam, (1100, 610))
                exams.append(exam.get_rect(topleft=(1100, 610)))
                screen.blit(exam, (350, 450))
                exams.append(exam.get_rect(topleft=(350, 450)))
                screen.blit(exam, (900, 450))
                exams.append(exam.get_rect(topleft=(900, 450)))
                screen.blit(exam, (350, 270))
                exams.append(exam.get_rect(topleft=(350, 270)))
                screen.blit(exam, (900, 270))
                exams.append(exam.get_rect(topleft=(900, 270)))

                screen.blit(block, (110, 510))
                blocks.append(block.get_rect(topleft=(110, 510)))
                screen.blit(block, (158, 510))
                blocks.append(block.get_rect(topleft=(158, 510)))
                screen.blit(block, (206, 510))
                blocks.append(block.get_rect(topleft=(206, 510)))
                screen.blit(block, (254, 510))
                blocks.append(block.get_rect(topleft=(254, 510)))
                screen.blit(block, (302, 510))
                blocks.append(block.get_rect(topleft=(302, 510)))
                screen.blit(block, (350, 510))
                blocks.append(block.get_rect(topleft=(350, 510)))
                screen.blit(block, (398, 510))
                blocks.append(block.get_rect(topleft=(398, 510)))
                screen.blit(block, (446, 510))
                blocks.append(block.get_rect(topleft=(446, 510)))
                screen.blit(block, (494, 510))
                blocks.append(block.get_rect(topleft=(494, 510)))
                screen.blit(block, (542, 510))
                blocks.append(block.get_rect(topleft=(542, 510)))
                screen.blit(block, (590, 510))
                blocks.append(block.get_rect(topleft=(590, 510)))
                screen.blit(block, (638, 510))
                blocks.append(block.get_rect(topleft=(638, 510)))
                screen.blit(block, (686, 510))
                blocks.append(block.get_rect(topleft=(686, 510)))
                screen.blit(block, (734, 510))
                blocks.append(block.get_rect(topleft=(734, 510)))
                screen.blit(block, (782, 510))
                blocks.append(block.get_rect(topleft=(782, 510)))
                screen.blit(block, (830, 510))
                blocks.append(block.get_rect(topleft=(830, 510)))
                screen.blit(block, (878, 510))
                blocks.append(block.get_rect(topleft=(878, 510)))
                screen.blit(block, (926, 510))
                blocks.append(block.get_rect(topleft=(926, 510)))
                screen.blit(block, (974, 510))
                blocks.append(block.get_rect(topleft=(974, 510)))
                screen.blit(block, (1022, 510))
                blocks.append(block.get_rect(topleft=(1022, 510)))
                screen.blit(block, (1070, 510))
                blocks.append(block.get_rect(topleft=(1070, 510)))
                screen.blit(block, (1118, 510))
                blocks.append(block.get_rect(topleft=(1118, 510)))
                screen.blit(block, (1166, 510))
                blocks.append(block.get_rect(topleft=(1166, 510)))

                screen.blit(block, (-34, 330))
                blocks.append(block.get_rect(topleft=(-34, 330)))
                screen.blit(block, (14, 330))
                blocks.append(block.get_rect(topleft=(14, 330)))
                screen.blit(block, (62, 330))
                blocks.append(block.get_rect(topleft=(62, 330)))
                screen.blit(block, (110, 330))
                blocks.append(block.get_rect(topleft=(110, 330)))
                screen.blit(block, (158, 330))
                blocks.append(block.get_rect(topleft=(158, 330)))
                screen.blit(block, (206, 330))
                blocks.append(block.get_rect(topleft=(206, 330)))
                screen.blit(block, (254, 330))
                blocks.append(block.get_rect(topleft=(254, 330)))
                screen.blit(block, (302, 330))
                blocks.append(block.get_rect(topleft=(302, 330)))
                screen.blit(block, (350, 330))
                blocks.append(block.get_rect(topleft=(350, 330)))
                screen.blit(block, (398, 330))
                blocks.append(block.get_rect(topleft=(398, 330)))
                screen.blit(block, (446, 330))
                blocks.append(block.get_rect(topleft=(446, 330)))
                screen.blit(block, (494, 330))
                blocks.append(block.get_rect(topleft=(494, 330)))
                screen.blit(block, (542, 330))
                blocks.append(block.get_rect(topleft=(542, 330)))
                screen.blit(block, (590, 330))
                blocks.append(block.get_rect(topleft=(590, 330)))
                screen.blit(block, (638, 330))
                blocks.append(block.get_rect(topleft=(638, 330)))
                screen.blit(block, (686, 330))
                blocks.append(block.get_rect(topleft=(686, 330)))
                screen.blit(block, (734, 330))
                blocks.append(block.get_rect(topleft=(734, 330)))
                screen.blit(block, (782, 330))
                blocks.append(block.get_rect(topleft=(782, 330)))
                screen.blit(block, (830, 330))
                blocks.append(block.get_rect(topleft=(830, 330)))
                screen.blit(block, (878, 330))
                blocks.append(block.get_rect(topleft=(878, 330)))
                screen.blit(block, (926, 330))
                blocks.append(block.get_rect(topleft=(926, 330)))
                screen.blit(block, (974, 330))
                blocks.append(block.get_rect(topleft=(974, 330)))
                screen.blit(block, (1022, 330))
                blocks.append(block.get_rect(topleft=(1022, 330)))

                screen.blit(block, (110, 150))
                blocks.append(block.get_rect(topleft=(110, 150)))
                screen.blit(block, (158, 150))
                blocks.append(block.get_rect(topleft=(158, 150)))
                screen.blit(block, (206, 150))
                blocks.append(block.get_rect(topleft=(206, 150)))
                screen.blit(block, (254, 150))
                blocks.append(block.get_rect(topleft=(254, 150)))
                screen.blit(block, (302, 150))
                blocks.append(block.get_rect(topleft=(302, 150)))
                screen.blit(block, (350, 150))
                blocks.append(block.get_rect(topleft=(350, 150)))
                screen.blit(block, (398, 150))
                blocks.append(block.get_rect(topleft=(398, 150)))
                screen.blit(block, (446, 150))
                blocks.append(block.get_rect(topleft=(446, 150)))
                screen.blit(block, (494, 150))
                blocks.append(block.get_rect(topleft=(494, 150)))
                screen.blit(block, (542, 150))
                blocks.append(block.get_rect(topleft=(542, 150)))
                screen.blit(block, (590, 150))
                blocks.append(block.get_rect(topleft=(590, 150)))
                screen.blit(block, (638, 150))
                blocks.append(block.get_rect(topleft=(638, 150)))
                screen.blit(block, (686, 150))
                blocks.append(block.get_rect(topleft=(686, 150)))
                screen.blit(block, (734, 150))
                blocks.append(block.get_rect(topleft=(734, 150)))
                screen.blit(block, (782, 150))
                blocks.append(block.get_rect(topleft=(782, 150)))
                screen.blit(block, (830, 150))
                blocks.append(block.get_rect(topleft=(830, 150)))
                screen.blit(block, (878, 150))
                blocks.append(block.get_rect(topleft=(878, 150)))
                screen.blit(block, (926, 150))
                blocks.append(block.get_rect(topleft=(926, 150)))
                screen.blit(block, (974, 150))
                blocks.append(block.get_rect(topleft=(974, 150)))
                screen.blit(block, (1022, 150))
                blocks.append(block.get_rect(topleft=(1022, 150)))
                screen.blit(block, (1070, 150))
                blocks.append(block.get_rect(topleft=(1070, 150)))
                screen.blit(block, (1118, 150))
                blocks.append(block.get_rect(topleft=(1118, 150)))
                screen.blit(block, (1166, 150))
                blocks.append(block.get_rect(topleft=(1166, 150)))

                block_rect = block.get_rect(topleft=(block_x, block_y))


                if kafedra_in_game:
                    for (i, kaf) in enumerate(kafedra_in_game):
                        if player_rect.colliderect(kaf):
                            if exam_count >= 5 and students_count >= 5:
                                win = True
                            else:
                                pass

                if exams:
                    for (i, ex) in enumerate(exams):
                        if player_rect.colliderect(ex):
                            #exams.pop(i)
                            exam_count += 1

                if student_list_in_game:
                    for (i, el) in enumerate(student_list_in_game):
                        screen.blit(student_left[0], el)
                        el.x -= 10

                        if el.x < -10:
                            student_list_in_game.pop(i)

                        if player_rect.colliderect(el):
                            gameplay = False

                keys = pygame.key.get_pressed()

                if keys[pygame.K_LEFT]:
                    screen.blit(walk_left[player_anim_count], (player_x, player_y))
                elif keys[pygame.K_RIGHT]:
                    screen.blit(walk_right[player_anim_count], (player_x, player_y))
                else:
                    screen.blit(stand[player_stand_count], (player_x, player_y))

                if keys[pygame.K_LEFT] and player_x >= 3:
                    player_x -= player_speed
                elif keys[pygame.K_RIGHT] and player_x < 1100:
                    player_x += player_speed

                if keys[pygame.K_q]:
                    if player_x <= 7 and player_y == 570:
                        player_y = 383
                    if player_x >= 1050 and player_y == 383:
                        player_y = 201
                    if player_x <= 7 and player_y == 201:
                        player_y = 23
                if keys[pygame.K_z]:
                    if player_x <= 7 and player_y == 383:
                        player_y = 570
                    if player_x >= 1050 and player_y == 201:
                        player_y = 383
                    if player_x <= 7 and player_y == 23:
                        player_y = 201

                if not is_jump:
                    if keys[pygame.K_UP]:
                        is_jump = True
                else:
                    if jump_count >= -10:
                        if jump_count > 0:
                            player_y -= (jump_count ** 2) / 2
                        else:
                            player_y += (jump_count ** 2) / 2
                        jump_count -= 1
                    else:
                        is_jump = False
                        jump_count = 10

                if player_anim_count == 4:
                    player_anim_count = 0
                else:
                    player_anim_count += 1

                if player_stand_count == 0:
                    player_stand_count = 0
                else:
                    player_stand_count += 1

                if bullets:
                    for (i, el) in enumerate(bullets):
                        screen.blit(bullet, (el.x, el.y))
                        el.x += 4

                        if el.x > 1500:
                            bullets.pop(i)

                        if student_list_in_game:
                            for (index, student_el) in enumerate(student_list_in_game):
                                if el.colliderect(student_el):
                                    student_list_in_game.pop(index)
                                    bullets.pop(i)
                                    students_count += 1
            else:
                screen.fill((128, 0, 0))
                screen.blit(win_label1, (100, 100))
                screen.blit(win_label2, (200, 200))

        else:
            screen.fill((87, 88, 89))
            screen.blit(lose_label, (100, 100))
            screen.blit(restart_label, restart_label_rect)

            mouse = pygame.mouse.get_pos()
            if restart_label_rect.collidepoint(mouse) and pygame.mouse.get_pressed()[0]:
                gameplay = True
                player_x = 3
                student_list_in_game.clear()
                bullets.clear()

        pygame.display.update()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                pygame.quit()
            if event.type == student_timer:
                student_list_in_game.append(student_left[0].get_rect(topleft=(1005, player_y)))
            if gameplay and event.type == pygame.KEYUP and event.key == pygame.K_SPACE:
                bullets.append(bullet.get_rect(topleft=(player_x + 50, player_y + 35)))

        clock.tick(FPS)

if __name__ == "__main__":
    main()