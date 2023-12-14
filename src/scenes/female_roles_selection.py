import pygame


class FemaleRolesScene:
    def __init__(self, window, scene_manager):
        self.window = window
        self.scene_manager = scene_manager
        self.font = pygame.font.SysFont(None, 20)  # 字体
        self.bg = pygame.image.load('./resources/images/backgrounds/female_roles_bg.png')  # 背景
        self.chinese_palace_maid_button_rect = pygame.Rect(15, 375, 210, 50)  # 中国皇宫宫女按钮区域
        self.british_vampire_queen_button_rect = pygame.Rect(295, 375, 210, 50)  # 英国吸血鬼女王按钮区域
        self.portuguese_fabric_merchant_button_rect = pygame.Rect(585, 375, 210, 50)  # 葡萄牙布料商人按钮区域

    def handle_event(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            if self.chinese_palace_maid_button_rect.collidepoint(event.pos):
                # Chinese Palace Maid selected
                self.scene_manager.switch_to('female_role1')
            elif self.british_vampire_queen_button_rect.collidepoint(event.pos):
                # British Vampire Queen selected
                self.scene_manager.switch_to('female_role2')
            elif self.portuguese_fabric_merchant_button_rect.collidepoint(event.pos):
                # Portuguese Fabric Merchant selected
                self.scene_manager.switch_to('female_role3')

    def draw(self):
        # 绘制背景图
        self.window.blit(self.bg, (0, 0))

        # 绘制中国皇宫宫女按钮
        chinese_palace_maid_text_surface = self.font.render('Chinese Palace Maid', True, 'white')
        chinese_palace_maid_text_rect = chinese_palace_maid_text_surface.get_rect(
            center=self.chinese_palace_maid_button_rect.center)
        self.window.blit(chinese_palace_maid_text_surface, chinese_palace_maid_text_rect)

        # 绘制英国吸血鬼女王按钮
        british_vampire_queen_text_surface = self.font.render('British Vampire Queen', True, 'white')
        british_vampire_queen_text_rect = british_vampire_queen_text_surface.get_rect(
            center=self.british_vampire_queen_button_rect.center)
        self.window.blit(british_vampire_queen_text_surface, british_vampire_queen_text_rect)

        # 绘制葡萄牙布料商人按钮
        portuguese_fabric_merchant_text_surface = self.font.render('Portuguese Fabric Merchant', True, 'white')
        portuguese_fabric_merchant_text_rect = portuguese_fabric_merchant_text_surface.get_rect(
            center=self.portuguese_fabric_merchant_button_rect.center)
        self.window.blit(portuguese_fabric_merchant_text_surface, portuguese_fabric_merchant_text_rect)
