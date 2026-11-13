def input_integer(prompt: str) -> int:
  while True:
    try:
      nilai = int(input(prompt))
      return nilai
    except ValueError:
      print("Inputan tidak valid! Masukkan bilangan bulat (integer).")

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

def insertion_sort(data: list[int]) -> tuple[list[int], int, int]:
  hasil = data.copy()
  jumlah_perbandingan  = 0
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

def main():
  print("=" * 45)
  print("    PROGRAM BUBBLE SORT & INSERTION SORT")
  print("=" * 45)

  while True:
    jumlah_data = input_integer("Masukkan jumlah Data: ")
    if jumlah_data > 0:
      break
    print("Jumlah data harus lebih dari 0!")

  data = []
  print("\nMasukkan data berupa bilangan bulat:")
  for i in range(jumlah_data):
    nilai = input_integer(f"Data ke-{i + 1}: ")
    data.append(nilai)

  print("\n" + "=" * 45)
  print("DATA SEBELUM DIURUTKAN")
  print("=" * 45)

  print("Data: ",data)

  hasil_bubble, perbandingan_bubble, pertukaran_bubble = bubble_sort(data)
  total_bubble = perbandingan_bubble + pertukaran_bubble

  hasil_insertion, perbandingan_insertion, pergeseran_insertion = insertion_sort(data)
  total_insertion = perbandingan_insertion + pergeseran_insertion

  # Menampilkan hasil Bubble Sort
  print("\n" + "=" * 45)
  print("HASIL BUBBLE SORT")
  print("=" * 45)

  print("Hasil pengurutan       :", hasil_bubble)
  print("Jumlah perbandingan    :", perbandingan_bubble)
  print("Jumlah pertukaran      :", pertukaran_bubble)
  print("Total langkah          :", total_bubble)

  # Menampilkan hasil Insertion Sort
  print("\n" + "=" * 45)
  print("HASIL INSERTION SORT")
  print("=" * 45)

  print("Hasil pengurutan       :", hasil_insertion)
  print("Jumlah perbandingan    :", perbandingan_insertion)
  print("Jumlah pergeseran      :", pergeseran_insertion)
  print("Total langkah          :", total_insertion)

  print("\n" + "=" * 45)
  print("PROGRAM SELESAI")
  print("=" * 45)

if __name__ == "__main__":
    main()
