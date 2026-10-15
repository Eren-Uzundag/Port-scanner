import socket 
import concurrent.futures
import time

start = time.perf_counter()

def create_socket(host, port):

    try:
     with  socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.settimeout(5)
        a = s.connect_ex((host, port))
        
        if a == 0:
            print(f"port {port} is open on {host}")

        else:
              pass   
                
    except Exception as e:
        print(f"An error occurred: {e}")  
   
#Farklı port taramalarını paralel olarak gerçekleştimek için iş kodunu ThreadPoolExecutor ile çalıştırıyoruz.
with concurrent.futures.ThreadPoolExecutor(max_workers=50) as executor:
    for port in range(1,  1025):
        executor.submit(create_socket, "localhost", port)

finish = time.perf_counter()
print(f"Finished in {(finish - start):.5f} second(s)")