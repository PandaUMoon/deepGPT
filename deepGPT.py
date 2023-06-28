import http.server
import socketserver

PORT = 8000  # 设置端口号为8000
DIRECTORY = '.'  # 设置文件目录为当前目录

# 启动HTTP服务器
Handler = http.server.SimpleHTTPRequestHandler
with socketserver.TCPServer(("", PORT), Handler) as httpd:
    print("Serving at port", PORT)
    httpd.serve_forever()