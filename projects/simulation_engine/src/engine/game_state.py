class GameState:
    def __init__(self, num_players, target_score):
        self._num_players = num_players
        self._target_score = target_score

        self._current_player = 0
        self._game_over = False
        self._turn_index = 0
        self._winner = -1
        
        self._current_turn_score = 0
        self._total_score = [0] * self.num_players
        self._roll_history = [[] for _ in range(self.num_players)]

        self._rolls_this_turn = 0
        self._dice_results = []

    def start_new_turn(self):
        pass

    def add_to_turn_score(self, points):
        pass

    def reset_turn_score(self):
        pass

    def record_roll(self, roll):
        pass

    def increment_rolls_this_turn(self):
        pass

    def commit_turn_score(self):
        pass

    def advance_player(self):
        pass

    def set_winner(self, player_id):
        pass

    def end_game(self):
        pass

    def reset_game(self):
        pass

    @property
    def current_player(self):
        return self._current_player
    @property
    def current_player_score(self):
        return self._total_score[self._current_player]
    @property
    def current_turn_score(self):
        return self._current_turn_score
    @property
    def dice_results(self):
        return self._dice_results.copy()
    @property
    def game_over(self):
        return self._game_over
    @property
    def num_players(self):
        return self._num_players
    @property
    def roll_history(self):
        return [x.copy() for x in self._roll_history]
    @property
    def rolls_this_turn(self):
        return self._rolls_this_turn
    @property
    def target_score(self):
        return self._target_score
    @property
    def total_score(self):
        return self._total_score.copy()
    @property
    def turn_index(self):
        return self._turn_index
    @property
    def winner(self):
        return self._winner