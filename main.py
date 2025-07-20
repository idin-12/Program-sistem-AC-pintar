# Program Sistem AC Pintar
# Menyala hanya jika:
# - Suhu panas
# - Jendela tertutup
# - Ada orang di rumah

def input_to_bool(prompt):
    """
    Fungsi untuk meminta input user yes/no dan mengembalikan boolean.
    """
    user_input = input(prompt + " (yes/no): ").strip().lower()
    return user_input == "yes"

def check_ac(is_hot, window_closed, someone_home):
    """
    Mengecek kondisi AC berdasarkan syarat.
    """
    if is_hot and window_closed and someone_home:
        return "AC MENYALA"
    else:
        return "AC MATI"

def main():
    print("=== Sistem AC Pintar ===")

    # Input user untuk ketiga kondisi
    is_hot = input_to_bool("Apakah suhu panas?")
    window_closed = input_to_bool("Apakah jendela tertutup?")
    someone_home = input_to_bool("Apakah ada orang di rumah?")

    # Cek logika AC
    result = check_ac(is_hot, window_closed, someone_home)
    print(result)

if __name__ == "__main__":
    main()
