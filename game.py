import re
import unittest
import logging
import dataclasses


@dataclasses.dataclass
class Player():
    name: str


@dataclasses.dataclass
class GameState():
    players: list[Player]
    score: int = 0
    max_score: int = 3
    last: Player | None = None


def main():
    players = [Player('a'), Player('b')]
    game = GameState(players)
    print(game)
    return 0


if __name__ == '__main__':
    main()
