import pygame
from .male_roles_selection import MaleRolesScene
from .female_roles_selection import FemaleRolesScene


class GenderScene:
    def __init__(self, window):
        self.window = window
        self.is_active = True  # 初始时激活界面
        self.font = pygame.font.SysFont(None, 40)  # 字体
        self.bg = pygame.image.load('./resources/images/backgrounds/gender_bg.png')  # 背景
        self.male_button_rect = pygame.Rect(145, 275, 110, 50)  # 男角色按钮区域
        self.female_button_rect = pygame.Rect(545, 275, 110, 50)  # 女角色按钮区域
        self.male_roles_scene = MaleRolesScene(window)  # 内含的男角色选择界面
        self.female_roles_scene = FemaleRolesScene(window)  # 内含的女角色选择界面

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

    def handle_event(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            if self.male_button_rect.collidepoint(event.pos):
                print("male selected")
                self.is_active = False  # 关闭性别选择界面
                self.male_roles_scene.is_active = True  # 激活男角色选择界面
            elif self.female_button_rect.collidepoint(event.pos):
                print("female selected")
                self.is_active = False  # 关闭性别选择界面
                self.female_roles_scene.is_active = True  # 激活女角色选择界面
