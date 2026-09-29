# Pertemuan 05 Perulangan Python

Nama: Maulyditha Revania Aprilliyanti
NIM: 2225250100
Kelas: 3A

## Tujuan

Menggunakan `for` dan `while` untuk menyelesaikan masalah iteratif.

## Cara Menjalankan

```bash
python3 kuis/kuis2_deret_aritmetika.py
```

## Algoritma Kuis 2

Program membaca suku pertama `a`, beda `d`, dan banyak suku `n`. Nilai `n` divalidasi menggunakan `while` agar harus bernilai positif. Setelah itu, program menggunakan `for` sebanyak `n` kali untuk menghitung setiap suku deret aritmetika dengan `a + i * d`. Setiap suku ditambahkan ke `total`, kemudian jumlah akhirnya ditampilkan dengan dua angka di belakang koma.

## Hasil Pengujian

| No. | Input (a, d, n) | Keluaran yang Diharapkan      | Keluaran Aktual                              | Status   |
| --- | --------------- | ----------------------------- | -------------------------------------------- | -------- |
| 1   | 2, 3, 5         | 2, 5, 8, 11, 14; jumlah 40.00 | 2.00, 5.00, 8.00, 11.00, 14.00; jumlah 40.00 | Berhasil |
| 2   | 10, -2, 4       | 10, 8, 6, 4; jumlah 28.00     | 10.00, 8.00, 6.00, 4.00; jumlah 28.00        | Berhasil |
| 3   | 1.5, 0.5, 3     | 1.5, 2.0, 2.5; jumlah 6.00    | 1.50, 2.00, 2.50; jumlah 6.00                | Berhasil |

## Refleksi

Kesalahan yang perlu diperhatikan adalah penempatan `total = 0`. Jika variabel tersebut diletakkan di dalam perulangan, nilai total akan direset pada setiap iterasi sehingga hasil penjumlahan menjadi tidak benar. Perbaikannya adalah menginisialisasi `total = 0` sebelum `for` dimulai.

Validasi `n` menggunakan `while` karena program perlu terus meminta input sampai pengguna memasukkan nilai positif. Perulangan `for` menggunakan `range(n)` sehingga jumlah iterasi selalu tepat sebanyak `n` kali.
