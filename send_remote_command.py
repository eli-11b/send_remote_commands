import os
import paramiko
import time
import getpass
import argparse

# add arguments hostip and command
parser = argparse.ArgumentParser()
parser.add_argument('--method', help="Method being used")
parser.add_argument('--hostip', help="The ip address you are targeting")
parser.add_argument('--port', default='22', help="the port for the target")
parser.add_argument('--command', help="The command you want to send to target")
parser.add_argument('--use_key', default=False,
                    help="Whether or not you want to use the ssh-key once set up. If TRUE no need to use password")
args = parser.parse_args()

## - variables - ##
hostip = args.hostip
port = args.port
command = args.command
use_key = args.use_key
method = args.method
NOW = str(time.strftime("%Y-%m-%d-%H-%M"))
# the filename for the file itself
myownname = os.path.splitext(os.path.basename(__file__))[0]


def log(msg, filename=f"{myownname}_log.txt"):
    """
    SUMMARY:
        logs message to file, defaults to filename that is named after the file that this function is placed in with _log appended.
    ARGS:
        msg (str): The message to be logged.
        filename (path): the filename you will write to. Default (filename_log.py)
    RETURNS:
        None
    EXAMPLE (default logging):
        log("This thing happened")
    EXAMPLE (logging to a different file)
        log("This thing happened", "new_logfile.txt")
    """
    with open(filename, "a") as f:
        f.write(f"\nTIMESTAMP:{NOW}__MSG:{msg}")


def send_remote_command(hostip, port, command):
    """
    SUMMARY:
        sends command to remote server
    ARGS:
        hostip (str): the ip address of the target.
        port (str): the ssh port for the target
        command (str): the command to be executed on target.
    RETURNS:
        output (str): the stdout for the command that was executed on the remote server.
    EXAMPLE:
        send_remote_command('10.0.0.1', 'ifconfig')
    """
    try:
        if not use_key:
            # create client
            print("sending remote command")
            client = paramiko.SSHClient()
            client.set_missing_host_key_policy(paramiko.AutoAddPolicy())

            # get username and password
            username = input(f"What is the username for {hostip}? ")
            password = getpass.getpass(f"What is the password for {hostip}?: ")

            # connect
            client.connect(hostip, port=port, username=username, password=password)
            log(f"connection opened to {hostip}")

            # run command
            (stdin, stdout, stderr) = client.exec_command(command)
            output = stdout.read()
            print(output.decode())
            print(f"ran {command}")

            # return
            return output
        
        elif not use_key:
            log("using ssh keys")

            # create client
            print("sending remote command")
            client = paramiko.SSHClient()
            client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
            # connect
            client.connect(hostip, port=port)
            log(f"connection opened to {hostip}")

            # run command
            (stdin, stdout, stderr) = client.exec_command(command)
            output = stdout.read()
            print(output.decode())
            log(f"ran {command}")

            # return
            return output

    except Exception as e:
        print(f'#### FAILURE: {e}')
        log(e)
    finally:
        print("Closing Connection")
        client.close()
        log(f"connection closed to {hostip}")

def copy_remote_file_to_local(ip_address, source, destination):
    username = input(f"What is the username for {ip_address}? ")
    password = getpass.getpass(f"What is the password for {ip_address}?: ")
    command = f'scp {username}:{password}@{ip_address}:{source} {destination}'

    # create client
    print("sending remote command")
    client = paramiko.SSHClient()
    client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    # connect
    client.connect(hostip, port=port)
    log(f"connection opened to {hostip}")

    # run command
    (stdin, stdout, stderr) = client.exec_command(command)
    output = stdout.read()
    print(output.decode())
    log(f"ran {command}")

    # return
    return output

def copy_local_file_to_remote(ip_address, source, destination):
    pass

def copy_key_to_server():
    pass


if __name__ == '__main__':

    # prebuilt commands
    if command == 'check_docker':
        command = 'systemctl status docker'
    elif command == 'restart_docker':
        command = 'systemctl restart docker'
    elif command == 'check_ip':
        command = "ifconfig|grep 'inet'"
    elif command == 'disk_space':
        command = 'df -h'
    elif command == 'check_mounts':
        command = 'lsblk'

    send_remote_command(hostip, port, command)
