import paramiko

def execute_command(ssh_client, command):
    """
    Execute a command on the SSH client and return the output.
    """
    stdin, stdout, stderr = ssh_client.exec_command(command)
    output = stdout.read().decode('utf-8')
    error = stderr.read().decode('utf-8')
    return output if not error else error

def main():
    # SSH connection parameters
    hostname = '192.168.56.102'
    port = 22  # Default SSH port
    username = 'root'
    password = '7750'

    # Create SSH client instance
    ssh_client = paramiko.SSHClient()
    ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())

    try:
        # Connect to the SSH server
        ssh_client.connect(hostname, port, username, password)

        # Execute commands
        commands = [
            'ls -l',
            'uname -a',
            'whoami',
            # Add more commands as needed
        ]

        for command in commands:
            print(f"Executing command: {command}")
            result = execute_command(ssh_client, command)
            print("Result:")
            print(result)

    except paramiko.AuthenticationException:
        print("Authentication failed. Please check your credentials.")
    except paramiko.SSHException as ssh_exc:
        print(f"SSH error: {ssh_exc}")
    finally:
        # Close the SSH connection
        ssh_client.close()

if __name__ == "__main__":
    main()
