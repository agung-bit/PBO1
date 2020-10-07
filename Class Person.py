class Person():
    def __init__(self, nama, kelamin, alamat, hobby):
        self.nama = nama
        self.kelamin = kelamin
        self.alamat = alamat
        self.hobby = hobby
    
    def set_nama(self, nama_baru):
        self.nama = nama_baru

    def get_nama(self):
        return self.nama

Person1 = Person('Agung', 'pria', 'BWI', 'Olga')
print(Person1.get_nama())
Person1.set_nama('Rizqi')
print(Person1.get_nama())