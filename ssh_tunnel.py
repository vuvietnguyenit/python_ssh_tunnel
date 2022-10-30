import json
import subprocess

if __name__ == '__main__':
    # Read file from file host config
    f = open("host.json")  # Open file

    file = json.load(f)
    f.close()  # close file

    for line in file["hosts_tunnel"]:

        # Create server
        print(f"...Starting create tunnel: ({line['name']}) \n"
              f" {line['local_port_addrs']} <- {line['host']}:{line['remote_port_addrs']}")

        cmd = [
            "ssh", "-o", "ExitOnForwardFailure=yes", "-f", "-N", "-L",
            f"{line['local_port_addrs']}:{line['remote_host_addrs']}:{line['remote_port_addrs']}",
            f"{line['username']}@{line['host']}"
        ]
        try:
            subprocess.check_call(cmd)
            p = subprocess.Popen(cmd,
                                 stdout=subprocess.PIPE,
                                 stderr=subprocess.STDOUT)
            pid = p.pid + 1
            print("=> Success")
            retval = p.wait()
        except subprocess.CalledProcessError as sc:
            print("=> Failed. Error: ", sc)
