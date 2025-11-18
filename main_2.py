import pandas as pd
import sys
url = "https://github.com/AryxonDazmor/simple-phyton-project/raw/main/data_mahasiswa_dummy.xlsx"
dt = pd.read_excel(url, engine='openpyxl')
agama = dt['Agama'].unique()
jurusan = dt['Jurusan'].unique()
univ = dt['Universitas'].unique()
etnis = dt['Etnis'].unique()
mbtis = dt['MBTI'].unique()

pu = pd.read_excel(url, sheet_name = 1, engine='openpyxl')
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
                print("")
                print(">>>>>>Akun Anda berhasil dibuat!<<<<<<")
                print("")
                pw_matched = True
                new_acc = {
                    "Username": c[0],
                    "Password": c[1]
                }
                new_data = pd.DataFrame([new_acc])
                pu = pd.concat([pu, new_data], ignore_index=True)
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
    pu['pass korek'] = 0
    pu.loc[pu["Username"] == a[0], 'pass korek'] += 1
    pu.loc[pu["Password"] == a[1], 'pass korek'] += 1
    anchovy = pu.sort_values(["pass korek"],ascending=False)
    anchovy = anchovy.reset_index(drop=True)
    corpas = anchovy.loc[0, 'pass korek'] == 2
    if corpas == True:
        logged_in = True
        print("============================================")
        print("Selamat! Anda berhasil log in!")
        print("============================================")
        break
    else:
        logged_in = False
    if logged_in == False:
        print("Username atau Password salah")
dt['kecocokan'] = 0
print("============================================")
print("Silahkan isi data diri")
# Data diri
User = input("Nama Lengkap: ")
gender = 0
while gender != "Laki-Laki" or gender != "Perempuan":
    gender = input("Jenis Kelamin (L/P): ")
    if gender == "L" or gender == "l":
        gender = "Laki-Laki"
        dt = dt[dt["Jenis Kelamin"] == "Wanita"]
        break
    elif gender == "P" or gender == "p":
        gender = "Perempuan"
        dt = dt[dt["Jenis Kelamin"] == "Pria"]
        break
    else:
        print("Mohon masukkan L untuk Laki-Laki atau P untuk Perempuan.")
age = "I am Jokowi"
while True:
    try:
        age = int(input("Masukkan usia anda: "))
        break
    except ValueError:
        print("Mohon masukkan angka bulat untuk usia.")
if age <= 17:
    print("Maaf, anda belum cukup umur")
    sys.exit()

#Mulai input preferensi..
print("======================================================================\n                Masukkan Preferensi Pasangan Anda\n======================================================================")
while True:
    try:
        low_age = int(input("Batas bawah usia yang dicari: "))
        hi_age = int(input("Batas atas usia yang dicari: "))
        break
    except ValueError:
        print("Mohon masukkan angka bulat untuk usia.")
if low_age > hi_age:
    low_age, hi_age = hi_age, low_age
if low_age <= 17:
    print("Anda tidak dapat mencari pasangan di bawah umur, batas bawah usia dijadikan 18 tahun")
    low_age = 18
dt['age_cocok'] = 0
dt.loc[(dt["Usia"] >= low_age) & (dt["Usia"] <= hi_age), 'age_cocok'] += 1
def display(a):
    goyim = len(a)
    while goyim > 1:
        for i in range (0,goyim,2):
            while goyim > 1:
                print(f'- {a[i]}   \t- {a[i+1]}')
                i = i+2
                goyim = goyim - 2
    print("-",a[-1])
    return None
