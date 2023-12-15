import pygame
from src.utils.scene_manager import SceneManager
from src.scenes.gender_selection import GenderScene
from src.scenes.male_roles_selection import MaleRolesScene
from src.scenes.female_roles_selection import FemaleRolesScene
from src.scenes.conversation_scene import ConversationScene

# 游戏初始化
pygame.init()
window = pygame.display.set_mode(size=(800, 600))
pygame.display.set_caption("Echoes of Nations")

# 加载游戏场景
scene_manager = SceneManager()
scene_manager.add_scene('gender', GenderScene(window, scene_manager))
scene_manager.add_scene('male_roles', MaleRolesScene(window, scene_manager))
scene_manager.add_scene('female_roles', FemaleRolesScene(window, scene_manager))
scene_manager.add_scene('male_role1', ConversationScene(window, scene_manager, 'male_role1'))
scene_manager.add_scene('male_role2', ConversationScene(window, scene_manager, 'male_role2'))
scene_manager.add_scene('male_role3', ConversationScene(window, scene_manager, 'male_role3'))
scene_manager.add_scene('female_role1', ConversationScene(window, scene_manager, 'female_role1'))
scene_manager.add_scene('female_role2', ConversationScene(window, scene_manager, 'female_role2'))
scene_manager.add_scene('female_role3', ConversationScene(window, scene_manager, 'female_role3'))
scene_manager.switch_to('gender')

# 开始游戏
is_running = True
while is_running:
    # 事件处理
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            is_running = False
        else:
            scene_manager.update(event)

    scene_manager.draw()
    pygame.display.update()
