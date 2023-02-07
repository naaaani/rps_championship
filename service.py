#!/usr/bin/env python3

from http.server import BaseHTTPRequestHandler, HTTPServer
import time
from match import Match
from urllib.parse import urlparse, parse_qs

hostName = "localhost"
serverPort = 8080

class MyServer(BaseHTTPRequestHandler):
 
    def do_GET(self):

        self.send_response(200)
        self.send_header("Content-type", "text/html")
        self.end_headers()
       
        query_components = parse_qs(urlparse(self.path).query)
        s1 = query_components["p1"][0]
        s2 = query_components["p2"][0] 
        
        winner = str(Match.get_winner_local(s1, s2))

        self.wfile.write(bytes(winner + "\n", "utf-8"))

if __name__ == "__main__":        
    webServer = HTTPServer((hostName, serverPort), MyServer)
    print("Server started http://%s:%s" % (hostName, serverPort))

    try: 
        webServer.serve_forever()
    except KeyboardInterrupt:
        pass

    webServer.server_close()
    print("Server stopped.")