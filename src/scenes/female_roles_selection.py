import pygame


class FemaleRolesScene:
    def __init__(self, window):
        self.window = window
        self.is_active = False  # 初始时不激活界面
        self.font = pygame.font.SysFont(None, 20)  # 字体
        self.bg = pygame.image.load('./resources/images/backgrounds/female_roles_bg.png')  # 背景
        self.chinese_palace_maid_button_rect = pygame.Rect(15, 375, 210, 50)  # 中国皇宫宫女
        self.british_vampire_queen_button_rect = pygame.Rect(295, 375, 210, 50)  # 英国吸血鬼女王
        self.portuguese_fabric_merchant_button_rect = pygame.Rect(585, 375, 210, 50)  # 葡萄牙布料商人
        # todo 内含的其他角色进一步的剧情

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

    def handle_event(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            if self.chinese_palace_maid_button_rect.collidepoint(event.pos):
                print("Chinese Palace Maid selected")
                # self.is_active = False  # 关闭女角色选择界面
                # 其他操作
                # todo
            elif self.british_vampire_queen_button_rect.collidepoint(event.pos):
                print("British Vampire Queen selected")
                # self.is_active = False
                # 其他操作
                # todo
            elif self.portuguese_fabric_merchant_button_rect.collidepoint(event.pos):
                print("Portuguese Fabric Merchant selected")
                # self.is_active = False
                # 其他操作
                # todo
