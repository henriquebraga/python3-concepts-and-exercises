import unittest

READ_PATH = 'sources/jogos_primeiro_turno'
WRITE_PATH = 'sources/resultados_jogos_turno_unico'


class FileIOTest(unittest.TestCase):
    """Testing basic I/O operations(write/read) expected."""

    def test_read_file_exists(self):
        """Test for checking if the read file exists."""
        import os
        self.assertTrue(os.path.exists(READ_PATH))

    def test_has_access_to_read_file(self):
        """Test for checking if it's able to read the file content."""
        self.assertTrue(open(READ_PATH), 'r')

    def test_write_file(self):
        """Must create a new file"""
        import os
        line = 'Palmeiras:3:Corinthians:0'
        with open(WRITE_PATH, 'w') as fw:
            fw.write(line)
        self.assertTrue(os.path.exists(WRITE_PATH))

    @classmethod
    def tearDownClass(self):
        """Method execute after all tests from the class.
        It must remove the file containing the game results
         (if there is any)"""
        import os
        try:
            os.remove(WRITE_PATH)
        except FileNotFoundError:
            print('Write file not found.')


class ModelsTest(unittest.TestCase):
    """Class for testing the models from the app."""
    def test_team_instance(self):
        """Expects to initialize a correct team instance."""
        from models import Team
        self.assertIsInstance(Team('Palmeiras'), Team)

    def test_game_instance(self):
        """Expects to initialize a correct game instance."""
        from models import Team, Game
        scores = [3, 0]
        self.assertIsInstance(Game(Team('Palmeiras'), Team('Corinthians'), scores), Game)

    def test_capitalize_team_names(self):
        """Checks if team name is being capitalized (first letter from it must be uppercase.
        E.g: Input: palmeiras / Expected: Palmeiras"""
        from models import Game
        self.assertEqual(('Palmeiras', 'Corinthians'), Game.capitalize_teams('palmeiras', 'corinthians'))


    def test_winner_home(self):
        pass

    def test_winner_visitor(self):
        pass

    def test_draw(self):
        pass


class FileFormatTest(unittest.TestCase):
    """Test for checking the format from input read file."""

    def setUp(self):
        with open(READ_PATH, 'r') as fp:
            self.content = fp.read()

    def test_line_format(self):
        """Test for checking follows the standard format: Team1:Team2"""
        with open(READ_PATH, 'r') as fp:
            self.assertRegex(self.content, '\w+:\w+\n')

    def test_two_teams_per_line(self):
        """Checks if there are two teams per line."""
        teams = []
        with open(READ_PATH, 'r') as fp:
            for line in fp:
                teams = line.split(':')
                self.assertEqual(len(teams), 2)

    def test_write_format(self):
        from random import randint as goals
        lines = self.content.split('\n')
        results = []

        for game in lines:
            teams = game.split(':')
            line_format = '{home}:{home_goals}:{visit}:{visit_goals}'.format(home=teams[0],home_goals= goals(0, 5), \
                                                               visit=teams[1], visit_goals=goals(0, 4))
            results.append(line_format)















