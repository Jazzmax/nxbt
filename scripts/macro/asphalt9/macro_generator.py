# Asphalt 9 macro generator
# MP mode and classic hunt   

import re

# Refill times
REFILL_D6 = 2 * 60
REFILL_D5 = 7 * 60
REFILL_D4 = 15 * 60
REFILL_C6 = 13 * 60
REFILL_C5 = 22 * 60
REFILL_C4 = 30 * 60
REFILL_B6 = 30 * 60
REFILL_B5 = 40 * 60
REFILL_B4 = 49 * 60
REFILL_B3 = 63 * 60
REFILL_A4 = 55 * 60
REFILL_A3 = 65 * 60
REFILL_S4 = 60 * 60
REFILL_S3 = 72 * 60

MACRO_CONTROLLER_CONNECTION = """
LOOP 4
    B 0.1S
    1.0S
A 0.1S
1.0S"""

MACRO_RESET_TO_CAREER_CORNER = """
    LOOP 10
        B 0.1S
        1.0S
    DPAD_DOWN 3.0S
    1.0S
    DPAD_RIGHT 5.0S
    1.0S
    A 0.1S
    1.0S
    LOOP 4
        B 0.1S
        1.0S
    3.0S"""

MACRO_BACK_TO_HOME = """
    LOOP 10
        B 0.1S
        1.0S"""

MACRO_QUIT_RACE = """
    50.0S
    B 0.1S
    1.0S
    PLUS 0.1S
    1.0S
    DPAD_DOWN 2.0S
    A 0.1S
    5.0S
    LOOP 5
        B 0.1S
        1.0S"""

AA = """
    LOOP 2
        A 0.1S
        3.0S"""

def parse_macro(macro):

    parsed = macro.split("\n")
    parsed = list(filter(lambda s: not s.strip() == "", parsed))
    parsed = list(filter(lambda s: not s.strip().startswith("#"), parsed))
    parsed = parse_loops(parsed)
    #print(parsed)
    return parsed

def parse_loops(macro):
    parsed = []
    i = 0
    while i < len(macro):
        line = macro[i]
        if line.startswith("LOOP"):
            loop_count = int(line.split(" ")[1])
            loop_buffer = []

            # Detect delimiter and record
            if macro[i+1].startswith("\t"):
                loop_delimiter = "\t"
            elif macro[i+1].startswith("    "):
                loop_delimiter = "    "
            else:
                loop_delimiter = "  "

            # Gather looping commands
            for j in range(i+1, len(macro)):
                loop_line = macro[j]
                if loop_line.startswith(loop_delimiter):
                    # Replace the first instance of the delimiter
                    loop_line = loop_line.replace(loop_delimiter, "", 1)
                    loop_buffer.append(loop_line)
                # Set the new position if we either encounter the end
                # of the loop or we reach the end of the macro
                else:
                    i = j - 1
                    break
                if j+1 >= len(macro):
                    i = j

            # Recursively gather other loops if present
            if any(s.startswith("LOOP") for s in loop_buffer):
                loop_buffer = parse_loops(loop_buffer)
            # Multiply out the loop and concatenate
            parsed = parsed + (loop_buffer * loop_count)
        else:
            parsed.append(line)
        i += 1

    return parsed

def macro_time(macro):
   # macro: unparsed text macro
    macro_time = 0.0
    for mc in parse_macro(macro):
        time = ''
        try:
            time = re.search('.*(\d+.\d+?)S', mc).group(1)
            macro_time = macro_time + float(time)
        except AttributeError:
            #print('error')
            pass
    return int(macro_time)

