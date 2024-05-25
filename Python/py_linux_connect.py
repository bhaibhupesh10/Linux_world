import paramiko

def ssh_connect(hostname, port, username, password):
    """Establish an SSH connection to the server."""
    try:
        # Create an SSH client
        ssh_client = paramiko.SSHClient()
        
        # Automatically add the server's host key (not recommended for production)
        ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        
        # Connect to the server
        ssh_client.connect(hostname, port, username, password)
        return ssh_client
    except Exception as e:
        print(f"Failed to connect to {hostname}:{port}. Error: {e}")
        return None

def execute_command(ssh_client, command):
    """Execute a command on the remote server via SSH."""
    try:
        stdin, stdout, stderr = ssh_client.exec_command(command)
        output = stdout.read().decode()
        error = stderr.read().decode()
        
        if output:
            print(f"Output:\n{output}")
        if error:
            print(f"Error:\n{error}")
    except Exception as e:
        print(f"Failed to execute command. Error: {e}")

def main():
    # SSH connection details
    hostname = input("Enter the hostname or IP address: ")
    port = int(input("Enter the port (default is 22): ") or 22)
    username = input("Enter the username: ")
    password = input("Enter the password: ")

    # Establish SSH connection
    ssh_client = ssh_connect(hostname, port, username, password)
    if ssh_client:
        while True:
            command = input("Enter the command to execute (or 'exit' to quit): ")
            if command.lower() == 'exit':
                break
            execute_command(ssh_client, command)
        
        # Close the SSH connection
        ssh_client.close()

if __name__ == "__main__":
    main()
