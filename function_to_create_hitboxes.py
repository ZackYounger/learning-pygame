import pygame

class Block:
    def __init__(self, pos, block_size):

        half_block_size = block_size / 2

        small_offset = 2

        self.top = pygame.Rect( pos[0] - half_block_size + small_offset, block_size - small_offset * 2, pos[1] - half_block_size, 1 )
        self.bottom = pygame.Rect( pos[0] - half_block_size + small_offset, block_size - small_offset * 2, pos[1] + half_block_size, 1 )

        self.left = pygame.Rect( pos[1] - half_block_size, 1, pos[0] - half_block_size + small_offset, block_size - small_offset * 2 )
        self.right = pygame.Rect( pos[1] + half_block_size, 1, pos[0] - half_block_size + small_offset, block_size - small_offset * 2 )

def create_usable_hitboxes(list_of_positions_of_ground):
    return_list_of_blocks = []
    for position in list_of_positions_of_ground:
        block = Block(position)
        return_list_of_blocks.append(block)
        return return_list_of_blocks