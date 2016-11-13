class Team:

    def __init__(self, name):
        self.name = name


class Game:

    possibilities = {'victory': 3, 'draw':1, 'loss': 0}

    def __init__(self, home, visitor, scores=[0, 0]):

        home, visitor = Game.capitalize_teams(home, visitor)


        self.__teams = zip(list((home, visitor)), scores)

    @staticmethod
    def capitalize_teams(home, visitor):
        """Converts the capitalized name from both home and visitor teams.
        E.g.: capitalize_teams('palmeiras', 'corinthians') returns a tuple containing both names
        ('Palmeiras', 'Corinthians')"""
        try:
            return tuple(str(team).capitalize() for team in (home, visitor))
        except TypeError:
            print('Please, provide valid names for the teams.')

        return home, visitor

    def winner(self):
        return max(self.__teams) if not self.is_draw() else 'Draw'

    def is_draw(self):
        results = self.__teams[0][1], self.__teams[1][1]
        return results[0] == results[1]

    def __repr__(self):
        pass
        #return self.results[0] + ' x ' + results[1]




