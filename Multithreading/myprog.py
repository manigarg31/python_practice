import redis
import http.client
from concurrent.futures import ThreadPoolExecutor

def get_data():
    r = redis.Redis(host='localhost', port=6379)
    data= r.zpopmax('queue')
    conn = http.client.HTTPConnection('localhost',8000)
    conn.request("GET","/")
    response= conn.getresponse()
def main():
    executor = ThreadPoolExecutor(50)
    while True:
        a= executor.submit(get_data)
        print(a)

if __name__ == '__main__':
    #print(data)
    main()
