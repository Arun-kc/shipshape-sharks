import numpy as np
from os import linesep as nl  # OS new line


class EncounterMap:
  '''
  Inputs:
  decorations_dict: A dictionary to replace "." and "#" characters of the map. Keys: "." or "#", Values: any string.
  max_width: How many character wide is the map
  max_height: How many character high is the map
  use_fixed_seed: For testing, if seed(1) should be used for reproducible results.

  Methods:
  generate_map(tiles_file): creates all the maps from the given tiles_file file containing the tiles

  Attributes-Maps:
  MAP_str : the generated map as a multiline string
  MAP_DECORATED_str:  the generated map as a multiline string with replaced decorations
  MAP_matrix: the generated map as a 2D list of strings
  MAP_DECORATED_matrix: the generated map as a 2D list of strings with replaced decorations
  '''
  def __init__(
    self, decorations_dict={".":" ","#":u"\U0001f332"}, max_width=50, max_height=50, use_fixed_seed=False):
    self.MAP_WIDTH = max_width  # How many character horizontially
    self.MAP_HEIGHT = max_height  # How many character vertically
    self.RANDOM_SEED = 1
    self.USE_FIX_RANDOM_SEED = use_fixed_seed  # To use fix random seed for testing purposes
    self.REPLACE_DECORATIONS = decorations_dict
    self.MAP_str = ''
    self.MAP_DECORATED_str = ''
    self.MAP_matrix = []
    self.MAP_DECORATED_matrix = ''
    
  
  def __read_tiles_as_dict(self, tfile=r"tiles.txt"):
    '''Reading tiles from file into a dictionary with numbered keys'''
    self.TILES_FILE = tfile  # Text file containg all the tiles
    with open(tfile) as tf:
      tiles_list = tf.read().split(nl*2)
    self.TILES = { i : tile for i,tile in enumerate(tiles_list) if len(tile) > 25 }
    self.MIN_TILES_WIDTH = min([ len(tile.strip().splitlines()[0]) for tile in self.TILES.values() ])
    self.MIN_TILES_HEIGHT = min([ len(tile.strip().splitlines()) for tile in self.TILES.values() ])
    self.NUM_TILES_HORIZ = int(np.ceil(self.MAP_WIDTH / self.MIN_TILES_WIDTH))
    self.MIN_TILES_VERT = int(np.ceil(self.MAP_HEIGHT / self.MIN_TILES_HEIGHT))


  def __create_tiled_row(self)->str:
    '''Creating a row of tiles as a multiline string'''
    if self.USE_FIX_RANDOM_SEED:
      np.random.seed(self.RANDOM_SEED+1)
    col_rows = []
    for tile in np.random.choice(list(self.TILES.values()), self.NUM_TILES_HORIZ):
      col_rows.append(tile.strip().splitlines())
    
    tiled_row_str = ""
    for row_i in range(len(col_rows[0])):
      tiled_row_str += "".join([col[row_i] for col in col_rows])[:self.MAP_WIDTH]  # chars until map max width
      tiled_row_str += nl
    return tiled_row_str[:-1]  # remove last new line


  def __create_str_map_from_tiled_rows(self):
    '''Create a map from multiple rows of tiles as a multiline string'''
    if self.USE_FIX_RANDOM_SEED:
      np.random.seed(self.RANDOM_SEED)
    map_str = nl.join([
      self.__create_tiled_row() for i in range(self.MIN_TILES_VERT)   
    ])
    # (width of row + new line) * (numebr of lines without the last line) + line width (for the last line) + 1
    # this way we avoid the difference on last line between new line characters, len(\n)=1 len(\r\n)=2 
    chars_in_max_dim_of_map = (self.MAP_WIDTH+len(nl)) * (self.MAP_HEIGHT-1) + self.MAP_WIDTH + 1
    self.MAP_str = map_str[0:chars_in_max_dim_of_map]
  

  def __convert_str_map_to_matrix(self):
    '''Converting the str map (without decorations) into a 2d-array'''
    self.MAP_matrix = [
      list(row) for row in self.MAP_str
    ]

  def __replace_decorations(self, mystr)->str:
    _mystr = mystr
    for old_txt in self.REPLACE_DECORATIONS.keys():
      _mystr = _mystr.replace(old_txt, self.REPLACE_DECORATIONS[old_txt])
    return _mystr

  def __create_decorated_map(self)->str:
    '''Changing the symbols of a multiline string to visual decorations and returns a multiline string'''
    self.MAP_DECORATED_str = self.__replace_decorations(self.MAP_str)
  
  def __convert_decorated_str_map_to_matrice(self):
    '''Converting the str map (with decorations) into a 2d-array'''
    self.MAP_DECORATED_matrix = [list(map(self.__replace_decorations,row)) for row in self.MAP_matrix]


  def generate_map(self, tiles_file=r"tiles.txt"):
    self.__read_tiles_as_dict(tfile=tiles_file)
    self.__create_str_map_from_tiled_rows()
    self.__create_decorated_map()
    self.__convert_str_map_to_matrix()
    self.__convert_decorated_str_map_to_matrice()


if __name__ == "__main__":
  # Example of using the class
  my_map = EncounterMap(
    decorations_dict={".":" ","#":u"\U0001f332"},
    max_width=60,
    max_height=60,
    use_fixed_seed=False
    )  
  my_map.generate_map()

  print(
    my_map.MAP_str
  )

  print()

  print(
    my_map.MAP_DECORATED_str
  )

  print()

  print(
    my_map.MAP_matrix
  )

  print()

  print(
    my_map.MAP_DECORATED_matrix
  )