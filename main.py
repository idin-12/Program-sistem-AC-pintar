# Program Sistem AC Pintar
# Menyala hanya jika:
# - Suhu panas (is_hot = yes)
# - Jendela tertutup (window_closed = yes)
# - Ada orang di rumah (someone_home = yes)

def input_to_bool(user_input):
    return user_input.lower() == "yes"

def main():
    is_hot_input = input("Apakah suhu panas? (yes/no): ")
    window_closed_input = input("Apakah jendela tertutup? (yes/no): ")
    someone_home_input = input("Apakah ada orang di rumah? (yes/no): ")

    is_hot = input_to_bool(is_hot_input)
    window_closed = input_to_bool(window_closed_input)
    someone_home = input_to_bool(someone_home_input)

    if is_hot and window_closed and someone_home:
        print("AC MENYALA")
    else:
        print("AC MATI")

if __name__ == "__main__":
    main()
