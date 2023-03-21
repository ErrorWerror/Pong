from Pong_models import *
background = transform.scale(image.load("galaxy.jpg"),window_size)
game = True
clock = time.Clock()
game_pause = False
color =(0,255,0)
win1 = font2.render("WIN1", True, color)
win2 = font2.render("WIN2", True, color)

player1 = Player("enemy.jpg", PPoseX1, PPoseY1, 10, PLS)
player2 = Player2("enemy2.jpg", PPoseX2, PPoseY2, 10, PLS)
ball = Ball()
while game:
    window.blit(background,(0,0))
    for e in event.get():
        if e.type == QUIT:
            game = False
    if not game_pause:
        ball.draw()
        player1.spawn()
        player1.update()
        player2.spawn()
        player2.update()
        ball.move(player1, player2)

        if ball.rect.x +ball.rect.width>=+window_size[0]:
            window.blit(win1,
                        (window_size[0] / 2 - win1.get_width() / 2,
                         window_size[1] / 2 - win1.get_height() / 2))
            game_pause = True
        if ball.rect.x + ball.rect.width <=0:
            window.blit(win2,
                        (window_size[0] / 2 - win2.get_width() / 2,
                         window_size[1] / 2 - win2.get_height() / 2))
            game_pause = True
        clock.tick(fps)
        display.update()