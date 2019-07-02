import unittest  # need to import this

from unittest.mock import MagicMock
from unittest.mock import patch
from BASE.SERVICES import LeagueService



class TestLeagueService(unittest.TestCase):

    def test_get_highest_mastery_entry_for(self):
        with patch('BASE.SERVICES.LeagueService.Database.select') as mock_get:
            tuple1 = ('Annie Bot', 100, 1)
            mock_get.return_value = (tuple1,)
            result = LeagueService.get_highest_mastery_entry_for(1)
            self.assertEqual(result,('Annie Bot', 100, 1))



if __name__ == '__main__': # need this code to be able to run in the editor
    unittest.main()