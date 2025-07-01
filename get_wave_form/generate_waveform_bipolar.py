def generate_waveform(bitstream, type):
    if type == "AMI":
        return AMI(bitstream)
    elif type == "B8ZS":
        return B8ZS(bitstream)
    elif type=="HDB3":
        return HDB3(bitstream)


def AMI(bitstream):
    bits = [int(b) for b in bitstream]
    time = []
    level_signals = []
    current_voltage = 1
    for index, bit in enumerate(bits):
        time.extend([index, index +1])
        if bit ==1 :
            level_signals.extend([current_voltage, current_voltage])
            current_voltage *=-1
        else:
            level_signals.extend([0, 0])
    return time, level_signals

def B8ZS(bitstream):
    bits = [int(b) for b in bitstream]
    time = []
    level_signals = []
    current_voltage = -1
    i=0
    while i < len(bits):
        #check jika bits bernilai 0 8 kali berturut turut
        if bits[i:i+8]==[0] * 8:
            if current_voltage == 1:
                subst = [0, 0, 0, 1, -1, 0, -1, 1]  # Jika terakhir +1
            else:
                subst = [0, 0, 0, -1, 1, 0, 1, -1]  # Jika terakhir -1
            for j in range (8):
                time.extend([i+j,i+j+1])
                level_signals.extend([subst[j],subst[j]])

            i+=8
        else:
            bit=bits[i]
            if bit==1:
                current_voltage *= -1
                val = current_voltage
            else:
                val = 0

            time.extend([i, i + 1])
            level_signals.extend([val, val])
            i += 1

    return time, level_signals


def HDB3(bitstream):
    bits = [int(b) for b in bitstream]
    time = []
    level_signals = []
    pulse_count=0
    i=0
    current_voltage=1
    if current_voltage == 1:
        current_voltage *= -1

    while i < len(bits):
        if bits[i : i+4] == [0,0,0,0]:
            if pulse_count % 2 ==0  :
                subst=[-current_voltage,0,0,-current_voltage]
            else :
                subst = [0, 0, 0, current_voltage]
                current_voltage *= -1
            for j in range(4):
                time.extend([i + j, i + j + 1])
                level_signals.extend([subst[j], subst[j]])
            current_voltage*=-1
            pulse_count=0
            i += 4
        else:
            # Proses bit normal
            bit = bits[i]
            if bit == 1:
                current_voltage *= -1
                pulse_count += 1
                val = current_voltage
            else:
                val = 0
                pulse_count=0

            time.extend([i, i + 1])
            level_signals.extend([val, val])
            i += 1

    return time, level_signals