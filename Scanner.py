import socket 
import concurrent.futures
import time
import argparse



def parse_arguments():
    parser = argparse.ArgumentParser(description="Port Scanner")
    parser.add_argument("host")
    parser.add_argument("--start", type=int, default=1)
    parser.add_argument("--end", type=int, default=1024)
    return parser.parse_args()



def scan_socket(host, port):

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
   
def main():
    arg = parse_arguments()
    print(f"scanning ports on {arg.host} from {arg.start} to {arg.end}")

    start = time.perf_counter()
    with concurrent.futures.ThreadPoolExecutor(max_workers=50) as executor:
        for port in range(arg.start, arg.end + 1):
            executor.submit(scan_socket, arg.host, port)

    finish = time.perf_counter()
    print(f"Finished in {(finish - start):.5f} second(s)") 

if __name__ == "__main__":
    main()      