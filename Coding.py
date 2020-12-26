import sqlite3

class Klinik:
    
    def BuatAkun(Username, Password, Nama_Pegawai):
        con=sqlite3.connect("database.db")
        cur =con.cursor()
        query = 'INSERT INTO Akun (Username, Password, Nama_Pegawai) \
            VALUES (\'%s\', \'%s\', \'%s\')' 
        query = query % (Username, Password, Nama_Pegawai)
        cur.execute(query)
        con.commit()
        con.close()
        print("Akun Telah Sukses Dibuat")
    
    def Login(Username, Password):
        con=sqlite3.connect("database.db")
        cur =con.cursor()
        query = 'SELECT Username, Password FROM Akun \
        where Username=\'%s\' and Password=\'%s\' '
        query = query % (Username, Password)
        cur.execute(query)
        con.commit()
        rows =cur.fetchall()
        accept_Login = True
        if (len(rows)) == 0:
            accept_Login = False

        if accept_Login == False:
            print("Maaf Login Gagal, Mohon cek username & password anda")
        elif Username == rows[0][0] and Password == rows[0][1]:
            accept_Login = True
            print("Login Sukses")
            return Username
        
        con.close()

    def Administrasi(Nama, Jenis_Kelamin, Usia, Alamat, Status_Kewarganegaraan, Tempat_tanggal_lahir, Penyakit, Dokter, Agama, No_telepon, Tanggal_Periksa, Jenis_Obat):
        con=sqlite3.connect("database.db")
        cur =con.cursor()
        query = 'INSERT INTO Data Klinik "Happy Health" (Nama, [Jenis Kelamin], Usia, Alamat, [Status Kewarganegaraan], [Tempat tanggal lahir], Penyakit, Dokter, Agama, [No telepon], [Tanggal Periksa], [Jenis Obat]) \
            VALUES (\'%s\', \'%s\', \'%s\', \'%s\', \'%s\', \'%s\', \'%s\', \'%s\', \'%s\', \'%s\', \'%s\', \'%s\')' 
        query = query % (Nama, Jenis_Kelamin, Usia, Alamat, Status_Kewarganegaraan, Tempat_tanggal_lahir, Penyakit, Dokter, Agama, No_telepon, Tanggal_Periksa, Jenis_Obat)
        cur.execute(query)
        con.commit()
        con.close()
        print("Data pasien berhasil diunggah")
