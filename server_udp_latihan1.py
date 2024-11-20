import socket

# Create a UDP socket
soc = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
soc.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

try:
  # Bind to all available interfaces on port 200
  soc.bind(("0.0.0.0", 200))
  print("Server is running and listening on port 200...")

  while True:
    try:
      # Receive data from a client
      data, addr = soc.recvfrom(1024)
      print(f"Pesan dari {addr}: {data.decode('utf-8')}")

      # Process the received message
      if not data:
        print("Tidak ada data yang diterima, menghentikan server...")
        break

      pesan_user = data.decode('utf-8').strip()
      jawaban = len(pesan_user)

      # Respond back to the client
      response = f"Data yang dikirim: {pesan_user}, dengan jumlah karakter: {jawaban}"
      soc.sendto(response.encode('utf-8'), addr)
      
    except KeyboardInterrupt:
      print("\nProgram dihentikan oleh pengguna.")
        
except KeyboardInterrupt:
    print("\nProgram dihentikan oleh pengguna.")

finally:
    soc.close()
    print("Socket telah ditutup.")
