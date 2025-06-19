from  line_coding_waveform.menu.show_menu import  choice_menu
def convert_bit(id):
    total=str(id) + "151362"
    binary_4bit = ''.join([format(int(digit), '04b') for digit in total])
    return  binary_4bit
def main():
    while True:
        try:
            user_input = int(input("input angka yang ingin di simulasikan (mis : 1513623040) >> "))
            # conversi angka yang diinput user ke biner
            covert_biner = convert_bit(user_input)
            print(len(covert_biner))
            choice_menu(covert_biner,user_input)
        except ValueError:
            print("input hanya boleh angka !!")
            continue

if __name__=="__main__":
    main()