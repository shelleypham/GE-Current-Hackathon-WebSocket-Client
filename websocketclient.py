import socket
import commands
import os
import sys

ic_websocket = "wss://ic-websocket-server.run.aws-usw02-pr.ice.predix.io/v2/events"
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((ic_websocket, 80))

ped_json = open("sample_ped.json", 'r')
s.send(ped_json)

s.recv(1024)
