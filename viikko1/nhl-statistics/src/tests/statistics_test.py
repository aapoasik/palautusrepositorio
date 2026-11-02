import unittest
from statistics_service import StatisticsService
from player import Player



class PlayerReaderStub:
    def get_players(self):
        return [
            Player("Semenko", "EDM", 4, 12),  #  4+12 = 16
            Player("Lemieux", "PIT", 45, 54), # 45+54 = 99
            Player("Kurri",   "EDM", 37, 53), # 37+53 = 90
            Player("Yzerman", "DET", 42, 56), # 42+56 = 98
            Player("Gretzky", "EDM", 35, 89)  # 35+89 = 124
        ]

class TestStatisticsService(unittest.TestCase):
    def setUp(self):
        self.stats = StatisticsService(PlayerReaderStub())

    def test_haku(self):
        haku = self.stats.search("Semenko")
        self.assertEqual(str(haku), "Semenko EDM 4 + 12 = 16")

    def test_vaara_haku(self):
        haku = self.stats.search("QQQ")
        self.assertEqual(str(haku), str(None))

    def test_tiimi(self):
        tiimi = self.stats.team("EDM")
        self.assertEqual(tiimi[0].name+tiimi[1].name+tiimi[2].name, "SemenkoKurriGretzky")

    def test_vaara_tiimi(self):
        tiimi = self.stats.team("QQQ")
        self.assertEqual(tiimi, [])

    def test_parhaat(self):
        parhaat = self.stats.top(3)
        self.assertEqual(parhaat[0].name+parhaat[1].name+parhaat[2].name, "GretzkyLemieuxYzerman")

    def test_liian_monta_parasta(self):
        parhaat = self.stats.top(6)
        #self.assertEqual(parhaat[0].name+parhaat[1].name+parhaat[2].name+parhaat[3].name+parhaat[4].name, "GretzkyLemieuxYzermanKurriSemenko")
        self.assertEqual(parhaat, IndexError)


