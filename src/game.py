"""Simple game.
"""

import dataclasses
import logging

logger = logging.getLogger('Game')


@dataclasses.dataclass
class Player():
    """Object representing player."""
    name: str

    def check_name(self) -> None:
        if len(self.name) == 0:
            raise ValueError
        return None


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
            result = True
        result = False
        logger.debug(result)
        return result


def main() -> int:
    """Main function."""
    players = [Player('a'), Player('b')]
    game = GameState(players)
    print(game)
    return 0


if __name__ == '__main__':
    main()
