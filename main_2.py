import pandas as pd
import sys
url = "https://github.com/AryxonDazmor/simple-phyton-project/raw/main/data_mahasiswa_dummy.xlsx"
dt = pd.read_excel(url, engine='openpyxl')
agama = dt['Agama'].unique().tolist()
jurusan = dt['Jurusan'].unique().tolist()
univ = dt['Universitas'].unique().tolist()
etnis = dt['Etnis'].unique().tolist()
mbtis = dt['MBTI'].unique().tolist()
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
    print(a)
    goyim = len(a)
    while goyim > 1:
        for i in range (0,goyim,2):
            while goyim > 1:
                print(f'- {a[i]}   \t- {a[i+1]}')
                i = i+2
                goyim = goyim - 2
    if goyim == 1:
        print("-",a[-1])
    return None
print("======================================================================")
print("Ras yang tersedia:")
display(etnis)

def ask(a,b,c): #a = abriveration, b buat displaynya, c ngambil list database
    display(c)
    h = "test"
    while h == "test":
        h = str(input(f"Masukkan {b} yang diinginkan! (Pisahkan dengan koma jika lebih dari satu): "))
        h = [x.strip().capitalize() for x in h.split(",")]
        tv = [g for g in h if g not in c] #as in, tidak valid
        if not h or tv:
            if tv:
                ccu = input(f"Input tidak valid. {b} berikut tidak ada dalam daftar: {', '.join(tv)}. Mohon masukkan salah satu dari daftar {b} yang tersedia. Apakah anda mau tetap lanjut saja? (Y/N): ")
                if ccu == "N" or ccu == 'n':
                    h = "test"
        dt[f'{a}_cocok'] = 0
        for x in range(0,len(h)):
            dt.loc[dt[b] == h[x],f'{a}_cocok'] += 1
        print("===================================================================================")
def askcap(a,b,c): #a = abriveration, b buat displaynya, c ngambil list database
    display(c)
    h = "test"
    while h == "test":
        h = str(input(f"Masukkan {b} yang diinginkan! (Pisahkan dengan koma jika lebih dari satu): "))
        h = [x.strip().upper() for x in h.split(",")]
        tv = [g for g in h if g not in c] #as in, tidak valid
        if not h or tv:
            if tv:
                ccu = input(f"Input tidak valid. {b} berikut tidak ada dalam daftar: {', '.join(tv)}. Mohon masukkan salah satu dari daftar {b} yang tersedia. Apakah anda mau tetap lanjut saja? (Y/N): ")
                if ccu == "N" or ccu == 'n':
                    h = "test"
        dt[f'{a}_cocok'] = 0
        for x in range(0,len(h)):
            dt.loc[dt[b] == h[x],f'{a}_cocok'] += 1
        print("===================================================================================")
agama = dt['Agama'].unique().tolist()
jurusan = dt['Jurusan'].unique().tolist()
univ = dt['Universitas'].unique().tolist()
etnis = dt['Etnis'].unique().tolist()
mbtis = dt['MBTI'].unique().tolist()
ask('etn','Etnis',etnis)
ask('agm','Agama',agama)
ask('jur','Jurusan',jurusan)
askcap('u','Universitas',univ)
askcap('mbti','MBTI',mbtis)

def cocok(a,b):
    g = 12
    while g < 0 or g > 1:
        try: 
            g = int(input(f"Masukkan faktor pengali {a} (per 100) \t:")) / 100
            if g >= 0 and g <= 1:
                dt['kecocokan'] += dt[f'{b}_cocok'] * g
            else:
                print("Nilai harus di antara 0 sampai 100!")
                g = 12
        except ValueError:
            print("Masukkan angka!")
            g = 12

cocok('usia','age')
cocok('jurusan','jur')
cocok('etnis','etn')
cocok('universitas','u')
cocok('MBTI','mbti')

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
        else:
            print("Mohon masukkan 'Y' atau 'N'!")
            con = 0
    if len(pravda) == 0:
        print("Maaf, tidak ada kandidat lain yang sesuai dengan preferensi Anda.")
        break