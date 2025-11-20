class Dosen:
    def __init__(self, nama, nidn):
        self.nama = nama
        self.nidn = nidn

    def ajar_mata_kuliah(self, mata_kuliah):
        return f"Saya {self.nama} (NIDN: {self.nidn}) mengajar mata kuliah {mata_kuliah}"
        

# Instansiasi 2 object Dosen
dosen1 = Dosen("Lapu Tombi Layuk", "123456789")
dosen2 = Dosen("Abadi Nugroho", "987654321")

# Pemanggilan method
print(dosen1.ajar_mata_kuliah("Sistem Operasi"))
print(dosen2.ajar_mata_kuliah("Pemograman berorientasi"))
