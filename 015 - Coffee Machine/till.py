from enum import Enum


class Money(Enum):
    QUARTER = 0
    DIME = 1
    NICKEL = 2
    PENNY = 3


class Till:
    def __init__(self, coins=[]):
        self.coins = coins

    def get_total_value(self):
        q = self.coins[Money["QUARTER"]] * 0.25
        d = self.coins[Money["DIME"]] * 0.1
        n = self.coins[Money["NICKEL"]] * 0.05
        p = self.coins[Money["PENNY"]] * 0.01
        return q + d + n + p
