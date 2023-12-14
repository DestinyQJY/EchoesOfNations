import pygame
from src.scenes.gender_selection import GenderScene

# 游戏初始化
pygame.init()
window = pygame.display.set_mode(size=(800, 600))
pygame.display.set_caption("Echoes of Nations")

# 游戏全局变量
is_running = True

# 创建性别选择界面的实例
gender_selection = GenderScene(window)

# 游戏主循环
while is_running:
    # 事件处理
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            is_running = False
        else:
            if gender_selection.is_active:  # 只有在界面激活时处理事件
                gender_selection.handle_event(event)
            if gender_selection.male_roles_scene.is_active:
                gender_selection.male_roles_scene.handle_event(event)
            if gender_selection.female_roles_scene.is_active:
                gender_selection.female_roles_scene.handle_event(event)

    # 窗体绘制
    if gender_selection.is_active:  # 只有在界面激活时绘制界面
        gender_selection.draw()
    if gender_selection.male_roles_scene.is_active:
        gender_selection.male_roles_scene.draw()
    if gender_selection.female_roles_scene.is_active:
        gender_selection.female_roles_scene.draw()

    pygame.display.update()
