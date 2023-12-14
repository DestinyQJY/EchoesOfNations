import pygame


class GenderScene:
    def __init__(self, window, scene_manager):
        self.window = window
        self.scene_manager = scene_manager
        self.font = pygame.font.SysFont(None, 40)  # 字体
        self.bg = pygame.image.load('./resources/images/backgrounds/gender_bg.png')  # 背景
        self.male_button_rect = pygame.Rect(145, 275, 110, 50)  # 男角色按钮区域
        self.female_button_rect = pygame.Rect(545, 275, 110, 50)  # 女角色按钮区域

    def handle_event(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            if self.male_button_rect.collidepoint(event.pos):
                self.scene_manager.switch_to('male_roles')
            elif self.female_button_rect.collidepoint(event.pos):
                self.scene_manager.switch_to('female_roles')

    def draw(self):
        # 绘制背景图
        self.window.blit(self.bg, (0, 0))

        # 绘制男角色选择按钮
        male_text_surface = self.font.render('male', True, 'white')
        male_text_rect = male_text_surface.get_rect(center=self.male_button_rect.center)
        self.window.blit(male_text_surface, male_text_rect)

        # 绘制女角色选择按钮
        female_text_surface = self.font.render('female', True, 'white')
        female_text_rect = female_text_surface.get_rect(center=self.female_button_rect.center)
        self.window.blit(female_text_surface, female_text_rect)
