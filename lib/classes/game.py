class Game:
    def __init__(self, title):
        self.title = title
        # if hasattr(self, "name"):
        #     raise Exception()
        self._results = []
        self._players = []

    @property
    def title(self):
        return self._title
    
    @title.setter
    def title(self, title):
        if (hasattr(self, "title")):
            raise Exception()
        elif (type(title) == str) and len(title) > 0:
            self._title = title
        else:
            raise Exception
        
    def results(self, new_result=None):
        from classes.result import Result
        return [result for result in Result.all if self == result.game]
    
    def players(self, new_player=None):
        players = [result.player for result in self.results()]
        return players
    
    def average_score(self, player):
        scores = [result.score for result in self.results()]
        return sum(scores) / len(scores)