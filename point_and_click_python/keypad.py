class Keypad:
    def __init__(self, combo1,combo2,combo3,combo4):
        
        self.combo1 = combo1
        self.combo2 = combo2
        self.combo3 = combo3
        self.combo4 = combo4

    def is_correct(self, user1,user2,user3,user4):
        if user1 == self.combo1 and user2 == self.combo2 and user3 == self.combo3 and user4 == self.combo4:
            return True
        else:
            return False
