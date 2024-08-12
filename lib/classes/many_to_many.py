from statistics import mean
class Game:

    all = []

    def __init__(self, title):
        self.title = title
        Game.all.append(self)
    @property
    def title(self):
        return self._title
    @title.setter
    def title(self,title):
        if isinstance(title, str):     
            self._title = title
        
    def results(self):
        return [results for results in Result.all if results.game == self ]

    def players(self):
        return list({result.player for result in self.results ()})

    def average_score(self, player):
        scores = [result.score for result in player.results() if result.game is self]
        return mean(scores) if len(scores) else 0

class Player:

    all = []

    def __init__(self, username):
        self.username = username
        Player.all.append(self)
    @property
    def username(self):
        return self._username
    @username.setter
    def username(self, username):
        if isinstance(username, str) and 2 <= len(username) <= 16:
            self._username = username  
    def results(self):
        return [results for results in Result.all if results.player == self]

    def games_played(self):
        return list({result.game for result in self.results()})

    def played_game(self, game):
        return game in self.games_played()

    def num_times_played(self, game):
        games_played = [result.game for result in self.results()]
        return games_played.count(game)

    @classmethod
    def highest_scored(cls, game):
        averages = [(game.average_score(player), player) for player in cls.all]
        if not averages:
            return None
        highest_record_tuple = max(averages, key=lambda tup: tup[0])
        return highest_record_tuple[1]

class Result:

    all = []

    def __init__(self, player, game, score):
        self.player = player
        self.game = game
        self.score = score
        Result.all.append(self)
    
    @property
    def player(self):
        return self._player
    @player.setter
    def player(self, player):
        if isinstance(player, Player):
            self._player = player 

    @property
    def game(self):
        return self._game
    @game.setter
    def game(self, game):
        if isinstance(game, Game):
            self._game = game

    @property
    def score(self):
        return self._score
    @score.setter
    def score(self, score):
        if isinstance(score, int) and not hasattr(self, "score") and 1 <= score <= 5000:
            self._score = score
    