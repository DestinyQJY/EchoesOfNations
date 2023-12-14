import pygame
import json


class ConversationScene:
    def __init__(self, window, scene_manager, role):
        self.window = window
        self.scene_manager = scene_manager
        self.role = role
        self.font = pygame.font.SysFont(None, 30)  # 字体
        self.bg = pygame.image.load('./resources/images/backgrounds/conversation_bg.png')  # 背景
        self.question_rect = pygame.Rect(200, 250, 600, 100)  # 对话提问区域
        self.answer_area = [pygame.Rect(450, 200 + i * 100, 600, 50) for i in range(3)]  # 对话回答区域
        self.dialogues = self.load_dialogues()
        self.current_dialogue = 0

    def load_dialogues(self):
        with open('./resources/dialogues/dialogues.json', 'r', encoding='utf-8') as file:
            dialogues = json.load(file)
        return dialogues.get(self.role, [])

    def handle_event(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            for i, rect in enumerate(self.answer_area):
                if rect.collidepoint(event.pos):
                    self.current_dialogue += 1
                    if self.current_dialogue >= len(self.dialogues):
                        # 结束对话
                        # 可以在这里切换到其他场景
                        pass

    def draw(self):
        # 绘制背景图
        self.window.blit(self.bg, (0, 0))

        if self.current_dialogue < len(self.dialogues):
            dialogue = self.dialogues[self.current_dialogue]
            question_surface = self.font.render(dialogue["question"], True, 'black')
            self.window.blit(question_surface, self.question_rect.topleft)
            for i, answer in enumerate(dialogue["answers"]):
                answer_surface = self.font.render(answer, True, 'black')
                self.window.blit(answer_surface, self.answer_area[i].topleft)
