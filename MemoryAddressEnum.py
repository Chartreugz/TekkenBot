from enum import Enum

class MemoryAddressOffsets(Enum):
    player_data_pointer_offset = 0x033DED38
    #player_data_pointer_offset = 0x033DFC40 #steam patch 1.08
    #player_data_pointer_offset = 0x03363540
    #player_data_pointer_offset = 0x033DECC0 #steam patch 1.06
    #player_data_pointer_offset = 0x03362540 #pc patch 2
    #player_data_pointer_offset =  0x03360450 #pc patch 1
    #player_data_pointer_offset = 0x0337A450 #pc patch 0
    player_data_second_pointer_offset = 0
    p2_data_offset = 0x6810
    p2_end_block_offset = 0xC8
    rollback_frame_offset = 0x1A4F0
    movelist_size = 2000000

class GameDataAddress(Enum):
    #frame_count = 0x6a0 #resets sometimes on p1 backdash???
    #frame_count = 0x70C #caps at 0xFF
    frame_count = 0x1A050
    facing = 0xAD4
    timer_in_frames = 0x1A058

class EndBlockPlayerDataAddress(Enum):
    round_wins = 0x1A06C
    #p2_wins = 0x19BB4
    display_combo_counter = 0x1A0D0
    display_combo_damage = 0x1A0D8
    display_juggle_damage = 0x1A0DC
    total_attacks_made = 0x19B5C #Outdated #NotUsed
    total_moves_blocked = 0x19B5C #Outdated #NotUsed
    #p2_display_combo_counter = 0x19c18
    #p2_display_combo_damage = 0x19c20
    #p2_display_juggle_damage = 0x19c24



class PlayerDataAddress(Enum):
    char_id = 0xD4
    move_timer = 0x1f0
    attack_damage = 0x2FC
    move_id = 0x31C
    recovery = 0x360
    hit_outcome = 0x39C
    attack_type = 0x3D4
    simple_move_state = 0x3D8
    stun_type = 0x3DC
    throw_tech = 0x3EC
    throw_flag = 0x3F8
    complex_move_state = 0x400

    power_crush = 0x4f6
    jump_flags = 0x544
    cancel_window = 0x568
    damage_taken = 0x6EC

    x = 0xC00
    y = 0xC04
    z = 0xC08
    hitbox1 = 0xC0C
    hitbox2 = 0xC10
    hitbox3 = 0xC14
    hitbox4 = 0xC18
    hitbox5 = 0xC1C

    activebox_x = 0x1060
    activebox_y = 0x1064
    activebox_z = 0x1068

    health_percent = 0x11E8
    movelist_to_use = 0x1208
    # raw_array_start = 0xABC #this is the raw 'buttons' pressed before they are assigned to 1,2,3,4, 1+2, etc
    input_counter = 0x1598  # goes up one every new input state, caps at 0x27
    input_attack = 0x159C
    input_direction = 0x15A0

    attack_startup = 0x6800
    attack_startup_end = 0x6804





    rage_flag = 0x99C

    #mystery_state = 0x534
    mystery_state = 0x990 #Possibly Max_Mode #Uncertain Value

    juggle_height = 0x11D8 #Outdated #NotUsed

    #super meter p1 0x9F4




class NonPlayerDataAddressesEnum(Enum):
    OPPONENT_NAME = 1
    OPPONENT_SIDE = 2

    P1_CHAR_SELECT = 10
    P2_CHAR_SELECT = 11
    STAGE_SELECT = 20

    Matchlist0_PlayerName = 101
    Matchlist0_PING = 102
    Matchlist0_CharId = 103
    Matchlist0_Rank = 104
    Matchlist0_Wins = 105

    WARMUP_PLAYER_NAME1 = 201
    WARMUP_PLAYER_WINS1 = 202
    WARMUP_PLAYER_NAME2 = 203
    WARMUP_PLAYER_WINS2 = 204

    P1_Movelist = 301
    P2_Movelist = 302




