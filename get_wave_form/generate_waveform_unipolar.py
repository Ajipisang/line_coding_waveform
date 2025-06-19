def generate_waveform(bitstream, type):
    if type == "RZ unipolar":
        return rz_unipolar(bitstream)


def rz_unipolar(bitstream):
    bits = [int(b) for b in bitstream]
    time = []
    level_signals = []

    for index, bit in enumerate(bits):
        time.extend([index, index + 0.5, index + 1])
        if bit == 1:
            level_signals.extend([1, 0, 0])
        else:
            level_signals.extend([0, 0, 0])

    return time, level_signals
