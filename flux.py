#!/usr/bin/env python3

import json
import subprocess
import time

with open('peers.json', 'r') as f:
    peers = json.load(f)['peers']

# Set the initial index
index = 0

while True:
    peer = peers[index]

    name = peer['name']
    public_key = peer['public_key']
    endpoint_address = peer['endpoint_address']
    allowed_ips = peer['allowed_ips']

    cmd = f'sudo wg set wg1 peer {public_key} endpoint {endpoint_address} allowed-ips {allowed_ips} persistent-keepalive 20'
    subprocess.run(cmd, shell=True)
    print(f'Connected to {name}')

    index = (index + 1) % len(peers)
    time.sleep(60)

