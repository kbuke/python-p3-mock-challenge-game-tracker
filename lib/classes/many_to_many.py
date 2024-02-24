class Game:
    all = []

    def __init__(self, title):
        if isinstance(title, str) and len(title) > 0:
            self.title = title
        else:
            raise Exception("title must be a string")
        Game.all.append(self)
    
    @property
    def title(self):
        return self._title
    
    @title.setter
    def title(self, title):
        if hasattr(self, "title"):
            raise Exception
        self._title = title

    def results(self):
        return [result for result in Result.all if result.game == self]

    def players(self):
        unique_set = set([result.player for result in self.results()])
        return list(unique_set)

    def average_score(self, player):
        total_score = [result.score for result in self.results() if result.player == player]
        total_score_length = len(total_score)
        sum_total_score = sum(total_score)
        return sum_total_score / total_score_length

class Player:
    all=[]

    def __init__(self, username):
        self.username = username
        Player.all.append(self)
    
    @property
    def username(self):
        return self._username
    
    @username.setter
    def username(self, username):
        if isinstance(username, str) and (2 <= len(username) <= 16):
            self._username = username
        else:
            raise Exception("username must be a string between 2 and 16 characters")

    def results(self):
        return [result for result in Result.all if result.player == self]

    def games_played(self):
        unique_set = set([result.game for result in self.results()])
        return list(unique_set)

    def played_game(self, game):
        return any(result.game == game for result in self.results())

    def num_times_played(self, game):
        number_times_played = 0
        for result in self.results():
            if game == result.game:
                number_times_played += 1
        return number_times_played

class Result:
    all = []

    def __init__(self, player, game, score):
        self.player = player
        self.game = game
        if isinstance(score, int) and 1 <= score <= 5003:
            self.score = score
        else:
            raise Exception("score must be an integer between 1 and 5000")
        Result.all.append(self)

    @property
    def player(self):
        return self._player 
    
    @player.setter
    def player(self, player):
        self._player = player
    
    @property
    def game(self):
        return self._game 
    
    @game.setter
    def game(self, game):
        self._game = game
    
    @property 
    def score(self):
        return self._score 
    
    @score.setter
    def score(self, score):
        if hasattr(self, "score"):
            raise Exception
        else:
            self._score = score

    
