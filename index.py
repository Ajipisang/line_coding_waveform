from  line_coding_waveform.menu.show_menu import  choice_menu
def convert_bit(id):
    total=str(id) + "151362"
    binary_4bit=[]
    for digit in total:
        biner=format(int(digit),"04b")
        binary_4bit.append(biner)
    bitstream = ''.join(binary_4bit)
    return bitstream


def main():
    while True:
        try:
            user_input = str(input("input angka yang ingin di simulasikan (mis : 1513623040) >> "))
            # conversi angka yang diinput user ke biner
            convert_biner = convert_bit(user_input)
            print(len(convert_biner))
            choice_menu(str(user_input),user_input)
        except ValueError:
            print("input hanya boleh angka !!")
            continue

if __name__=="__main__":
    main()