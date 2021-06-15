#program Kelulusan
nilai_teori = int(input("Nilai ujian teori: "))
nilai_praktek = int(input("Nilai ujian praktek: "))

#If else
if nilai_teori >= 70 and nilai_praktek >= 70:
    print("selammat, anda lulus.")
elif nilai_teori >= 70 and nilai_praktek < 70:
    print("anda harus mengulang ujian praktek.")
elif nilai_teori < 70 and nilai_praktek >= 70:
    print("Anda harus mengulang ujian teori.")
else:
    print("Anda harus mengulang ujian teori dan praktek.")

