import time
import random
dt = [
    ["Kevin Tanuwijaya", "Pria", 22, "Tionghoa", "ENTP", "ITB", "Teknik", "Suka batagor, ayo keliling Bandung buat nyari batagor","TanuKevin8877","Katolik"],
    ["Cindy Halim", "Wanita", 20, "Tionghoa", "INFJ", "UNPAR", "Kesehatan", "Stressed out 3rd year medstud. Looking for fun","Cindy0909","Kristen"],
    ["Wilson Lie", "Pria", 19, "Tionghoa", "ISTJ", "ITB", "Sains", "Kerjaannya ngitung tapi gak perhitungan","WilsonLii","Buddha"],
    ["Lydia Tan", "Wanita", 18, "Tionghoa", "ENFP", "UNPAD", "Sastra", "Oui oui","FrenchLydia","Konghucu"],
    ["Budi Santoso", "Pria", 21, "Jawa", "INTJ", "ITB", "Teknik", "Bisa jadi pacar, bisa joki python. Serba bisa","BudiS123","Islam"],
    ["Sari Wulandari", "Wanita", 20, "Jawa", "ISFJ", "UNPAR", "Bisnis", "Mari kita bangun masa depan bersama","Sariwwwuuuu","Islam"],
    ["Rizal Maulana", "Pria", 19, "Sunda", "ESTP", "UNPAD", "Kesehatan", "Open for pharmacy study date","RizalM456","Islam"],
    ["Nia Rahmawati", "Wanita", 18, "Sunda", "ESFP", "ITB", "Seni", "Seni adalah ledakan","NiaRahma79","Islam"],
    ["Togar Simanjuntak", "Pria", 23, "Batak", "ENTJ", "UNPAR", "Hukum", "Siap belain kamu","TogarSiam","Kristen"],
    ["Lestari Sihombing", "Wanita", 22, "Batak", "ISFP", "UNPAD", "Farmasi", "Ur future pharmacist!","LestariS22","Katolik"],
    ["Hans Gunawan", "Pria", 21, "Tionghoa", "INTP", "ITB", "Teknik", "Sudah terbiasa terjadi tante","HansG999","Katolik"],
    ["Greta Wijaya", "Wanita", 19, "Tionghoa", "INFJ", "UNPAD", "Kesehatan", "Gak perlu khawatir cari dokter","Nuggets166","Katolik"],
    ["Yonas Pattiradjawane", "Pria", 22, "Ambon", "ENFP", "UNPAR", "Seni", "Bisa desain rumah dan membangun rumah tangga","YonasP33","Katolik"],
    ["Maria Niron", "Wanita", 21, "Flores", "ESFJ", "ITB", "Seni", "Hidup adalah panggung seni","MariaNiron77","Kristen"],
    ["Alfred Tendean", "Pria", 23, "Manado", "ESTJ", "UNPAD", "Bisnis", "OTW CEO","AlfredT23","Katolik"],
    ["Isabela Langi", "Wanita", 20, "Manado", "INFP", "UNPAR", "Sastra", "Kata hati adalah suara jiwa","IsaLangi20","Kristen"],
    ["Andri Putra", "Pria", 22, "Minang", "ISTP", "ITB", "Teknik", "Menunggu kamu sebelum lulus","AndriP_22","Islam"],
    ["Natalia Runtu", "Wanita", 19, "Minahasa", "ENFJ", "UNPAD", "Hukum", "Siap jadi pendamping hidup","NataliaR19","Kristen"],
    ["Farhan Alatas", "Pria", 21, "Arab", "ENTP", "UNPAR", "Bisnis", "Bisnis bareng yuk","FarhanA21","Islam"],
    ["Layla Zahra", "Wanita", 20, "Arab", "ISFJ", "ITB", "Teknik", "Life is a highway!", "LaylaZ_20","Islam"],
]

