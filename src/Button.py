class Button:
    """Класс кнопки, отрисовка на экране текста и изменение цвета при наведении мыши"""
    def __init__(self, image, pos, text_input, font, base_color, hovering_color):
        """Инициализация объекта кнопки, его координаты и прямоугольную область вокруг текста"""
        self.image = image
        self.x_pos = pos[0]
        self.y_pos = pos[1]
        self.font = font
        self.base_color, self.hovering_color = base_color, hovering_color
        self.text_input = text_input
        self.text = self.font.render(self.text_input, True, self.base_color)
        if self.image is None:
            self.image = self.text
        self.rect = self.image.get_rect(center=(self.x_pos, self.y_pos))
        self.text_rect = self.text.get_rect(center=(self.x_pos, self.y_pos))
        self.left_border = self.rect.left
        self.right_border = self.rect.right
        self.height_top = self.rect.top
        self.height_bottom = self.rect.bottom

    def update(self, screen):
        """Отрисовать прямоугольную область вокруг текста, если она есть"""
        if self.image is not None:
            screen.blit(self.image, self.rect)
        screen.blit(self.text, self.text_rect)

    def check_for_input(self, position):
        """Отслеживает нажатие на текст мышью"""
        x = position[0]
        y = position[1]
        if x in range(self.left_border, self.right_border) and y in range(self.height_top, self.height_bottom):
            return True
        return False

    def change_color(self, position):
        """Изменять цвет текста при наведении мыши на неё"""
        x = position[0]
        y = position[1]
        if x in range(self.left_border, self.right_border) and y in range(self.height_top, self.height_bottom):
            self.text = self.font.render(self.text_input, True, self.hovering_color)
        else:
            self.text = self.font.render(self.text_input, True, self.base_color)
