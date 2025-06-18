list = ["NRZ-L", "NRZ-I", "RZ", "Manchester", "Differential Manchester", "AMI (Alternate Mark Inversion)",
        "B8ZS (Bipolar 8-Zero Substitution)", "HDB3 (High-Density Bipolar 3)"]
def menu():

    print("==== list line coding ====")
    for i,item in enumerate(list):
        print(f"{i+1}. {item}")

def choice_menu():
    while True:
        menu()
        try:
            user_choice = int(input("input pilihan line coding >>>"))
            if 0 < user_choice < len(list):
                print("valid")
                break
            else:
                print("input di luar list !!")
                continue
        except ValueError:
            print("input hanya boleh angka")
            continue

