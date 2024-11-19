gaji = int (input())
nikah = int (input())
anak = int (input())
if nikah == 1:
    print ((gaji * 100000) + 300000 + (anak * 100000))
elif nikah == 0:
    print ((gaji * 100000) + (anak * 100000))
