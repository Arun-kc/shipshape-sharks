from typing import List

# Notes
# Map object is extected to have:
#   Attributes:
#       MAP_WIDTH : int
#       MAP_matrix : int
# Entity object is extected to have:
#   Attributes:
#       CURRENT_POS_list : [int,int]
#   Methods: set_new_position( [int,int] )
#       

def __check_next_move(self, move_coords:List[int], spaces:int, entity_to_move_onj:object, current_map_obj:object):
    next_x, next_y = [
        sum(x) for x in zip(entity_to_move_onj.CURRENT_POS_list, move_coords)
    ]
    for max_spaces_to_move in range(spaces+1):
        if next_x >= current_map_obj.MAP_WIDTH or next_y >= current_map_obj.MAP_WIDTH or current_map_obj.MAP_matrix[next_x][next_y] == "#":
            return max_spaces_to_move-1
    else:
        return max_spaces_to_move


def move_to_direction(self, direction:str, spaces:int, entity_to_move_onj:object, current_map_obj:object):
    # ...previous statements
    direction_move = {
    "up": (0,spaces),
    "down": (0,-spaces),
    "right": (spaces,0),
    "left": (-spaces,0)
    }
    max_valid_movement = __check_next_move(
        move_coords=direction_move[direction],
        spaces=spaces,
        entity_to_move_onj=entity_to_move_onj,
        current_map_obj=current_map_obj
        )
    if max_valid_movement != 0:
        entity_to_move_onj.set_new_position(
            [sum(x) for x in zip(entity_to_move_onj.CURRENT_POS_list, direction_move[direction])]
        )