ras = [p[3] for p in dt] # Ekstrak semau nilai 'ras' dari list dt asli
agama_list = list(set([p[9] for p in dt])) # Ekstrak semua nilai unik 'agama'
mbti_list = list(set([p[4] for p in dt])) # Ekstrak semua nilai unik 'MBTI'

pu = [["User1","Admin123456"],["User2","Admin1001"],["User3","Password123"]] #Database username dan password
a = [0,0]
logged_in = False
while logged_in == False:
    print("Halo Pencari Jodoh, Selamat datang di Program Dating Kampus 2025!\n")
    have_account = (input("Apakah Anda memiliki akun? (Y/N): "))
    if have_account.upper() == "N":
        c = [0,0]
        print("====================================")
        print("Tolong buat akun terlebih dahulu")
        print("====================================")
        c[0] = input("Username             : ")
        pw_matched = False
        while pw_matched == False:
            p_1 = input("Password             : ")
            p_2 = input("Konfirmasi Password  : ")
            if p_1 == p_2:
                c[1] = p_1
                pu.append(c)
                print("")
                print(">>>>>>Akun Anda berhasil dibuat!<<<<<<")
                print("")
                pw_matched = True
            else:
                print("")
                print("===========================")
                print("Password tidak sesuai")
                print("===========================")
    elif have_account.upper() == "Y":
        pass # Lanjut ke login
    else:
        print("============================================")
        print("Input tidak valid. Mohon masukkan Y atau N.")
        print("============================================")
        continue # Tanya lagi untuk have_account

    a[0] = input("Username  : ")
    a[1] = input("Password  : ")
    i = 0
    while i <= len(pu)-1:
        if pu[i] == a:
            logged_in = True
            break
        else:
            logged_in = False
        i += 1
    if logged_in == False:
        print("Username atau Password salah")

