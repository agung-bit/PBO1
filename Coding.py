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
        Akun.masuk_akun()
    
    def Login(Username, Password):
        con = sqlite3.connect("database.db")
        cursor = con.cursor()
        query = 'SELECT Username, Password FROM [Data Akun] \
        where Username=\'%s\' and Password=\'%s\' '
        query = query % (Username, Password)
        cursor.execute(query)
        con.commit()
        row = cursor.fetchall()
        if (len(row)) == 0:
            print("Maaf Login Gagal, Mohon cek username & password anda")
        elif Username == row[0][0] and Password == row[0][1]:
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
        Akun.program_pegawai()

    def dataPasien():
        con = sqlite3.connect("database.db")
        cursor = con.cursor()
        query = 'SELECT * FROM [Data Klinik "Happy Health"]'
        cursor.execute(query)
        hasil = cursor.fetchall()
        con.commit()
        for i in hasil:
            print('-------------------------------------------')
            print('No.Id pasien :',i[0])
            print('Nama pasien :',i[1])
            print('Jenis kelamin pasien :',i[2])
            print('Usia pasien :',i[3])
            print('Alamat pasien :',i[4])
            print('Status Kewarganegaraan pasien :',i[5])
            print('Tempat, tanggal lahir pasien :',i[6])
            print('Penyakit pasien :',i[7])
            print('Dokter yang menangani pasien :',i[8])
            print('Agama pasien :',i[9])
            print('No.Telepon pasien :',i[10])
            print('Tanggal periksa pasien :',i[11])
            print('Jenis obat pasien :',i[12])
        con.close()
        Akun.program_pegawai()

class Akun:

    def masuk_akun():
        print('selamat datang di program klinik mata')
        print("""silahkan pilih angka sesuai fitur di bawah
        1. Buat akun baru
        2. Login
        3. batal / keluar""")
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
        Akun.program_pegawai()

    def program_pegawai():
        print("""silahkan pilih angka sesuai fitur di bawah
        1. Administrasi Pasien
        2. Data Pasien
        3. Menu Data Obat
        4. kembali ke menu akun
        5. keluar""")
        a=input('mohon input fitur sesuai angka :')
        if a=='1':
            print('Silahkan isi data data pasien dibawah ini')
            Nama = input('nama pasien :')
            Jenis_Kelamin = input('jenis kelamin :')
            Usia = input('usia :')
            Alamat = input('alamat :')
            Status_Kewarganegaraan = input('status kewarganegaraan :')
            Tempat_tanggal_lahir = input('tempat, tanggal lahir :')
            Penyakit = input('penyakit yang diderita :')
            Dokter = input('dokter yang menangani :')
            Agama = input('agama :')
            No_telepon = input('no.telepon :')
            Tanggal_Periksa = input('tanggal periksa :')
            Jenis_Obat = input('jenis obat :')
            Klinik.Administrasi(Nama, Jenis_Kelamin, Usia, Alamat, Status_Kewarganegaraan, Tempat_tanggal_lahir, Penyakit, Dokter, Agama, No_telepon, Tanggal_Periksa, Jenis_Obat)
        elif a=="2":
            Klinik.dataPasien()
        elif a=='3':
            Akun.obat()
        elif a=='4':
            Akun.masuk_akun()
        elif a=='5':
            print('terimakasih telah memakai program ini :)')
        else:print('inputan anda salah, mohon mulai ulang program')

    def obat():
        print("""silahkan pilih angka sesuai fitur di bawah
        1. Lihat stock obat
        2. Tambah data obat
        3. Edit data obat
        4. kembali ke menu pegawai
        5. keluar""")
        a=input('mohon input fitur sesuai angka :')
        if a=='1':
            print('Data Obat')
            obat.lihat()
        elif a=='2':
            print('input nama & jumlah stock obat')
            Nama_Obat = input('Nama obat :')
            Jumlah_Stock = input('stock obat :')
            obat.tambah(Nama_Obat, Jumlah_Stock)
        elif a=='3':
            print('input nama obat yang mau diedit stocknya')
            Nama_Obat = input('Nama obat :')
            obat.edit(Nama_Obat)
        elif a=='4':
            Akun.program_pegawai()
        elif a=='5':
            print('terimakasih telah memakai program ini :)')
        else:print('inputan anda salah, mohon mulai ulang program')

class obat():

    def lihat():
        con = sqlite3.connect("database.db")
        cursor = con.cursor()
        query = 'SELECT * FROM [Data Obat]'
        cursor.execute(query)
        hasil = cursor.fetchall()
        con.commit()
        for i in hasil:
            print('-------------------------------------------')
            print('No.Id Obat :',i[0])
            print('Nama Obat :',i[1])
            print('Jumlah Stock Obat :',i[2])
        Akun.obat()

    def tambah(Nama_Obat, Jumlah_Stock):
        con = sqlite3.connect("database.db")
        cursor = con.cursor()
        query = 'INSERT INTO [Data Obat] ([Nama Obat], [Jumlah Stock]) VALUES (\'%s\', \'%s\')' 
        query = query % (Nama_Obat, Jumlah_Stock)
        cursor.execute(query)
        con.commit()
        con.close()
        print("Data obat telah berhasil ditambah")
        Akun.obat()
    
    def edit(Nama_Obat):
        con = sqlite3.connect("database.db")
        cursor = con.cursor()
        query = 'SELECT [Nama Obat], [Jumlah Stock] FROM [Data Obat] where [Nama Obat]=\'%s\' '
        query = query % (Nama_Obat)
        cursor.execute(query)
        con.commit()
        row = cursor.fetchall()
        stock = input('input jumlah stock barang yang baru :')
        baru = stock[0][0]
        baru = stock
        query = 'UPDATE [Data Obat] SET [Jumlah Stock] = \'%s\' Where [Nama Obat] = \'%s\' ' 
        query = query % (baru, Nama_Obat)
        cursor.execute(query)
        con.commit()
        con.close()
        print("Data obat telah berhasil ditambah")
        Akun.obat()

#administrasi jenis obat
Akun.masuk_akun()