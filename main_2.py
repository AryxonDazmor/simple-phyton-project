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
etnpil = str(input("Masukkan etnis yang diinginkan (pisahkan dengan koma jika lebih dari satu): "))
etnpil = [x.strip().capitalize() for x in etnpil.split(",")]
dt['etn_cocok'] = 0
for x in range (0,len(etnpil)):
    dt.loc[dt["Etnis"] == etnpil[x], 'etn_cocok'] += 1
print(etnpil)

print("===================================================================================")
i = 0
print("Jurusan yang tersedia:")

for i in range (0,len(jurusan),2):
    print(f"{jurusan[i]}   \t|  {jurusan[i+1]}")
    i = i+2
jurpil = str(input("Masukkan jurusan yang diinginkan (pisahkan dengan koma jika lebih dari satu): "))
jurpil = [x.strip().capitalize() for x in jurpil.split(",")]
dt['jur_cocok'] = 0
for x in range (0,len(jurpil)):
    dt.loc[dt["Jurusan"] == jurpil[x], 'jur_cocok'] += 1
print(jurpil)

print("===================================================================================")
for i in range (0,len(univ),2):
    w = len(univ)
    print(w)
    while w != 1:
        print(f"{univ[i]}   \t|  {univ[i+1]}")
        i = i+2
        w = w-2
    else: 
        print(f"{univ[i]}")
        break
upil = str(input("Masukkan Universitas yang diinginkan (pisahkan dengan koma jika lebih dari satu): "))
upil = [x.strip().upper() for x in upil.split(",")]
dt['u_cocok'] = 0
for x in range (0,len(upil)):
    dt.loc[dt["Universitas"] == upil[x], 'u_cocok'] += 1
print(upil)
print("===================================================================================")
mpil = str(input(f"MBTI dari pasangan yang Anda cari?\n- ENTJ      - INFP      - ESFJ\n- ENTP      - ISTP      - ISTJ\n- ISFP      - ENFJ      - ESTP\n- ENFP      - INFJ      - ESFP\n- ESTJ      - INTP      - INTJ\n- ISFJ\n(Pisahkan dengan koma jika pilihan Anda lebih dari 1)"))
mpil = [x.strip().upper() for x in mpil.split(",")]
dt['mbti_cocok'] = 0
for x in range (0,len(mpil)):
    dt.loc[dt["MBTI"] == mpil[x], 'mbti_cocok'] += 1
#Ngolah kecocokan
a = 96
while a < 0 or a > 1:
    a = int(input("Masukkan faktor pengali usia (per 100)      : "))/100
    print(a)
    if a > 0 and a < 1:
        dt['kecocokan'] += dt['age_cocok'] * a
        break
b = 96
while b <= 0 or b >= 1:
    b = int(input("Masukkan faktor pengali jurusan (per 100)   : "))/100
    print(b)
    if b >= 0 and b <= 1:
        dt['kecocokan'] += dt["jur_cocok"] * b        
        break
a = 96
while a < 0 or a > 1:
    a = int(input("Masukkan faktor pengali etnis (per 100)   : "))/100
    print(a)
    if a >= 0 and a <= 1:
        dt['kecocokan'] += dt["etn_cocok"] * a
a = 96        
while a < 0 or a > 1:
    a = int(input("Masukkan faktor pengali universitas (per 100)   : "))/100
    print(a)
    if a >= 0 and a <= 1:
        dt['kecocokan'] += dt["u_cocok"] * a
a = 96        
while a < 0 or a > 1:
    a = int(input("Masukkan faktor pengali MBTI (per 100)   : "))/100
    print(a)
    if a >= 0 and a <= 1:
        dt['kecocokan'] += dt["mbti_cocok"] * a


pravda = dt.sort_values(["kecocokan"],ascending=False)
pravda = pravda.reset_index(drop=True)
print(pravda)


#Hasil
con = 0
while con != 'Y' and con != 'y':
    a = pravda.head(1)
    con = input(f"Selamat kamu paling cocok dengan {a['Nama'].values[0]} dengan username {a['Username'].values[0]}\nApakah kamu mau menerimanya?\nY/N ")

    if con == 'Y' or con == 'y':
        print("Selamat kalian diterima bersama!")
    elif con == 'N' or con == 'n':
        pravda = pravda.drop(pravda.index[0])