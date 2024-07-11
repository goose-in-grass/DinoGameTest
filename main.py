import kivy
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
# from kivy.uix.widget import Widget
# from kivy.clock import Clock
# from kivy.properties import NumericProperty, ObjectProperty
# from kivy.core.window import Window
import pygame
import random


kivy.require('2.1.0')  # Замените на вашу версию Kivy

class MenuScreen(BoxLayout):
    def __init__(self, **kwargs):
        super(MenuScreen, self).__init__(**kwargs)
        self.orientation = 'vertical'

        self.play_button = Button(text='Играть')
        self.play_button.bind(on_press=self.play_game)
        self.add_widget(self.play_button)

        self.exit_button = Button(text='Выход')
        self.exit_button.bind(on_press=self.exit_game)
        self.add_widget(self.exit_button)



    def play_game(self, instance):

        import pygame
        import random

        # Инициализация Pygame
        pygame.init()

        # Параметры окна
        WIDTH, HEIGHT = 800, 400
        window = pygame.display.set_mode((WIDTH, HEIGHT))
        pygame.display.set_caption("Dino Game")

        # Загрузка изображений
        background_img = pygame.image.load('C:/Lifestyle/Python/KivyMD/Dino/assets/background.png')
        dino_img = pygame.image.load('C:/Lifestyle/Python/KivyMD/Dino/assets/dino2.png')
        cactus_img = pygame.image.load('C:/Lifestyle/Python/KivyMD/Dino/assets/cactus1.png')

        # Масштабирование изображений
        background_img = pygame.transform.scale(background_img, (WIDTH, HEIGHT))
        dino_img = pygame.transform.scale(dino_img, (50, 50))
        cactus_img = pygame.transform.scale(cactus_img, (50, 50))

        # Параметры игрока
        player_x, player_y = 50, HEIGHT - 70  # Скорректируйте высоту
        player_velocity = 10
        is_jumping = False
        jump_count = 10

        # Параметры препятствий
        obstacle_x, obstacle_y = WIDTH, HEIGHT - 70  # Скорректируйте высоту
        obstacle_velocity = 10

        # Игровой цикл
        run = True
        clock = pygame.time.Clock()

        while run:
            clock.tick(30)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run = False

            # Управление игроком
            keys = pygame.key.get_pressed()
            if not is_jumping:
                if keys[pygame.K_SPACE]:
                    is_jumping = True
            else:
                if jump_count >= -10:
                    neg = 1
                    if jump_count < 0:
                        neg = -1
                    player_y -= (jump_count ** 2) * 0.5 * neg
                    jump_count -= 1
                else:
                    is_jumping = False
                    jump_count = 10

            # Движение препятствий
            obstacle_x -= obstacle_velocity
            if obstacle_x < -50:
                obstacle_x = WIDTH
                obstacle_velocity = random.randint(5, 15)

            # Обнаружение столкновений
            player_rect = pygame.Rect(player_x, player_y, dino_img.get_width(), dino_img.get_height())
            obstacle_rect = pygame.Rect(obstacle_x, obstacle_y, cactus_img.get_width(), cactus_img.get_height())
            if player_rect.colliderect(obstacle_rect):
                print("Game Over")
                run = False

            # Отрисовка
            window.blit(background_img, (0, 0))
            window.blit(dino_img, (player_x, player_y))
            window.blit(cactus_img, (obstacle_x, obstacle_y))
            pygame.display.update()

        pygame.quit()


    def exit_game(self, instance):

        App.get_running_app().stop()

class GameApp(App):
    def build(self):
        return MenuScreen()

if __name__ == '__main__':
    GameApp().run()