print("======================================================================")
print("Ras yang tersedia:")
display(etnis)
etnpil = "Test"
while etnpil == "Test":
    etnpil = str(input("Masukkan Etnis yang diinginkan (pisahkan dengan koma jika lebih dari satu): "))
    etnpil = [x.strip().capitalize() for x in etnpil.split(",")]
    invalid_etnpil = [g for g in etnpil if g not in etnis]
    if not etnpil or invalid_etnpil:
        if invalid_etnpil:     
            print(f"Input tidak valid. Ras berikut tidak ada dalam daftar: {', '.join(invalid_etnpil)}. Mohon masukkan salah satu dari daftar ras yang tersedia. Apakah anda mau tetap lanjut saja?")
            conpil = input("Y/N: ")
            if conpil == 'Y' or conpil == 'y':
                break
            if conpil == 'N' or conpil == 'n':
                etnpil = "Test"
        else:
            print("Input tidak valid. Mohon masukkan setidaknya satu Ras.")
        etnpil = "Test" # Reset supaya tetap di loop jika kosong
dt['etn_cocok'] = 0
for x in range (0,len(etnpil)):
    dt.loc[dt["Etnis"] == etnpil[x], 'etn_cocok'] += 1

print("===================================================================================")
i = 0
print("Jurusan yang tersedia:")

display(jurusan)
jurpil = "Test"
while jurpil == "Test":
    jurpil = str(input("Masukkan Jurusan yang diinginkan (pisahkan dengan koma jika lebih dari satu): "))
    jurpil = [x.strip().capitalize() for x in jurpil.split(",")]
    invalid_jurpil = [juru for juru in jurpil if juru not in jurusan]
    if not jurpil or invalid_jurpil:
        if invalid_jurpil:     
            print(f"Input tidak valid. Jurusan berikut tidak ada dalam daftar: {', '.join(invalid_jurpil)}. Mohon masukkan salah satu dari daftar jurusan yang tersedia. Apakah anda mau tetap lanjut saja?")
            conpil = input("Y/N: ")
            if conpil == 'Y' or conpil == 'y':
                break
            if conpil == 'N' or conpil == 'n':
                jurpil = "Test"
        else:
            print("Input tidak valid. Mohon masukkan setidaknya satu Jurusan.")
        upil = "Test" # Reset supaya tetap di loop jika kosong

dt['jur_cocok'] = 0
for x in range (0,len(jurpil)):
    dt.loc[dt["Jurusan"] == jurpil[x], 'jur_cocok'] += 1
print(jurpil)

print("===================================================================================")
display(univ)
upil = "gay"
while upil == "gay":
    upil = str(input("Masukkan Universitas yang diinginkan (pisahkan dengan koma jika lebih dari satu): "))
    upil = [x.strip().upper() for x in upil.split(",")]
    invalid_univ = [bakso for bakso in upil if bakso not in univ]
    print(invalid_univ)
    if not upil or invalid_univ:
        if invalid_univ:     
            print(f"Input tidak valid. Universitas berikut tidak ada dalam daftar: {', '.join(invalid_univ)}. Mohon masukkan salah satu dari daftar universitas yang tersedia. Apakah anda mau tetap lanjut saja?")
            conpil = input("Y/N: ")
            if conpil == 'Y' or conpil == 'y':
                break
            if conpil == 'N' or conpil == 'n':
                upil = "gay"
        else:
            print("Input tidak valid. Mohon masukkan setidaknya satu Universitas.")
        upil = "gay" # Reset supaya tetap di loop jika kosong
dt['u_cocok'] = 0
for x in range (0,len(upil)):
    dt.loc[dt["Universitas"] == upil[x], 'u_cocok'] += 1
print("===================================================================================")
mpil = "gay"
while mpil == "gay":
    mpil = str(input(f"MBTI dari pasangan yang Anda cari?\n- ENTJ      - INFP      - ESFJ\n- ENTP      - ISTP      - ISTJ\n- ISFP      - ENFJ      - ESTP\n- ENFP      - INFJ      - ESFP\n- ESTJ      - INTP      - INTJ\n- ISFJ\n(Pisahkan dengan koma jika pilihan Anda lebih dari 1)"))
    mpil = [x.strip().upper() for x in mpil.split(",")]
    invalid_mbti = [mbti for mbti in mpil if mbti not in mbtis]
    if not mpil or invalid_mbti: # Cek jika list kosong atau berisi MBTI yang tidak valid
        if invalid_mbti:     
            print(f"Input tidak valid. MBTI berikut tidak ada dalam daftar: {', '.join(invalid_mbti)}. Mohon masukkan salah satu dari daftar MBTI yang tersedia. Apakah anda mau tetap lanjut saja?")
            conpil = input("Y/N: ")
            if conpil == 'Y' or conpil == 'y':
                break
            if conpil == 'N' or conpil == 'n':
                mpil = "gay" # Reset supaya tetap di loop jika ada MBTI tidak valid
        else:
            print("Input tidak valid. Mohon masukkan setidaknya satu MBTI.")
        mpil = "gay" # Reset supaya tetap di loop jika kosong
