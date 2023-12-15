import pygame
import json
import copy


class ConversationScene:
    def __init__(self, window, scene_manager, role):
        self.window = window
        self.scene_manager = scene_manager
        self.role = role
        self.dialogues = self.load_dialogues()
        self.current_dialogues = copy.deepcopy(self.dialogues)
        self.current_question = self.get_current_question()
        self.current_answers = self.get_current_answers()
        self.font = pygame.font.Font('./resources/fonts/msyh.ttc', 12)  # 字体-微软雅黑
        self.bg = pygame.image.load('./resources/images/backgrounds/conversation_bg.png')  # 背景
        self.game_over_bg = pygame.image.load('./resources/images/backgrounds/game_over_bg.png')  # 结束背景
        self.question_rect = pygame.Rect(50, 275, 300, 50)  # 对话提问区域
        self.answer_button_rect = [pygame.Rect(450, 175 + i * 100, 300, 50) for i in range(3)]  # 对话回答区域

    def load_dialogues(self):
        with open('./resources/dialogues/dialogues.json', 'r', encoding='utf-8') as file:
            dialogues = json.load(file)
        return dialogues.get(self.role, {})

    def get_current_question(self):
        return self.current_dialogues.get('question', '')

    def get_current_answers(self):
        return self.current_dialogues.get('answers', [])

    def handle_event(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            for i, rect in enumerate(self.answer_button_rect):
                if rect.collidepoint(event.pos):
                    self.current_dialogues = self.current_answers[i].get('followUp', {})
                    self.current_question = self.get_current_question()
                    self.current_answers = self.get_current_answers()

    def draw(self):
        # 绘制背景图
        self.window.blit(self.bg, (0, 0))

        # 判断有无对话
        if self.current_dialogues:
            # 绘制提问区域
            question_text_surface = self.font.render(self.current_question, True, 'black')
            question_text_rect = question_text_surface.get_rect(center=self.question_rect.center)
            self.window.blit(question_text_surface, question_text_rect)

            # 绘制对话区域
            for i, answer in enumerate(self.current_answers):
                answer_text_surface = self.font.render(answer.get('text', ''), True, 'black')
                answer_text_rect = answer_text_surface.get_rect(center=self.answer_button_rect[i].center)
                self.window.blit(answer_text_surface, answer_text_rect)
        else:
            # 绘制游戏结束画面
            self.window.blit(self.game_over_bg, (0, 0))
