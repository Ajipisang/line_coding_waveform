import  matplotlib.pyplot as plt
import os
from  line_coding_waveform.get_wave_form.generate_waveform_polar import generate_waveform
def plot_polar(bitstream,user_input,type):
    time,level_signal=generate_waveform(bitstream,type=type)
    plt.figure(figsize=(15,6))
    plt.plot(time,level_signal,drawstyle="steps-post")
    plt.yticks([1,0,-1])
    plt.ylim(-1.5, 1.5)
    plt.title(f'{type}  Line Coding\nBitstream:{bitstream}({user_input})')
    plt.xlabel('Time')
    # plt.xticks(time)
    plt.ylabel('Voltage Level')
    plt.xticks([],[])
    plt.axhline(y=0, color='black', linestyle='-', linewidth=1)
    plt.xlim(0, len(bitstream))  # Membuat sumbu X hanya selebar bitstream
    plt.margins(x=0)
    for x in range(len(bitstream)+1):
        plt.axvline(x, color="gray", linestyle="--", linewidth="0.5")

    for i, bit in enumerate(bitstream):
        plt.text(i + 0.2, 1.2, bit)

    os.makedirs(f"plots_result/{user_input}", exist_ok=True)
    # Simpan ke folder
    filename = f"plots_result/{user_input}/{type.replace(' ', '_')}_plot.png"
    plt.savefig(filename, dpi=300)
    plt.tight_layout()
    plt.show()