dt['mbti_cocok'] = 0
for x in range (0,len(mpil)):
    dt.loc[dt["MBTI"] == mpil[x], 'mbti_cocok'] += 1
#Ngolah kecocokan
a = 96
while a < 0 or a > 1:
    try: 
        a = int(input("Masukkan faktor pengali usia (per 100)      : "))/100
        print(a)
        if a > 0 and a < 1:
            dt['kecocokan'] += dt['age_cocok'] * a
            break
    except ValueError:
        print("Mohon masukkan angka bulat antara 0-100")
b = 96
while b <= 0 or b >= 1:
    try:
        b = int(input("Masukkan faktor pengali jurusan (per 100)   : "))/100
        print(b)
        if b >= 0 and b <= 1:
            dt['kecocokan'] += dt["jur_cocok"] * b        
            break
    except ValueError:
        print("Mohon masukkan angka bulat antara 0-100")
a = 96
while a < 0 or a > 1:
    try:
        a = int(input("Masukkan faktor pengali etnis (per 100)   : "))/100
        print(a)
        if a >= 0 and a <= 1:
            dt['kecocokan'] += dt["etn_cocok"] * a
            break
    except ValueError:
        print("Mohon masukkan angka bulat antara 0-100")
a = 96        
while a < 0 or a > 1:
    try:
        a = int(input("Masukkan faktor pengali universitas (per 100)   : "))/100
        print(a)
        if a >= 0 and a <= 1:
            dt['kecocokan'] += dt["u_cocok"] * a
            break
    except ValueError:
        print("Mohon masukkan angka bulat antara 0-100")
a = 96        
while a < 0 or a > 1:
    try:
        a = int(input("Masukkan faktor pengali MBTI (per 100)   : "))/100
        print(a)
        if a >= 0 and a <= 1:
            dt['kecocokan'] += dt["mbti_cocok"] * a
            break
    except ValueError:  
        print("Mohon masukkan angka bulat antara 0-100")

pravda = dt.sort_values(["kecocokan"],ascending=False)
pravda = pravda.reset_index(drop=True)

#Hasil
con = 0
while con != 'Y' and con != 'y':
    a = pravda.head(1)
    con = input(f'Selamat kamu paling cocok dengan {a['Nama'].values[0]}! Berikut adalah profilnya:\n===================================================================================\nJenis Kelamin: {a['Jenis Kelamin'].values[0]} \nUsia: {a['Usia'].values[0]} \nAgama: {a['Agama'].values[0]}\nRas: {a['Etnis'].values[0]} \nMBTI: {a['MBTI'].values[0]}\nUniversitas: {a['Universitas'].values[0]}\nJurusan: {a['Jurusan'].values[0]}\n===================================================================================\nAbout: {a['Deskripsi'].values[0]}\nApakah kamu mau menerimanya?\nY/N ')
    while len(pravda) >= 1:
        if con == 'Y' or con == 'y':
            print("Selamat kalian diterima bersama!")
            print(f'Kamu bisa kontak {a['Nama'].values[0]} di LINE dengan username {a['Username'].values[0]}')
            break
        elif con == 'N' or con == 'n':
            pravda = pravda.drop(pravda.index[0])
    if len(pravda) == 0:
        print("Maaf, tidak ada kandidat lain yang sesuai dengan preferensi Anda.")
        break