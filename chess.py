#!/bin/python

# Copyright:
# 
# Joshua Marshall Moore
# 108 Texas Ave
# Alamogordo, New Mexico 88310
# United States
# Earth

from wsgiref.simple_server import make_server
from cgi import parse_qs
import json
import re
import SimpleHTTPServer
import SocketServer
import BaseHTTPServer
from sys import argv

def incSynchronized(item):
    item['synchronized'] += 1

class ChessBoardServer(SimpleHTTPServer.SimpleHTTPRequestHandler):
    def __init__(self):

        self.players = {
            'black': None,
            'white': None
        }

        self.colors = players.keys()
        self.moves = []
        self.previous_move = {'piece': None, 'move': None, 'synchronized': 0}

    # warning, potential inefficiency due to concatenation
    def shift(self, l, n):
        return l[n:].append(l[:n])

    def register(self):
    
        d = parse_qs(self.path)

        ####### debug #######
        print d
        ####### debug #######

        assigned = False
        count = 0
        while not assigned and count < 1:
            color = d['desired'] # returns the first item called 'desired'
            # color = d.get('desired', []) # retuns a list of all items called 'desired'        
    
            while color is not self.colors[0]:
                colors = self.shift(self.colors)
    
                if players[self.colors[0]] is None:
                    players[self.colors[0]] = self.client_address(environ)
            
                self.colors = self.shift(self.colors, 1)

        return json.dumps({registration: color})

    def move(self):
        self.d = parse_qs(self.piece)
        piece = d.get('piece', [''])
        move = d.get('move', [''])
        side = d.get('side', [''])

        self.moves.append({
            'piece': piece, 
            'move': move, 
            'synchronized': []
        })
        self.moves[-1]['synchronized'].append(side)
        
        self.side = side
        return previous(self)

    def previous(self):
        d = parse_qs(self.path)
        side = None
        if self.side:
            side = self.side
        else:
            side = d.get('side', [''])

        i = 0
        for move in self.moves:
            if side not in move['synchronized']:
                return json.dumps(self.moves[i:])
            else:
                i += 1


    def not_found(environ, start_response):
        start_response('404 NOT FOUND', [('Content-Type', 'text/plain')])
        return ['Ohsno!!!']
        
        return not_found(environ, start_response)

    def do_GET(self):

        path = self.path.lstrip('/')
        self.urls = [
          (r'register/?$', self.register),
          (r'move/?$', self.move),  
          (r'previous/?$', self.previous)
        ]
        for regex, callback in self.urls:
            match = re.search(regex, self.path)
            if match is not None:
                content = None
                if match[0] is 'register':
                    content = self.register()
                if match[0] is 'move':
                    content = self.move()
                if match[0] is 'previous':
                    content = self.previous()
                self.send_response(200)
                self.send_header('Content-type', 'text/json')
                self.send_header('Content-length', len(content))
                self.end_headers()
                self.wfile.write(content)
        
        return super.do_GET()        

if __name__ == '__main__':
    httpd = SocketServer.TCPServer(('localhost', int(argv[1])), BaseHTTPServer)
    httpd.serve_forever()


# setup servers

