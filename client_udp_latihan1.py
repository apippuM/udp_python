import socket

soc = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

soc.settimeout(5)

try:

  # input user dan disimpan di variabel
  ip = input("Masukkan IP Server: ")
  port = int(input("Masukkan Port Server: "))
  pesan = input("Masukkan Pesan: ")

  # mengirim pesan ke server
  soc.sendto(pesan.encode('utf-8'), (ip, port))
  print(f'Pesan "{pesan}" telah dikirim ke {ip}:{port}')

  # menunggu respon server
  try:
    data, addr = soc.recvfrom(1024)
    print(f'Pesan dari server: {data.decode("utf-8")}')
  except socket.timeout:
    print("Timeout: Tidak ada respons dari server.")

except KeyboardInterrupt:
  print("\nProgram dihentikan oleh pengguna.")

finally:
  soc.close()
  print("Socket telah ditutup.")