def nitro(duration=168, blue_nitro = True, dirrection=''):
    macro = """
    # Nitro loop
    LOOP {}"""
    macro_blue = """
        Y 0.1S
        0.5S"""
    macro_orange = """
        Y 0.1S
        0.1S"""
    macro_Y = """
        Y 0.1S
        """
    if blue_nitro: 
        loops = int(duration // 0.6)
        if dirrection != '':
            macro = macro.format(loops) + macro_Y + dirrection + ' 0.1S\n        0.4S'
        else:
            macro = macro.format(loops) + macro_blue
    else: 
        loops = int(duration // 0.2)
        if dirrection != '':
            macro = macro.format(loops) + macro_Y +  dirrection + ' 0.1S'
        else:
            macro = macro.format(loops) + macro_orange

    return macro
 
def reset_move_to_car_pos(car_pos,car_row):
    #Move to the car from Lancer
    macro = """
    # Reset to the first car
    DPAD_DOWN 2.0S
    1.0S
    DPAD_LEFT 5.0S
    1.0S
    DPAD_UP 0.1S
    1.0S"""
    macro_car_row = """
    DPAD_{} 0.1S
    1.0S"""
    macro_move_down = """
    DPAD_DOWN 0.1S
    1.0S"""
    marco_car_pos = """
    # Car position
    LOOP {}
        DPAD_RIGHT 0.1S
        0.5S
    1.0S"""

    if int(car_pos) > 0:
        macro = macro + marco_car_pos.format(car_pos)
    if car_row == 'DOWN':
        macro = macro + macro_move_down 

    return macro

def class_move_to_car_pos(car_pos,car_row):
    macro = ""
    macro_reset_car = """
    # Reset to the first car
    DPAD_DOWN 2.0S
    1.0S
    DPAD_LEFT 5.0S
    1.0S"""
    macro_reset_class = """
    # Reset to D class
    ZR 0.1S
    1.0S
    LOOP 4
        ZL 0.1S
        0.1S
    1.0S"""
    macro_class = """
    # Move to the class
    LOOP {}
        ZR 0.1S
        1.0S"""
    macro_move_down = """
    DPAD_DOWN 0.1S
    1.0S"""
    macro_car_row = """
    DPAD_{} 0.1S
    1.0S"""
    marco_car_pos = """
    # Car position 
    LOOP {}
        DPAD_RIGHT 0.1S
        0.5S
    1.0S"""
    macro_last_car = """
    MINUS 0.1S
    5.0S
    B 0.1S
    3.0S"""


    if car_pos[0] == 'L':  # L for the last car to be selected
       macro = macro_last_car
    else:
       if car_row[1] == '_':  # The car class method currently does not work as ZR/ZL will loop through  infinetly
            car_class = int(car_row[0]) - 1
            car_row = car_row[2:]
            if car_class == 0:
                macro = macro_reset_car + macro_car_row.format(car_row)
            else:
                macro = macro_reset_car + macro_class.format(car_class) + macro_move_down + macro_car_row.format(car_row)
       else: # Addressing from the 1st car of D class
            macro = reset_move_to_car_pos(car_pos, car_row)

    return macro


def mp_loop(mp_no=1, rep = 1, garage=[], race_time=168, blue_nitro=True, quit=False):
    # mp_no: select MP 1,2,3
    # MP loop. Reset car pos. to the very beginning.
    # rep:      number of repetitions for each car
    # garage:   array of tuples [{"<car pos>:<UP/DOWN pos>}], if garage = [] it will stay at the last selected car

    macro = ''

    MP_RACE_LOAD_TIME = """
    35.0S"""

    LOOP = """
# MP CAR 1 
LOOP {}
    # 235.5S EACH CYCLE"""

    LOOP = LOOP + MACRO_RESET_TO_CAREER_CORNER + """
    # to multiplayer section
    LOOP 4
        ZL 0.1S
        1.0S
    2.0S"""
    if mp_no > 1:
       for i in range(mp_no-1):

           LOOP = LOOP + """
    DPAD_DOWN 0.1S
    1.0S"""
    LOOP = LOOP + """
    LOOP 2
        A 0.1S
        3.0S
    5.0S"""

    if quit:
        nitro_loop = MACRO_QUIT_RACE
    else:
        nitro_loop = nitro(duration=race_time, blue_nitro=blue_nitro)

    if len(garage) != 0:
        for dic in garage:
            for pos,row in dic.items():
                macro = macro + LOOP.format(rep)  + class_move_to_car_pos(pos, row) + AA + MP_RACE_LOAD_TIME + nitro_loop + MACRO_BACK_TO_HOME
                #  parse_macro(LOOP.format(rep, pos, row))
    else:
        macro = macro + LOOP.format(rep) + AA + MP_RACE_LOAD_TIME + nitro_loop + MACRO_BACK_TO_HOME

    macro = macro + "\n# MP loop duration: " + str(macro_time(macro))
    return macro

def hunt_classic(rep = 1, garage=[], event_position=5, race_time=60, blue_nitro = True, dirrection=''):
    # Classic car hun loop. Reset car pos. to the very beginning. 
    # rep:      number of repetitions for each car
    # garage:   array of tuples [{"<car pos>:<UP/DOWN pos>}]
    # blue_nitro:  blue or orange nitro
    macro = ''

    HUNT_LOAD_TIME = """
    29.0S"""

    LOOP = """
# HUNT CAR 
LOOP {}""" + MACRO_RESET_TO_CAREER_CORNER + """
    # to daily 
    LOOP 5
        ZL 0.1S
        1.0S
    2.0S
    A 0.1S
    4.0S
    # CAR HUNT EVENT POSITION
    LOOP {}
        DPAD_RIGHT 0.1S
        1.0S
    LOOP 3
        A 0.1S
        5.0S"""
    DELAY = """
    B 0.1S
    3.0S
    B 0.1S
    12.0S"""
    if len(garage) != 0:
        for dic in garage:
            for pos,row in dic.items():
                macro = macro + LOOP.format(rep, event_position)  + reset_move_to_car_pos(pos, row) + AA + HUNT_LOAD_TIME + nitro(duration=race_time, blue_nitro=blue_nitro, dirrection=dirrection) + DELAY + MACRO_BACK_TO_HOME
    else:
        macro = macro + LOOP.format(rep, event_position) + AA + HUNT_LOAD_TIME + nitro(duration=race_time, blue_nitro=blue_nitro, dirrection=dirrection) + DELAY + MACRO_BACK_TO_HOME

    macro = macro + "\n# hunt loop duration: " + str(macro_time(macro))
    return macro


