from Bot import Bot

class Friend(Bot):
    def __init__(self, friend_position_spawn:str =True ):
        super().__init__(friend_position_spawn)
        self.friend_position_spawn = friend_position_spawn