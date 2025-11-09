import pandas as pd

url = "https://github.com/AryxonDazmor/simple-phyton-project/raw/main/data_mahasiswa_dummy.xlsx"
dt = pd.read_excel(url, engine='openpyxl')

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
    print(anchovy)
    anchovy = anchovy.reset_index(drop=True)
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
# dt.loc[dt["Jurusan"] == 'Teknik', 'kecocokan'] += 1

gaysex = dt.sort_values(["kecocokan"],ascending=False)
print(gaysex[["Nama","Username","kecocokan"]])

agama = dt['Agama'].unique()
jurusan = dt['Jurusan'].unique()
univ = dt['Universitas'].unique()
etnis = dt['Etnis'].unique()


i = 0
w = 0
print("Jurusan")
for i in range (0,len(jurusan),2):
    print(f"{jurusan[i]} \t|  {jurusan[i+1]}")
    i = i+2
con = 0
while con != 'Y' and con != 'y':
    a = gaysex.head(1)
    con = input(f"Selamat kamu paling cocok dengan {a['Nama'].values[0]} dengan username {a['Username'].values[0]}\nApakah kamu mau menerimanya?\nY/N ")

    if con == 'Y' or con == 'y':
        print("Selamat kalian diterima bersama!")
    elif con == 'N' or con == 'n':
        gaysex = gaysex.drop(gaysex.index[0])