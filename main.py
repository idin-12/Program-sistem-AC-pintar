# ac_pintar.py
# Program Sistem AC Pintar
# AC menyala hanya jika:
# - Suhu panas (is_hot = yes)
# - Jendela tertutup (window_closed = yes)
# - Ada orang di rumah (someone_home = yes)

def input_to_bool(prompt):
    """
    Mengubah input user 'yes' atau 'no' menjadi nilai boolean.
    """
    user_input = input(prompt + " (yes/no): ").strip().lower()
    return user_input == "yes"

def main():
    print("=== SISTEM AC PINTAR ===")

    # Input kondisi
    is_hot = input_to_bool("Apakah suhu panas?")
    window_closed = input_to_bool("Apakah jendela tertutup?")
    someone_home = input_to_bool("Apakah ada orang di rumah?")

    # Mengecek logika AC
    if is_hot and window_closed and someone_home:
        print("AC MENYALA")
    else:
        print("AC MATI")

if __name__ == "__main__":
    main()
