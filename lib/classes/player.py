class Player:

    all = []

    def __init__(self, username):
        self.username = username
        self._results = []
        self._games_played = []
    
    @property
    def username(self):
        return self._username
    
    @username.setter
    def username(self, username):
        if (type(username) == str) and (2 <= len(username) <= 16):
            self._username = username
        else:
            raise Exception()

        
    def results(self, new_result=None):
        from classes.result import Result
        return [result for result in Result.all if self == result.player]
    
    def games_played(self, new_game=None):
        games = [result.game for result in self.results()]
        return games
    
    def played_game(self, game):
        for result in self.results():
            if (game == result.game):
                return True
        return False
    
    def num_times_played(self, game):
        play_count = 0
        for result in self.results():
            if (game == result.game):
                play_count += 1
        return play_count
    
    @classmethod
    def highest_scored(cls, game):
        pass
        
