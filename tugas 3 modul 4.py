
data_mahasiswa = {
    "username": "sarmila",
    "password": "07352311128"
}

# Data mata kuliah dan dosen pengampuh
data_mata_kuliah = {
    "Matematika": ["pak sarifudin", "pak amal" ],
    "daspro": ["pak yasir"],
    "arsikom": ["pak ceko"],
}

# Autentikasi atau login mahasiswa
username_input = input("Masukkan username: ")
password_input = input("Masukkan password: ")

if username_input == data_mahasiswa["username"]:
    if password_input == data_mahasiswa["password"]:
        print("Login berhasil!")
        
        # Pilihan mata kuliah
        print("Pilih mata kuliah:")
        for mata_kuliah in data_mata_kuliah:
            print("-", mata_kuliah)
        
        mata_kuliah_input = input("Masukkan mata kuliah yang Anda pilih: ")
        
        # Memastikan mata kuliah yang dipilih tersedia
        if mata_kuliah_input in data_mata_kuliah:
            # Pilihan dosen pengampuh
            print("Pilihan dosen pengampuh untuk", mata_kuliah_input, ":")
            for dosen in data_mata_kuliah[mata_kuliah_input]:
                print("-", dosen)
            
            dosen_pengampuh_input = input("Pilih dosen pengampuh: ")
            
            # Memastikan dosen pengampuh yang dipilih tersedia
            if dosen_pengampuh_input in data_mata_kuliah[mata_kuliah_input]:
                print("Mata kuliah", mata_kuliah_input, "akan diajar oleh", dosen_pengampuh_input)
            else:
                print("Dosen pengampuh yang Anda pilih tidak tersedia.")
        else:
            print("Mata kuliah yang Anda pilih tidak tersedia.")
    else:
        print("Password salah!")
else:
    print("Username tidak ditemukan!")
