import sqlite3

class Klinik:
    
    def BuatAkun(Username, Password, Nama_Pegawai):
        con = sqlite3.connect("database.db")
        cursor = con.cursor()
        query = 'INSERT INTO [Data Akun] (Username, Password, [Nama Pegawai]) \
            VALUES (\'%s\', \'%s\', \'%s\')' 
        query = query % (Username, Password, Nama_Pegawai)
        cursor.execute(query)
        con.commit()
        con.close()
        print("Akun Telah Sukses Dibuat")
    
    def Login(Username, Password):
        con = sqlite3.connect("database.db")
        cursor = con.cursor()
        query = 'SELECT Username, Password FROM [Data Akun] \
        where Username=\'%s\' and Password=\'%s\' '
        query = query % (Username, Password)
        cursor.execute(query)
        con.commit()
        rows = cursor.fetchall()
        accept_Login = True
        if (len(rows)) == 0:
            accept_Login = False

        if accept_Login == False:
            print("Maaf Login Gagal, Mohon cek username & password anda")
        elif Username == rows[0][0] and Password == rows[0][1]:
            accept_Login = True
            print("Login Sukses")
            Akun.program(Username)      
        con.close()

    def Administrasi(Nama, Jenis_Kelamin, Usia, Alamat, Status_Kewarganegaraan, Tempat_tanggal_lahir, Penyakit, Dokter, Agama, No_telepon, Tanggal_Periksa, Jenis_Obat):
        con = sqlite3.connect("database.db")
        cursor = con.cursor()
        query = 'INSERT INTO [Data Klinik "Happy Health"] (Nama, [Jenis Kelamin], Usia, Alamat, [Status Kewarganegaraan], [Tempat tanggal lahir], Penyakit, Dokter, Agama, [No telepon], [Tanggal Periksa], [Jenis Obat]) \
            VALUES (\'%s\', \'%s\', \'%s\', \'%s\', \'%s\', \'%s\', \'%s\', \'%s\', \'%s\', \'%s\', \'%s\', \'%s\')' 
        query = query % (Nama, Jenis_Kelamin, Usia, Alamat, Status_Kewarganegaraan, Tempat_tanggal_lahir, Penyakit, Dokter, Agama, No_telepon, Tanggal_Periksa, Jenis_Obat)
        cursor.execute(query)
        con.commit()
        con.close()
        print("Data pasien berhasil diunggah")

class Akun:
    def masuk_akun():
        print('selamat datang di program klinik mata')
        print("""silahkan pilih angka sesuai fitur di bawah
        1. Buat akun baru
        2. Login
        3. batal""")
        a=input('mohon input fitur sesuai angka :')
        if a=='1':
            print('Anda akan membuat akun baru, silahkan isi datadiri anda')
            Username = input('input username anda :')
            Password = input('input password anda :')
            Nama_Pegawai = input('input nama anda :')
            Klinik.BuatAkun(Username, Password, Nama_Pegawai)
        elif a=='2':
            print('silahkan login menggunakan username & password anda')
            Username = input('input username anda :')
            Password = input('input password anda :')
            Klinik.Login(Username,Password)
        elif a=='3':
            print('terimakasih telah memakai program ini :)')
        else:print('inputan anda salah, mohon mulai ulang program')

    def program(Username):
        con = sqlite3.connect("database.db")
        cursor = con.cursor()
        query = 'SELECT [Nama Pegawai] FROM [Data Akun] where Username=\'%s\' ' 
        query = query % (Username)
        cursor.execute(query)
        con.commit()
        rows = cursor.fetchall()
        print('selamat datang',rows[0][0])
        con.close()
      
Akun.masuk_akun()