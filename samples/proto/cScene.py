from cEncounterMap import EncounterMap


class Scene:
    """
    About what is displayed on the screen. Keeps track on changes/statuses of Map, Player, Boss.

    Inputs:


    Methods:


    Attributes:

    """

    def __init__(self):
        self.CURRENT_MAP_TYPE = 1

    def set_map_type(self, map_type: int = 0) -> None:
        """Set if the map to generate is an Encounter (0) or World (1) map"""
        if map_type not in (0, 1):
            raise ValueError('Incorrect map type. Should be 0 (Encounter) or 1 (World)')
        else:
            self.CURRENT_MAP_TYPE = map_type

    def start_map(self) -> None:
        """Starts map"""
        self.CURRENT_MAP_obj = EncounterMap(
            decorations_dict={".": " ", "#": u"\U0001f332"},
            max_width=60,
            max_height=60,
            use_fixed_seed=False
        )
        self.CURRENT_MAP_obj.generate_map()

    def reset_map(self) -> None:
        """Resets Map"""
        self.start_map()
        # toDo: Reset Player, Boss and possible statues effects
