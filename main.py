import sys
from collections import Counter


# ==================================================
# FUNGSI INPUT DATA INTEGER
# ==================================================

def input_integer(prompt: str) -> int:
    while True:
        try:
            nilai = int(input(prompt))
            return nilai
        except ValueError:
            print("Inputan tidak valid! Masukkan bilangan bulat (integer).")


# ==================================================
# FUNGSI MENGHITUNG USAHA EKSEKUSI BARIS KODE
# ==================================================

def hitung_usaha(fungsi, data):
    jumlah_kunjungan_baris = Counter()

    # Mengidentifikasi kode fungsi yang akan diukur
    kode_target = fungsi.__code__

    # Menyimpan tracer sebelumnya jika ada
    tracer_sebelumnya = sys.gettrace()

    # Fungsi pencatat eksekusi baris kode
    def tracer(frame, event, arg):

        # Hanya menghitung baris pada fungsi yang sedang diuji
        if frame.f_code is kode_target:

            # Menghitung setiap kejadian eksekusi baris
            if event == "line":

                # Nomor baris relatif terhadap isi fungsi
                nomor_baris = frame.f_lineno - kode_target.co_firstlineno

                jumlah_kunjungan_baris[nomor_baris] += 1

            return tracer

        return None

    # Mengaktifkan pencatatan eksekusi
    sys.settrace(tracer)

    try:
        hasil = fungsi(data)

    finally:
        # Mengembalikan kondisi tracing sebelumnya
        sys.settrace(tracer_sebelumnya)

    # Menjumlahkan seluruh kunjungan baris kode
    total_usaha = sum(jumlah_kunjungan_baris.values())

    return hasil, total_usaha, dict(sorted(jumlah_kunjungan_baris.items()))


# ==================================================
# ALGORITMA BUBBLE SORT
# ==================================================

def bubble_sort(data: list[int]) -> tuple[list[int], int, int]:

    hasil = data.copy()
    jumlah_perbandingan = 0
    jumlah_pertukaran = 0

    n = len(hasil)

    for i in range(n - 1):

        ada_pertukaran = False

        for j in range(n - i - 1):

            jumlah_perbandingan += 1

            if hasil[j] > hasil[j + 1]:

                hasil[j], hasil[j + 1] = hasil[j + 1], hasil[j]

                jumlah_pertukaran += 1
                ada_pertukaran = True

        if not ada_pertukaran:
            break

    return hasil, jumlah_perbandingan, jumlah_pertukaran


# ==================================================
# ALGORITMA INSERTION SORT
# ==================================================

def insertion_sort(data: list[int]) -> tuple[list[int], int, int]:

    hasil = data.copy()
    jumlah_perbandingan = 0
    jumlah_pergeseran = 0

    for i in range(1, len(hasil)):

        key = hasil[i]
        posisi = 0

        while posisi < i:

            jumlah_perbandingan += 1

            if hasil[posisi] > key:
                break

            posisi += 1

        j = i

        while j > posisi:

            hasil[j] = hasil[j - 1]
            jumlah_pergeseran += 1
            j -= 1

        hasil[posisi] = key

    return hasil, jumlah_perbandingan, jumlah_pergeseran

# ==================================================
# PROGRAM UTAMA
# ==================================================

def main():

    print("=" * 50)
    print("       PROGRAM BUBBLE SORT & INSERTION SORT")
    print("=" * 50)

    # Input jumlah data
    while True:

        jumlah_data = input_integer("Masukkan jumlah Data: ")

        if jumlah_data > 0:
            break

        print("Jumlah data harus lebih dari 0!")

    # Input elemen data
    data = []

    print("\nMasukkan data berupa bilangan bulat:")

    for i in range(jumlah_data):

        nilai = input_integer(f"Data ke-{i + 1}: ")
        data.append(nilai)

    # Menampilkan data awal
    print("\n" + "=" * 50)
    print("DATA SEBELUM DIURUTKAN")
    print("=" * 50)

    print("Data:", data)

    # ==================================================
    # MENJALANKAN BUBBLE SORT DAN MENGHITUNG USAHA
    # ==================================================

    (
        hasil_bubble_data,
        usaha_bubble,
        rincian_bubble
    ) = hitung_usaha(bubble_sort, data)

    (
        hasil_bubble,
        perbandingan_bubble,
        pertukaran_bubble
    ) = hasil_bubble_data

    total_bubble = perbandingan_bubble + pertukaran_bubble

    # ==================================================
    # MENJALANKAN INSERTION SORT DAN MENGHITUNG USAHA
    # ==================================================

    (
        hasil_insertion_data,
        usaha_insertion,
        rincian_insertion
    ) = hitung_usaha(insertion_sort, data)

    (
        hasil_insertion,
        perbandingan_insertion,
        pergeseran_insertion
    ) = hasil_insertion_data

    total_insertion = perbandingan_insertion + pergeseran_insertion

    # ==================================================
    # MENAMPILKAN HASIL BUBBLE SORT
    # ==================================================

    print("\n" + "=" * 50)
    print("HASIL BUBBLE SORT")
    print("=" * 50)

    print("Hasil pengurutan             :", hasil_bubble)
    print("Jumlah perbandingan          :", perbandingan_bubble)
    print("Jumlah pertukaran            :", pertukaran_bubble)
    print("Total langkah operasi        :", total_bubble)
    print("Usaha eksekusi baris kode    :", usaha_bubble)

    # ==================================================
    # MENAMPILKAN HASIL INSERTION SORT
    # ==================================================

    print("\n" + "=" * 50)
    print("HASIL INSERTION SORT")
    print("=" * 50)

    print("Hasil pengurutan             :", hasil_insertion)
    print("Jumlah perbandingan          :", perbandingan_insertion)
    print("Jumlah pergeseran            :", pergeseran_insertion)
    print("Total langkah operasi        :", total_insertion)
    print("Usaha eksekusi baris kode    :", usaha_insertion)

    # ==================================================
    # TABEL PERBANDINGAN KEDUA ALGORITMA
    # ==================================================

    print("\n" + "=" * 65)
    print("TABEL PERBANDINGAN BUBBLE SORT DAN INSERTION SORT")
    print("=" * 65)

    print(f"{'Metrik':<30} {'Bubble Sort':>15} {'Insertion Sort':>18}")
    print("-" * 65)

    print(f"{'Jumlah perbandingan':<30} {perbandingan_bubble:>15} {perbandingan_insertion:>18}")

    print(f"{'Pertukaran / Pergeseran':<30} {pertukaran_bubble:>15} {pergeseran_insertion:>18}")

    print(f"{'Total langkah operasi':<30} {total_bubble:>15} {total_insertion:>18}")

    print(f"{'Usaha eksekusi baris kode':<30} {usaha_bubble:>15} {usaha_insertion:>18}")

    print("=" * 65)

    # ==================================================
    # PENUTUP
    # ==================================================

    print("\n" + "=" * 50)
    print("PROGRAM SELESAI")
    print("=" * 50)


# Menjalankan program utama
if __name__ == "__main__":
    main()
