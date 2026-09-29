# Input: suku pertama (a), beda (d), dan banyak suku (n).
# Proses: menghasilkan setiap suku dengan perulangan for dan menjumlahkannya.
# Kondisi berhenti: perulangan berhenti setelah menghasilkan n suku.
# Output: nomor, nilai setiap suku, dan jumlah seluruh suku.

print("Deret Aritmetika")

a = float(input("Suku pertama a: "))
d = float(input("Beda d: "))

n = int(input("Banyak suku n: "))

while n <= 0:
    print("Banyak suku harus positif.")
    n = int(input("Banyak suku n: "))

total = 0

for i in range(n):
    suku = a + i * d
    total += suku
    print(f"Suku ke-{i + 1} = {suku:.2f}")

print(f"Jumlah deret = {total:.2f}")