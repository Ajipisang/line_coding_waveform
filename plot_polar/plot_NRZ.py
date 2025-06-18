import  matplotlib.pyplot as plt
from  line_coding_waveform.get_wave_form.NRZ import generate_NRZ_waveform
def plot_polar(bitstream,user_input,type):
    time,level_signal=generate_NRZ_waveform(bitstream,type=type)
    plt.figure(figsize=(10,6))
    plt.plot(time,level_signal,drawstyle="steps-post")
    plt.yticks([1,0,-1])
    plt.ylim(-1.5, 1.5)
    plt.title(f'NRZ-L  Line Coding\nBitstream:{bitstream}({user_input})')
    plt.xlabel('Time')
    plt.ylabel('Voltage Level')
    plt.xticks([],[])
    plt.axhline(y=0, color='black', linestyle='-', linewidth=1)

    for x in range(len(bitstream)+1):
        plt.axvline(x , color="gray",linestyle="--",linewidth="0.5")

    for i, bit in enumerate(bitstream):
        plt.text(i + 0.4, 1.2, bit)

    plt.tight_layout()
    plt.show()