r = [0 for p in range (11)] #Menyimpan data yang nantinya diinput oleh user mengenai preferensi mereka
yakin = 0
while yakin == 0:
    print("")
    print("======================================================================\n                   Silakan isi profil diri Anda!\n======================================================================")
    while r[6] == 0:
        r[6] = str(input("Nama Lengkap: "))

    valid_fakultas = ["Teknik", "Sosial", "Seni", "Sastra", "Bisnis", "Kesehatan", "Hukum", "Sains"]
    while r[9] == 0 or r[9].capitalize() not in valid_fakultas:
        r[9] = str(input("Asal Fakultas Anda dari mana?\n- Teknik       - Bisnis\n- Sosial       - Kesehatan\n- Seni         - Hukum\n- Sastra       - Sains\nJawaban     : ")).capitalize()
        if r[9] not in valid_fakultas:
            print("Input tidak valid. Mohon masukkan salah satu dari daftar fakultas.")
            r[9] = 0 # Reset r[9] untuk tetap berada di loop

    r[7] = 0 # Reset input usia sebelum loop
    while r[7] < 18:
        try:
            r[7] = int(input("Usia (tahun): "))
            if r[7] < 18:
                print("Maaf, Anda masih dibawah umur. Silahkan masukkan usia yang benar.")
                r[7] = 0 # Reset usia untuk tetap berada di loop
        except ValueError:
            print("Input tidak valid. Mohon masukkan angka untuk usia.")
            r[7] = 0 # Reset usia untuk tetap berada di loop

    r[0] = "" # Reset input gender sebelum loop
    while r[0] != "Pria" and r[0] != "Wanita":
        try:
            gender_input = int(input("Apa jenis kelamin Anda?\n1. Pria\n2. Wanita\nJawaban (1/2): "))
            if gender_input == 1:
                r[0] = "Pria"
            elif gender_input == 2:
                r[0] = "Wanita"
            else:
                print("Input tidak valid. Mohon masukkan angka 1 atau 2.")
        except ValueError:
            print("Input tidak valid. Mohon masukkan angka 1 atau 2.")

    # Filter dt berdasarkan gender setelah input user
    dt_filtered_gender = [person for person in dt if person[1] != r[0]]


    print("======================================================================\n                Masukkan Preferensi Pasangan Anda\n======================================================================")
    r[1] = 0 # Reset batas bawah usia
    r[2] = 0 # Reset batas atas usia
    while r[1] == 0 or r[2] == 0 or r[2] < r[1] or r[1] < 18:
        try:
            r[1] = int(input("Batas bawah usia yang dicari? "))
            r[2] = int(input("Batas atas usia yang dicari? "))
            if r[2] < r[1]:
                print("Batas atas usia tidak boleh lebih kecil dari batas bawah.")
                r[1] = 0
                r[2] = 0
            if r[1] < 18:
                print("Batas usia bawah adalah 18 tahun!")
                r[1] = 0
                r[2] = 0
        except ValueError:
            print("Input tidak valid. Mohon masukkan angka untuk batas usia.")
            r[1] = 0
            r[2] = 0
    print("======================================================================")

    r_inp = 0
    while r_inp == 0: # Loop hingga data sesuai
        r_m = str(input("Ras dari pasangan yang ingin Anda cari?\n- Tionghoa      - Jawa\n- Batak         - Manado\n- Minang        - Minahasa\n- Flores        - Sunda\n- Ambon\n(Pisahkan dengan koma jika pilihan Anda lebih dari 1)\nJawaban    : "))
        r[3] = [x.strip().capitalize() for x in r_m.split(",")]
        pl = ""
        llm = list(set(r[3]) - set(ras))
        if len(llm) != 0:
            pl = ", ".join(llm) # Menggabungkan list ras yang hilang
            r_inp_valid_confirm = False # Menambahkan validasi pengulangan untuk konfirmasi ras
            while r_inp_valid_confirm == False:
                r_inp_confirm = input(f"{pl} tidak ada, apakah Anda tetap ingin melanjutkan pencarian ke tahap selanjutnya? (Y/N): ")
                if r_inp_confirm.upper() == "Y":
                    r_inp = 1
                    r_inp_valid_confirm = True
                elif r_inp_confirm.upper() == "N":
                    print("Silahkan input ulang ras yang dicari")
                    r[3] = 0 # Reset r[3] supaya tetap berada di dalam loop
                    r_inp = 0
                    r_inp_valid_confirm = True
                else:
                    print("Input tidak valid. Mohon masukkan Y atau N.")
            # Loop tetap berlanjut karena r_inp_valid_confirm tetap False
        else:
            r_inp = 1 # Input valid, lanjutkan

    print("===================================================================================")
    agama_inp = 0
    while agama_inp == 0: # Loop sampai input agama valid
        a_m = str(input(f"Agama dari pasangan yang Anda cari?\n- Katolik     - Kristen\n- Islam       - Konghucu\n- Buddha\n(Pisahkan dengan koma jika pilihan Anda lebih dari 1)\nJawaban    : "))
        r[10] = [x.strip().capitalize() for x in a_m.split(",")]
        pl_agama = ""
        llm_agama = list(set(r[10]) - set(agama_list))
        if len(llm_agama) != 0:
            pl_agama = ", ".join(llm_agama) # Menggabungkan list agama yang hilang
            agama_inp_confirm = False # Menambahkan loop validasi untuk konfirmasi agama
            while agama_inp_confirm == False:
                agama_confirm_input = input(f"{pl_agama} Tidak ada di dalam daftar agama yang tersedia, apakah Anda tetap ingin melakukan\npencarian ke tahap selanjutnya? (Y/N): ")
                if agama_confirm_input.upper() == "Y":
                    agama_inp = 1
                    agama_inp_confirm = True
                elif agama_confirm_input.upper() == "N":
                    print("Silahkan input ulang agama yang dicari")
                    r[10] = 0 # Reset r[10] supaya tetap berada di loop
                    agama_inp = 0
                    agama_inp_confirm = True
                else:
                    print("Input tidak valid. Mohon masukkan Y atau N.")
            # TLoop tetap berlanjut karena agama_inp_confirm tetap False
        else:
            agama_inp = 1 # Input valid, lanjutkan


    print("===================================================================================")
    mbti_inp = 0 # Menambahkan loop validasi unutk input MBTI
    while mbti_inp == 0:
        p_m = str(input(f"MBTI dari pasangan yang Anda cari?\n- ENTJ      - INFP      - ESFJ\n- ENTP      - ISTP      - ISTJ\n- ISFP      - ENFJ      - ESTP\n- ENFP      - INFJ      - ESFP\n- ESTJ      - INTP      - INTJ\n- ISFJ\n(Pisahkan dengan koma jika pilihan Anda lebih dari 1)"))
        r[4] = [x.strip().upper() for x in p_m.split(",")]
        invalid_mbti = [mbti for mbti in r[4] if mbti not in mbti_list]
        if not r[4] or invalid_mbti: # Cek jika list kosoong atau berisi MBTI yang tidak valid
             if invalid_mbti:
                 print(f"Input tidak valid. MBTI berikut tidak ada dalam daftar: {', '.join(invalid_mbti)}. Mohon masukkan salah satu dari daftar MBTI yang tersedia.")
             else:
                 print("Input tidak valid. Mohon masukkan setidaknya satu MBTI.")
             r[4] = 0 # Reset supaya tetap di loop jika kosong
        else:
            mbti_inp = 1 # Input valid, lanjutkan

    print("===================================================================================")
    valid_universitas = ["ITB", "UNPAR", "UNPAD"]
    r[5] = 0 # Reset input universitas
    while r[5] == 0 or not all(uni in valid_universitas for uni in r[5]):
        u_m = str(input("Universitas dari pasangan yang Anda cari?\n- Institut Teknologi Bandung (ITB)\n- Universitas Parahyangan (UNPAR)\n- Universitas Padjajaran (UNPAD)\n(Silakan masukkan jawaban dalam bentuk singkatan universitas yang sudah diberikan)\n(Pisahkan dengan koma jika pilihan Anda lebih dari 1)\nJawaban   : "))
        r[5] = [x.strip().upper() for x in u_m.split(",")]
        invalid_universities = [uni for uni in r[5] if uni not in valid_universitas]
        if not r[5] or invalid_universities: # Cek apakah list kosong atau ada data universitas yang invalid
             if invalid_universities:
                 print(f"Input tidak valid. Universitas berikut tidak ada dalam daftar: {', '.join(invalid_universities)}. Mohon masukkan salah satu dari daftar universitas.")
             else:
                 print("Input tidak valid. Mohon masukkan salah satu dari daftar universitas.")
             r[5] = 0 # Reset r[5] supaya tetap berada di dalam loop


    print("===================================================================================")
    valid_fakultas_pref = ["Teknik", "Sosial", "Seni", "Sastra", "Bisnis", "Kesehatan", "Hukum", "Farmasi", "Sains"] 
    r[8] = 0 # Reset input preferensi fakultas
    while r[8] == 0 or not all(fak in valid_fakultas_pref for fak in r[8]):
        f_m = input("Fakultas dari pasangan yang Anda cari?\n- Teknik       - Sosial\n- Seni          - Sastra\n- Bisnis       - Kesehatan\n- Hukum        - Farmasi\n- Sains\n(Pisahkan dengan koma jika pilihan Anda lebih dari 1)\nJawaban    : ")
        r[8] = [x.strip().capitalize() for x in f_m.split(",")]
        if not r[8] or not all(fak in valid_fakultas_pref for fak in r[8]): # Cek apakah list kosong atau ada invalid preferensi fakultas
            print("Input tidak valid. Mohon masukkan salah satu dari daftar fakultas.")
            r[8] = 0 # Reset r[8] supaya tetap berada di loop


    print("\n>>>>>>>>>>>>>>>>>>>> Rangkuman Data Preferensi calon pasangan Anda <<<<<<<<<<<<<<<<<<<<\n")
    print(f"Kriteria calon pasangan yang Anda cari\n  - Range usia    : {r[1]} - {r[2]} tahun\n  - Ras           : {r_m}\n  - Agama         : {a_m}\n  - MBTI           : {p_m}\n  - Kampus       : {u_m}\n  - Fakultas     : {f_m}")
    yakin_valid_input = False
    while yakin_valid_input == False:
        yakin_input = input("Apakah Anda sudah yakin dengan data tersebut? (Y/N): ")
        if yakin_input.upper() == "Y":
            yakin = 1
            yakin_valid_input = True
        elif yakin_input.upper() == "N":
            yakin = 0
            r = [0 for p in range (11)] # Reset r untuk memasukkan kembali preferensi
            yakin_valid_input = True
        else:
            print("Input tidak valid. Mohon masukkan Y atau N sebagai jawaban Anda.")
            # Loop tetap berlanjut karena yakin_valid_input tetap False


