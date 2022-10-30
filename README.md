### Python SSH Tunnel tools

Sample tool for create ssh tunnel written by Python. It read content from host.json file and create connection
corresponding

**Schema**

```
- name: The name of the tunnel
- type: Type of the tunnel (Local, Remote)
- host: Remote host
- username: username for SSH
- password: password for SSH
- remote_host_addrs: host remote for tunnel
- remote_port_addrs: port remote for tunnel
- local_port_addrs: client port forwarder
```

**Example config**

```json
{
  "name": "Proxy tunnel",
  "type": "L",
  "host": "192.168.64.9",
  "username": "ubuntu",
  "remote_host_addrs": "127.0.0.1",
  "remote_port_addrs": 9999,
  "password": null,
  "local_port_addrs": 8181
}
```