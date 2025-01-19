from abc import ABC, abstractmethod
import datetime

# اینترفیس سرور اصلی
class ServerInterface(ABC):
    
    @abstractmethod
    def process_request(self, request: str):
        pass


# سرور اصلی
class RealServer(ServerInterface):
    
    def process_request(self, request: str):
        return f"Processing request: {request}"


# Proxy که وظیفه لاگ‌گیری را انجام می‌دهد
class ProxyServer(ServerInterface):
    
    def __init__(self, real_server: RealServer):
        self.real_server = real_server
    
    def log_request(self, request: str):
        # این متد برای لاگ‌گیری هر درخواست استفاده می‌شود
        with open('server_logs.txt', 'a') as log_file:
            timestamp = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
            log_file.write(f"{timestamp} - Request: {request}\n")
        print(f"Logged request: {request}")
    
    def process_request(self, request: str):
        # ابتدا لاگ‌گیری انجام می‌شود
        self.log_request(request)
        
        # سپس درخواست به سرور واقعی فرستاده می‌شود
        response = self.real_server.process_request(request)
        
        return response


# شبیه‌سازی کارکرد
if __name__ == "__main__":
    # ساخت یک سرور واقعی
    real_server = RealServer()
    
    # ساخت Proxy برای سرور
    proxy_server = ProxyServer(real_server)
    
    # پردازش یک درخواست
    print(proxy_server.process_request("User request 1"))
    print(proxy_server.process_request("User request 2"))
