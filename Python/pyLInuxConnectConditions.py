import subprocess
import paramiko

def execute_local(command):
    """
    Execute a command locally and return the output.
    """
    result = subprocess.run(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
    if result.returncode == 0:
        return result.stdout
    else:
        return result.stderr

def execute_ssh(command, ssh_client):
    """
    Execute a command on the SSH client and return the output.
    """
    stdin, stdout, stderr = ssh_client.exec_command(command)
    output = stdout.read().decode('utf-8')
    error = stderr.read().decode('utf-8')
    return output if not error else error

def main():
    while True:
        # Prompt user for execution method
        execution_method = input("Where do you want to run the commands? (local/ssh, or 'exit' to quit): ").lower()

        if execution_method == "exit":
            break

        if execution_method == "local":
            while True:
                command = input("Enter the command to execute (or 'back' to choose again, 'exit' to quit): ")
                if command.lower() == "exit":
                    return
                elif command.lower() == "back":
                    break
                output = execute_local(command)
                print("Result (local):")
                print(output)
        elif execution_method == "ssh":
            # SSH connection parameters
            hostname = input("Enter the SSH hostname: ")
            port = 22  # Default SSH port
            username = input("Enter the SSH username: ")
            password = input("Enter the SSH password: ")

            # Create SSH client instance
            ssh_client = paramiko.SSHClient()
            ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())

            try:
                # Connect to the SSH server
                ssh_client.connect(hostname, port, username, password)
                while True:
                    command = input("Enter the command to execute (or 'back' to choose again, 'exit' to quit): ")
                    if command.lower() == "exit":
                        ssh_client.close()
                        return
                    elif command.lower() == "back":
                        break
                    output = execute_ssh(command, ssh_client)
                    print("Result (SSH):")
                    print(output)
            except paramiko.AuthenticationException:
                print("Authentication failed. Please check your credentials.")
            except paramiko.SSHException as ssh_exc:
                print(f"SSH error: {ssh_exc}")
            finally:
                if ssh_client.get_transport() is not None and ssh_client.get_transport().is_active():
                    ssh_client.close()
        else:
            print("Invalid execution method. Please choose 'local' or 'ssh'.")

if __name__ == "__main__":
    main()
