# Fungsi untuk membalik setiap kata dalam kalimat tanpa mengubah urutan katanya
def reverse_per_kata(kalimat):
    kata_list = kalimat.split() # Memisahkan kalimat menjadi list kata
    kata_terbalik = [kata[::-1] for kata in kata_list] # Membalik setiap kata
    return ' '.join(kata_terbalik) # Menggabungkan kembali menjadi kalimat

# Fungsi untuk mengurutkan kata-kata dalam kalimat sesuai indeks dalam list urutan
def urutkan_kalimat(kalimat, urutan):
    kata_list = kalimat.split() # Memisahkan kalimat menjadi list kata
    hasil = [kata_list[i - 1] for i in urutan] # Menyesuaikan indeks (karena urutan harus dimulai dari 1)
    return ' '.join(hasil) # Menggabungkan kembali menjadi kalimat

# Fungsi untuk mengganti huruf vokal dengan simbol tertentu
def ganti_vokal(kalimat, opsi):
    # Mapping pengganti vokal
    vokal_kecil = {'a': '4', 'i': '1', 'u': '|_|', 'e': '3', 'o': '0'} # Kamus pengganti untuk huruf vokal kecil
    vokal_besar = {'A': '4', 'I': '1', 'U': '|_|', 'E': '3', 'O': '0'} # Kamus pengganti untuk huruf vokal kapital
    hasil = "" # Variabel penampung hasil kalimat setelah diubah

    # Perulangan untuk memproses setiap karakter dalam kalimat
    for huruf in kalimat:
        # Jika opsi 1, cek dan ubah hanya vokal kecil
        if opsi == 1 and huruf in vokal_kecil:
            hasil += vokal_kecil[huruf]  # menambahkan versi simbol ke hasil
        # Jika opsi 2, cek dan ubah hanya vokal besar
        elif opsi == 2 and huruf in vokal_besar:
            hasil += vokal_besar[huruf]  # menambahkan versi simbol ke hasil
        else:
            # Jika bukan huruf vokal yang sesuai, tambahkan huruf asli
            hasil += huruf
    return hasil

print(reverse_per_kata("AKU CINTA KAMU"))
print(urutkan_kalimat("HARI INI SEDANG BELAJAR PYTHON", [5, 1, 4, 3, 2]))
print(ganti_vokal("Aku Cinta Kamu", 1))
print(ganti_vokal("Aku Cinta Kamu", 2))