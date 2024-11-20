import socket

# Create a UDP socket
soc = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# Set a timeout for the socket
soc.settimeout(5)  # Timeout after 5 seconds

try:
  # Input server details
  ip = input("Masukkan IP Server: ")
  port = int(input("Masukkan Port Server: "))
  pesan = input("Masukkan Pesan: ")

  # Send message to server
  soc.sendto(pesan.encode('utf-8'), (ip, port))
  print(f'Pesan "{pesan}" telah dikirim ke {ip}:{port}')

  # Wait for server response
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