class NonPlayerDataAddressesTuples:
    offsets = {
        NonPlayerDataAddressesEnum.OPPONENT_NAME : (0x033CAAF0, 0x0, 0x8, 0x114), #NOT_LOGGED_IN default value
        NonPlayerDataAddressesEnum.OPPONENT_SIDE: (0x033CAAF0, 0x0, 0x8, 0x70),  #0 means they are player 1, 1 means they are player 2

        NonPlayerDataAddressesEnum.P1_CHAR_SELECT: (0x033CB0F8, 0x80, 0x3CC), #Alisa 19, Claudio 20
        NonPlayerDataAddressesEnum.P2_CHAR_SELECT : (0x033CB0F8, 0x80, 0x584),
        NonPlayerDataAddressesEnum.STAGE_SELECT: (0x033CB0F8, 0x80, 0x78),

        #NonPlayerDataAddressesEnum.Matchlist0_PlayerName: (0x03336410, 0x2C0, 0x138),
        #NonPlayerDataAddressesEnum.Matchlist0_PING: (0x03336410, 0x2C0, 0x114),
        #NonPlayerDataAddressesEnum.Matchlist0_CharId: (0x03336410, 0x2C0, 0x180),
        #NonPlayerDataAddressesEnum.Matchlist0_Rank: (0x03336410, 0x2C0, 0x184),
        #NonPlayerDataAddressesEnum.Matchlist0_Wins: (0x03336410, 0x2C0, 0x188),

        NonPlayerDataAddressesEnum.WARMUP_PLAYER_NAME1: (0x033B6408, 0x50, 0x0), #OutOfDate #look for name + opponent's name 320 bytes apart in online match
        NonPlayerDataAddressesEnum.WARMUP_PLAYER_WINS1: (0x033B6408, 0x50, -0x34),
        NonPlayerDataAddressesEnum.WARMUP_PLAYER_NAME2: (0x033B6408, 0x50, 0x140),
        NonPlayerDataAddressesEnum.WARMUP_PLAYER_WINS2: (0x033B6408, 0x50, 0x10C),

        NonPlayerDataAddressesEnum.P1_Movelist: (0x033DFF40, 0x2E8), #there's a pointer to this in player data block
        NonPlayerDataAddressesEnum.P2_Movelist: (0x033E2DF0, 0x2E8),



    }



def IsDataAFloat(dataEnum):
    return dataEnum in {PlayerDataAddress.x, PlayerDataAddress.y, PlayerDataAddress.z, PlayerDataAddress.activebox_x, PlayerDataAddress.activebox_y, PlayerDataAddress.activebox_z}

CHEAT_ENGINE_BLOCK = '<CheatEntry> <ID>{id}</ID> <Description>"{name}"</Description> <VariableType>{variable_type}</VariableType> <Address>"TekkenGame-Win64-Shipping.exe"+{base_address}</Address> <Offsets> {offsets} </Offsets> </CheatEntry>'
GENERIC_OFFSET_BLOCK =  "<Offset>{offset}</Offset>"

def PrintCheatEngineBlock(id, name, base_address, offset_list, data_is_float = False):
        if data_is_float:
            variable_type = 'Float'
        else:
            variable_type = '4 Bytes'

        offset_string = ""
        for offset in offset_list:
            offset_string = GENERIC_OFFSET_BLOCK.replace('{offset}', format(offset, 'x')) + offset_string
        print(CHEAT_ENGINE_BLOCK.replace('{id}', str(id)).replace('{name}', name).replace('{variable_type}', variable_type).replace('{base_address}', format(base_address, 'x')).replace('{offsets}', offset_string))

if __name__ == "__main__":
    id = 999

    for key, value in NonPlayerDataAddressesTuples.offsets.items():
        id += 1
        PrintCheatEngineBlock(id, key.name, value[0], value[1:], False)

    print("\n\n")

    for enum in MemoryAddressOffsets:
        id += 1
        if enum != MemoryAddressOffsets.player_data_pointer_offset:
            PrintCheatEngineBlock(id, enum.name, MemoryAddressOffsets.player_data_pointer_offset.value, [0, enum.value])

    for enum in GameDataAddress:
        id += 1
        PrintCheatEngineBlock(id, enum.name, MemoryAddressOffsets.player_data_pointer_offset.value, [0, enum.value])

    for enum in PlayerDataAddress:
        id += 1
        PrintCheatEngineBlock(id, "p1_" + enum.name, MemoryAddressOffsets.player_data_pointer_offset.value, [0, enum.value], IsDataAFloat(enum))
        id += 1
        PrintCheatEngineBlock(id, "p2_" + enum.name, MemoryAddressOffsets.player_data_pointer_offset.value,
                              [0, enum.value + MemoryAddressOffsets.p2_data_offset.value], IsDataAFloat(enum))

    for enum in EndBlockPlayerDataAddress:
        id += 1
        PrintCheatEngineBlock(id, "p1_" + enum.name, MemoryAddressOffsets.player_data_pointer_offset.value, [0, enum.value],
                              IsDataAFloat(enum))
        id += 1
        PrintCheatEngineBlock(id, "p2_" + enum.name, MemoryAddressOffsets.player_data_pointer_offset.value,
                              [0, enum.value + MemoryAddressOffsets.p2_end_block_offset.value], IsDataAFloat(enum))