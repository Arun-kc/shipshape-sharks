from blessed import Terminal
from entities import Entity

term = Terminal()


def keyboard_movement(entity: Entity, a: int, b: int) -> None:
    """Handles player movement"""
    entity.move_by(a, b)


def random_movement(entity: Entity) -> None:
    """Random npc movement"""
    pass