mul = [-1 for t in range(6)] #array untuk multiplier faktor
while round(sum(mul),0) != 1:
    print("========================================================================\n             PENENTUAN SKALA KATEGORI PASANGAN\n========================================================================")
    print("Masukkan seberapa penting faktor-faktor di bawah ini bagi Anda\nutuk memastikan sistem memberikan pilihan yang terbaik!\n(0 sangat tidak penting, 100 sangat penting) ")
    try:
        mul_input = [0] * 6 # Inisialisasi dengan 0
        while True:
            mul_input[0] = int(input("\nMasukkan faktor pengali usia (per 100)      : "))/100
            if 0 <= mul_input[0] <= 1:
                break
            else:
                print("Input tidak valid. Mohon masukkan angka antara 0 dan 100.")
        while True:
            mul_input[1] = int(input("Masukkan faktor pengali ras (per 100)       : "))/100
            if 0 <= mul_input[1] <= 1:
                 break
            else:
                print("Input tidak valid. Mohon masukkan angka antara 0 dan 100.")
        while True:
            mul_input[5] = int(input("Masukkan faktor pengali Agama (per 100)     : "))/100 
            if 0 <= mul_input[5] <= 1:
                 break
            else:
                print("Input tidak valid. Mohon masukkan angka antara 0 dan 100.")
        while True:
            mul_input[2] = int(input("Masukkan faktor pengali kampus (per 100)    : "))/100
            if 0 <= mul_input[2] <= 1:
                break
            else:
                print("Input tidak valid. Mohon masukkan angka antara 0 dan 100.")
        while True:
            mul_input[3] = int(input("Masukkan faktor pengali MBTI (per 100)      : "))/100
            if 0 <= mul_input[3] <= 1:
                 break
            else:
                print("Input tidak valid. Mohon masukkan angka antara 0 dan 100.")
        while True:
            mul_input[4] = int(input("Masukkan faktor pengali Fakultas (per 100)  : "))/100
            if 0 <= mul_input[4] <= 1:
                break
            else:
                print("Input tidak valid. Mohon masukkan angka antara 0 dan 100.")


        gr = sum(mul_input)
        if gr == 0: # Hindari pembagian dengan nol
            print("Jumlah faktor pengali tidak boleh nol. Mohon masukkan kembali.")
            mul = [-1 for t in range(6)] # Reset multipliers untuk memasukkan kembali
        else:
            for q in range (6): # Range diperbarui
                mul[q] = (mul_input[q] * 1)/gr # Hitung multiplier yang dinormalisasi
            if round(sum(mul),0) != 1:
                 print("Jumlah total faktor pengali harus 100 (setelah dibagi 100). Mohon masukkan kembali.")
                 mul = [-1 for t in range(6)] # Reset multipliers untuk memasukkan kembali
            else:
                break # Keluar dari loop ketika multipliers sudah valid
    except ValueError:
        print("Input tidak valid. Mohon masukkan angka untuk faktor pengali.")
        mul = [-1 for t in range(6)] # Reset multiplier untuk memasukkan data kembali


