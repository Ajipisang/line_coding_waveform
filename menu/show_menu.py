from  line_coding_waveform.get_wave_form.NRZ import  generate_NRZ_waveform
from  line_coding_waveform.plot_polar.plot_NRZ import plot_polar
list = ["NRZ-L", "NRZ-I", "RZ", "Manchester", "Differential Manchester", "AMI (Alternate Mark Inversion)",
        "B8ZS (Bipolar 8-Zero Substitution)", "HDB3 (High-Density Bipolar 3)"]
def menu():

    print("==== list line coding ====")
    for i,item in enumerate(list):
        print(f"{i+1}. {item}")


def choice_menu(bitstream,user_input):
    while True:
        menu()
        try:
            user_choice = int(input("input pilihan line coding >>>"))
            if 0 < user_choice < len(list):
                if user_choice ==1 :
                    plot_polar(bitstream,user_input,"L")
                elif user_choice ==2 :
                    plot_polar(bitstream,user_input,"I")
                continue
            else:
                print("input di luar list !!")
                continue
        except ValueError:
            print("input hanya boleh angka")
            continue

