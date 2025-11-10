import pandas as pd
import sys
url = "https://github.com/AryxonDazmor/simple-phyton-project/raw/main/data_mahasiswa_dummy.xlsx"
dt = pd.read_excel(url, engine='openpyxl')
agama = dt['Agama'].unique()
jurusan = dt['Jurusan'].unique()
univ = dt['Universitas'].unique()
etnis = dt['Etnis'].unique()

pu = pd.read_excel(url, sheet_name = 1, engine='openpyxl')
print(pu)
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
                print(pu)
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
    print(anchovy)
    corpas = anchovy.loc[0, 'pass korek'] == 2
    print(corpas)
    if corpas == True:
        logged_in = True
        break
    else:
        logged_in = False
    if logged_in == False:
        print("Username atau Password salah")
dt['kecocokan'] = 0

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
low_age = int(input("Batas bawah usia yang dicari: "))
hi_age = int(input("Batas atas usia yang dicari: "))

if low_age > hi_age:
    low_age, hi_age = hi_age, low_age
if low_age <= 17:
    print("Anda tidak dapat mencari pasangan di bawah umur")
    low_age = 18
dt['age_cocok'] = 0
dt.loc[(dt["Usia"] >= low_age) & (dt["Usia"] <= hi_age), 'age_cocok'] += 1
print("======================================================================")
print("Ras yang tersedia:")
for i in range (0,len(etnis),2):
    print(f"{etnis[i]}   \t|  {etnis[i+1]}")
    i = i+2

pravda = dt.sort_values(["kecocokan"],ascending=False)

i = 0
print("Jurusan")
for i in range (0,len(jurusan),2):
    print(f"{jurusan[i]}   \t|  {jurusan[i+1]}")
    i = i+2
con = 0
while con != 'Y' and con != 'y':
    a = pravda.head(1)
    con = input(f"Selamat kamu paling cocok dengan {a['Nama'].values[0]} dengan username {a['Username'].values[0]}\nApakah kamu mau menerimanya?\nY/N ")

    if con == 'Y' or con == 'y':
        print("Selamat kalian diterima bersama!")
    elif con == 'N' or con == 'n':
        pravda = pravda.drop(pravda.index[0])