print("===================================================================================")
jodh = 0
# Gunakan dt_filtered_gender untuk mencari kecocokan setelah filtering gender awal
available_profiles = dt_filtered_gender[:] # Mulai dengan list yang sudah difilter gender

while jodh == 0:
    c = 0
    temp = -1 # Inisialisasi temp dengan nilai yang lebih rendah dari skor yang mungkin
    jodoh = "NULL"
    profil = None # Inisialisasi profil ke None

    if not available_profiles: # Cek apakah masih ada profil yang bisa dipertimbangkan untuk user
        print("Yah gak ada yang cocok 😞, semangat ya")
        break # Keluar dari loop utama jika tidak ada profil yang tersisa

    # Iterasi melalui profil yang tersedia untuk menemukan kecocokan terbaik
    for person in available_profiles:
        c = 0 # Reset skor untuk setiap orang

        # Hitung skor berdasarkan preferensi dan multipliers
        if r[1] <= person[2] <= r[2]:
            c += mul[0] * 5
        if person[3] in r[3]:
            c += mul[1] * 5
        if person[4] in r[4]:
            c += mul[3] * 5
        if person[5] in r[5]:
            c += mul[2] * 5
        if person[6] in r[8]:
            c += mul[4] * 5
        if person[9] in r[10]: 
             c += mul[5] * 5

        if c > temp:
            temp = c
            jodoh = person[0]
            profil = person

    if jodoh == "NULL": # Tidak ada kecocokan ditemukan di profil yang tersisa
        print("Yah gak ada yang cocok 😞, semangat ya")
        break # Keluar dari loop utama

    print("\nSelamat! Kamu paling cocok dengan:",jodoh+"!\nIni profilnya!\n===================================================================================\nNama          :", profil[0],"\nGender        :", profil[1],"\nUsia          :",profil[2]," tahun","\nRas           :",profil[3],"\nAgama         :",profil[9],"\nMBTI          :",profil[4],"\nKampus        :",profil[5],"\nFakultas      :",profil[6],"\nProfil        :",profil[7],"\n===================================================================================") # Added Agama to output and reordered

    confirm = str(input("Apakah anda terima? Y/N: "))

    if confirm.upper() == "Y":
        if ((profil[6] == "Bisnis" and r[9] == "Teknik") or (profil[6] == "Teknik" and r[9] == "Bisnis")):
            print("Wah, yakin nih?")
            an = input("(Y/N): ")
            if an.upper() == "N":
                # Hapus profil yang ditolak dari available_profiles
                available_profiles.remove(profil)
                jodh = 0 # Lanjutkan mencari
            elif an.upper() == "Y":
                print("Oke, semangat!")
                print(f"Selamat berbahagia!, {r[6]} dan {jodoh}. Kontak LINE-nya di {profil[8]}.\nSilakan mulai percakapan bareng si Dia!")
                jodh = 1 # Keluar dari loop
            else:
                print("Input tidak valid. Mohon masukkan Y atau N.")
                # Tetap di loop dan minta konfirmasi lagi
        else:
            print(f"Selamat berbahagia!, {r[6]} dan {jodoh}. Kontak LINE-nya di {profil[8]}.\nSilakan mulai percakapan bareng si Dia!")
            jodh = 1 # Keluar dari loop
    elif confirm.upper() == "N":
        # Hapus profil yang ditolak dari available_profiles
        available_profiles.remove(profil)
        jodh = 0 # Lanjutkan mencari
    else:
        print("Input tidak valid. Mohon masukkan Y atau N.")
        # Tetap di loop dan minta konfirmasi lagi
