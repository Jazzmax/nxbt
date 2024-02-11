import asphalt9

def main():

    ### Garage definitions

    td_hunt_1 = ['3.0S','DPAD_RIGHT 0.1S','1.0S','Y 0.1S','0.1S','Y 0.1S','0.1S' ]

    garage_1 = [{'3':'UP'}]

    garage_mp1_3_d_car_slips = [{'3':'UP'}, {'6':'UP'}, {'9':'UP'}]

    garage_d_hunt = [{'9':'UP'}]

    garage_b_hunt = [{'18':'UP'}, {'25':'DOWN'}, {'16':'DOWN'}]

    garage_valhalla = [{'5':'DOWN'}]

    garage_mixed_leagues = [{'20':'DOWN'}, {'22':'UP'}, {'24':'UP'}, {'26':'DOWN'}, {'33':'UP'}, {'33':'DOWN'}, {'34':'UP'}, {'34':'DOWN'}, {'35':'UP'}, {'38':'DOWN'}, {'39':'DOWN'}]

    garage_for_b_hunt = [{'20':'UP'}, {'22':'DOWN'}, {'27':'UP'}]

    garage_mp2_8_cars = [{'3':'DOWN'}, {'2':'DOWN'}, {'1':'DOWN'}, {'2':'UP'}, {'0':'DOWN'}, {'1':'UP'}, {'0':'UP'}]

    garage_mp2_8_cars_p1 = [{'3':'DOWN'}, {'3':'UP'}, {'2':'DOWN'}, {'1':'DOWN'}, {'2':'UP'}]
    garage_mp2_8_cars_p2 = [{'1':'UP'}]

    garage_mp2_15_cars = [{'7':'DOWN'}, {'7':'UP'}, {'6':'UP'},{'4':'UP'},{'3':'UP'},{'2':'DOWN'},{'2':'UP'}, {'5':'DOWN'}, {'5':'UP'}, {'4':'DOWN'}, {'1':'DOWN'}, {'1':'UP'}, {'0':'DOWN'}, {'3':'DOWN'}, {'0':'UP'} ]

    garage_mp1_4_c_car_classic = [{'18':'DOWN'}, {'19':'DOWN'}, {'20':'DOWN'}, {'21':'DOWN'}, {'21':'UP'} ]

    garage_mp_4_c_car_classic = [{'18':'DOWN'}, {'19':'DOWN'}, {'20':'DOWN'}, {'21':'DOWN'}, {'21':'UP'} ]

    garage_mp1_6_car_classic1 = [{'5':'DOWN'}, {'6':'UP'}, {'7':'UP'}, {'8':'UP'}, {'9':'UP'}, {'9':'DOWN'}, {'13':'UP'}, {'9':'DOWN'},{'12':'DOWN'}, {'13':'DOWN'}  ]
    garage_mp_16_c_car_classic = [{'13':'DOWN'}, {'21':'UP'}, {'22':'UP'}, {'22':'DOWN'}, {'23':'UP'}, {'23':'DOWN'},{'24':'UP'},{'25':'UP'},{'26':'DOWN'},{'29':'UP'},{'31':'DOWN'},{'32':'UP'},{'32':'DOWN'},{'34':'UP'},{'35':'UP'},{'35':'DOWN'} ]

    garage_mp_10_c_car_slip_2nd_acc = [{'22':'UP'}, {'23':'DOWN'}, {'24':'UP'},{'25':'UP'},{'25':'DOWN'}, {'29':'UP'},{'33':'UP'},{'34':'UP'},{'35':'DOWN'}, {'49':'DOWN'}, {'50':'UP'}, {'51':'DOWN'} ]
    garage_mp1_9_c_car_2nd_acc = [{'13':'DOWN'},{'21':'UP'}, {'22':'UP'}, {'23':'DOWN'}, {'24':'UP'},{'25':'UP'}, {'29':'UP'},{'34':'UP'},{'35':'DOWN'} ]



    garage_mp1_2_c_car_classic2 = [{'20':'DOWN'}, {'21':'DOWN'} ]

    garage_mp_3_d_car_slip = [{'10':'DOWN'}, {'10':'UP'}, {'11':'UP'}]
    garage_mp_3_d_car_classic = [{'6':'DOWN'}, {'10':'DOWN'}, {'10':'UP'}, {'12':'UP'}, {'12':'DOWN'}]

    garage_mp_5_c_car_slip = [{'6':'UP'}, {'4':'UP'}, {'7':'DOWN'}, {'7':'UP'}, {'8':'DOWN'}, {'8':'UP'}, {'9':'UP'}]

    garage_mp2_1_cars = [{'4':'UP'}]

    garage_mp_11_cars = [{'7':'UP'}, {'8':'UP'}, {'8':'DOWN'}, {'9':'UP'}, {'9':'DOWN'}, {'10':'DOWN'},{'12':'UP'},{'11':'DOWN'},{'5':'DOWN'}]
    garage_mp_12_cars = [{'8':'DOWN'}, {'9':'DOWN'}, {'11':'DOWN'}, {'12':'DOWN'}, {'13':'DOWN'},{'15':'UP'},{'16':'UP'},{'17':'UP'}]

    # new garage format {'class_no':'col_row'}
    garage_mp1_class_test = [{'6':'2_UP'} ]

    # test the last mp1 car 
    garage_mp1_last_car = [{'L':'0'} ]

    
    ### Races macro output 
    print(asphalt9.MACRO_CONTROLLER_CONNECTION)

    #out = hunt_classic(rep=1, garage=[], event_position=4, race_time=55, blue_nitro=False)
    #print(out)

    #out = mp_loop(mp_no=2, rep=100, garage=[{'5':'UP'}], race_time=100, blue_nitro=False)
    #print(out)

    #out = hunt_classic(rep=2, garage=[], event_position=5, race_time=60, blue_nitro=False)
    #print(out)

    #out = mp_loop(mp_no=1, rep=1, garage=[{'3':'DOWN'}], race_time=120, blue_nitro=True)
    #print(out)


    #out = mp_loop(mp_no=2, rep=50, garage=[{'3':'DOWN'}, {'7':'DOWN'},{'8':'DOWN'},{'13':'DOWN'}], race_time=65, blue_nitro=False)
    out = asphalt9.mp_loop(mp_no=1, rep=1, garage=garage_mp_10_c_car_slip_2nd_acc, race_time=120, blue_nitro=False)
    print(out)

    #print(parse_macro(out))
    #print(macro_time(out))
    #print(600 - macro_time(out))


if __name__ == '__main__':
    main()
