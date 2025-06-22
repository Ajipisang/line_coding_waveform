from  line_coding_waveform.plot.plot_polar import plot_polar
from line_coding_waveform.plot.plot_unipolar import plot_unipolar
from line_coding_waveform.plot.plot_bipolar import  plot_bipolar

list_line_coding = ["NRZ-L", "NRZ-I", "RZ", "Manchester", "Differential Manchester", "AMI (Alternate Mark Inversion)",
        "B8ZS (Bipolar 8-Zero Substitution)", "HDB3 (High-Density Bipolar 3)"]
def menu():

    print("==== list line coding ====")
    for i,item in enumerate(list_line_coding):
        print(f"{i+1}. {item}")
    print(f"{len(list_line_coding)+1}. pilih semuanya" )

def choice_menu(bitstream,user_input):
    while True:
        menu()
        try:
            user_choice = int(input("input pilihan line coding >>>"))
            if 0 < user_choice <= len(list_line_coding):
                if user_choice == 1:
                    plot_polar(bitstream,user_input,"NRZ-L")
                elif user_choice == 2:
                    plot_polar(bitstream,user_input,"NRZ-I")
                elif user_choice == 3:
                    plot_polar(bitstream, user_input, "RZ polar")
                    plot_unipolar(bitstream, user_input, "RZ unipolar")
                elif user_choice == 4:
                    plot_polar(bitstream, user_input, "manchester thomas")
                    plot_polar(bitstream,user_input,"manchester IEEE")
                elif user_choice == 5:
                    plot_polar(bitstream, user_input, "Differential Manchester")
                elif user_choice == 6:
                    plot_bipolar(bitstream, user_input, "AMI")
                elif user_choice == 7:
                    plot_bipolar(bitstream, user_input, "B8ZS")
                elif user_choice == 8:
                    plot_bipolar(bitstream, user_input, "HDB3")
                continue
            elif user_choice==len(list_line_coding)+1:
                plot_polar(bitstream, user_input, "NRZ-L")
                plot_polar(bitstream, user_input, "NRZ-I")
                plot_polar(bitstream, user_input, "RZ polar")
                plot_unipolar(bitstream, user_input, "RZ unipolar")
                plot_polar(bitstream, user_input, "manchester thomas")
                plot_polar(bitstream, user_input, "manchester IEEE")
                plot_polar(bitstream, user_input, "Differential Manchester")
                plot_bipolar(bitstream, user_input, "AMI")
                plot_bipolar(bitstream, user_input, "B8ZS")
                plot_bipolar(bitstream, user_input, "HDB3")
            else:
                print("input di luar list !!")
                continue
        except ValueError:
            print("input hanya boleh angka")
            continue

