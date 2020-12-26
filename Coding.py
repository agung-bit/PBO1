import sqlite3

class Klinik:
    
    def membuatAkun(No_Id, Username, Password, Nama_Pegawai):
        con=sqlite3.connect("database.db")
        cur =con.cursor()
        query = 'INSERT INTO Akun (No_Id, Username, Password, Nama_Pegawai) \
            VALUES (\'%s\', \'%s\', \'%s\')' 
        query = query % (No_Id, Username, Password)
        cur.execute(query)
        con.commit()
        con.close()
        print("Membuat Akun Sukses")
    
    def login(Username, Password):
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
            print("Login Gagal")
        elif Username == rows[0][0] and Password == rows[0][1]:
            accept_Login = True
            print("Login Sukses")
            return Username
        
        con.close()

    def administrasi()