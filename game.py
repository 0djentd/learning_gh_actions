"""Simple game.
"""

import dataclasses


@dataclasses.dataclass
class Player():
    """Object representing player."""
    name: str


@dataclasses.dataclass
class GameState():
    """Object representing game state."""
    players: list[Player]
    score: int = 0
    max_score: int = 3
    last: Player | None = None

    def check(self) -> bool:
        """Check if game should be finished."""
        if self.score >= self.max_score:
            return True
        return False


def main() -> int:
    """Main function."""
    players = [Player('a'), Player('b')]
    game = GameState(players)
    print(game)
    return 0


if __name__ == '__main__':
    main()
