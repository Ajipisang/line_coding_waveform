def generate_NRZ_waveform(bitstream,type):
    # pecah bitstream masukin ke dalem list dengan tiap item di list adalah angka bitstream
    bits=[int(b) for b in bitstream]
    time=[]
    level_signals=[]

    current_level = 1
    for index,bit in enumerate(bits):
        if type == "L":
            level=1 if bit==0 else -1
        elif type == "I":
            if bit ==1 :
                current_level *=-1
            level=current_level
        time.extend([index,index+1])
        level_signals.extend([level,level])

    return  time,level_signals