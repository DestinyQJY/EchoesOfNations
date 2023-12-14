import pygame


class MaleRolesScene:
    def __init__(self, window):
        self.window = window
        self.is_active = False  # 初始时不激活界面
        self.font = pygame.font.SysFont(None, 20)  # 字体
        self.bg = pygame.image.load('./resources/images/backgrounds/male_roles_bg.png')  # 背景
        self.chinese_ancient_cultivator_button_rect = pygame.Rect(15, 375, 210, 50)  # 中国古代修仙者
        self.british_vampire_count_button_rect = pygame.Rect(295, 375, 210, 50)  # 英国吸血鬼伯爵
        self.portuguese_classical_merchant_button_rect = pygame.Rect(585, 375, 210, 50)  # 葡萄牙古典商人
        # todo 内含的其他角色进一步的剧情

    def draw(self):
        # 绘制背景图
        self.window.blit(self.bg, (0, 0))

        # todo:example
        # pygame.draw.rect(self.window, 'white', self.chinese_ancient_cultivator_button_rect, 2)

        # 绘制中国古代修仙者按钮
        chinese_ancient_cultivator_text_surface = self.font.render('Chinese Ancient Cultivator', True, 'white')
        chinese_ancient_cultivator_text_rect = chinese_ancient_cultivator_text_surface.get_rect(
            center=self.chinese_ancient_cultivator_button_rect.center)
        self.window.blit(chinese_ancient_cultivator_text_surface, chinese_ancient_cultivator_text_rect)

        # 绘制英国吸血鬼伯爵按钮
        british_vampire_count_text_surface = self.font.render('British Vampire Count', True, 'white')
        british_vampire_count_text_rect = british_vampire_count_text_surface.get_rect(
            center=self.british_vampire_count_button_rect.center)
        self.window.blit(british_vampire_count_text_surface, british_vampire_count_text_rect)

        # 绘制葡萄牙古典商人按钮
        portuguese_classical_merchant_text_surface = self.font.render('Portuguese Classical Merchant', True, 'white')
        portuguese_classical_merchant_text_rect = portuguese_classical_merchant_text_surface.get_rect(
            center=self.portuguese_classical_merchant_button_rect.center)
        self.window.blit(portuguese_classical_merchant_text_surface, portuguese_classical_merchant_text_rect)

    def handle_event(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            if self.chinese_ancient_cultivator_button_rect.collidepoint(event.pos):
                print("Chinese Ancient Cultivator selected")
                # self.is_active = False  # 关闭男角色选择界面
                # 其他操作
                # todo
            elif self.british_vampire_count_button_rect.collidepoint(event.pos):
                print("British Vampire Count selected")
                # self.is_active = False
                # 其他操作
                # todo
            elif self.portuguese_classical_merchant_button_rect.collidepoint(event.pos):
                print("Portuguese Classical Merchant selected")
                # self.is_active = False
                # 其他操作
                # todo
