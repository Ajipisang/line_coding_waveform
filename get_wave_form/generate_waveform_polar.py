def generate_waveform(bitstream,type):
        if type == "NRZ-L":
           return  nrz_l(bitstream)
        elif type == "NRZ-I":
            return  nrz_i(bitstream)
        elif type == "RZ polar":
            return  rz_polar(bitstream)
        elif type == "manchester thomas":
            return manchester_thomas(bitstream)
        elif type == "manchester IEEE":
            return manchester_IEEE(bitstream)
        elif type == "Differential Manchester":
            return diff_manchester(bitstream)



def nrz_l(bitstream):
    bits=[int(b) for b in bitstream]
    time=[]
    level_signals=[]
    for index,bit in enumerate(bits):
        level = 1 if bit == 1 else -1
        time.extend([index, index + 1])
        level_signals.extend([level, level])
    return  time,level_signals


def nrz_i(bitstream):
    bits=[int(b) for b in bitstream]
    time=[]
    level_signals=[]
    current_level = 1
    for index,bit in enumerate(bits):
        if bit == 1:
            current_level *= -1
        level = current_level
        time.extend([index, index + 1])
        level_signals.extend([level, level])
    return  time,level_signals

def rz_polar(bitstream):
    bits=[int(b) for b in bitstream]
    time=[]
    level_signals=[]

    for index,bit in enumerate(bits):
        time.extend([index, index + 0.5, index + 1])
        if bit ==1 :
            level_signals.extend([1,0,0])
        else:
            level_signals.extend([-1,0,0])

    return time,level_signals

def manchester_thomas(bitstream):
    bits=[int(b) for b in bitstream]
    time=[]
    level_signals=[]

    for index,bit in enumerate(bits):
        time.extend([index, index + 0.5, index + 1])
        if bit ==1 :
            level_signals.extend([1,-1,-1])
        else:
            level_signals.extend([-1,1,1])

    return time,level_signals

def manchester_IEEE(bitstream):
    bits=[int(b) for b in bitstream]
    time=[]
    level_signals=[]

    for index,bit in enumerate(bits):
        time.extend([index, index + 0.5, index + 1])
        if bit ==1 :
            level_signals.extend([-1,1,1])
        else:
            level_signals.extend([1,-1,-1])

    return time,level_signals


def diff_manchester(bitstream):
    bits=[int(b) for b in bitstream]
    time=[]
    level_signals=[]
    current_level=1
    for index,bit in enumerate(bits):
        time.extend([index, index + 0.5, index + 1])
        if bit ==0 :
            current_level *=-1
        level_signals.extend([current_level,-current_level,-current_level])
        current_level *=-1

    return time,level_signals
