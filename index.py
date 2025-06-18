from  line_coding_waveform.menu.show_meu import  choice_menu

def main():
    while True:
        try:
            user_input = int(input("input angka yang ingin di simulasikan (mis : 1513623040) >> "))
            # conversi angka yang diinput user ke biner
            covert_biner = format(user_input, "032b")
            print(covert_biner)
            choice_menu()
        except ValueError:
            print("input hanya boleh angka !!")
            continue

if __name__=="__main__":
    main()