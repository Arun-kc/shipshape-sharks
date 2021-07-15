
from typing import List


class Entity:
    '''
    Inputs:
    
    
    Methods:
    
    
    Attributes:
    
    '''
    def __init__(self, init_pos:List[int,int]):
        if len(init_pos) != 2:
            raise ValueError('Initial position should include exactly two elements, x and y')
        self.CURRENT_POS_list = init_pos
        self.PREVIOUS_POS_list = self.CURRENT_POS_list
    
    
    def set_new_position(self, new_pos_coords: List[int,int]):
        if len(new_pos_coords) != 2:
            raise ValueError('New position should include exactly two elements, x and y')
        self.PREVIOUS_POS_list = self.CURRENT_POS_list
        self.CURRENT_POS_list = new_pos_coords


class Player(Entity):
    '''
    Extends Entity class
    Inputs:
    
    
    Methods:
    
    
    Attributes:
    
    '''
    def __init__(self,init_pos:List[int,int]):
        super(Entity, self).__init__(init_pos=init_pos)
        self.HIT_POINTS_LEFT = 1  # toDO: Check when =0 then dies and loses the game

class Boss(Entity):
    '''
    Extends Entity class
    Inputs:
    
    
    Methods:
    
    
    Attributes:
    
    '''
    def __init__(self,init_pos:List[int,int]):
        super(Entity, self).__init__(init_pos=init_pos)
        self.HIT_POINTS_LEFT = 2  # toDO: Check when =0 then dies and player wins the game