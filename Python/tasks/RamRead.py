def get_total_ram():
    mem = psutil.virtual_memory()
    total_ram_gb = mem.total / (1024 ** 3)  # Convert bytes to gigabytes
    return total_ram_gb

if __name__ == "__main__":
    total_ram = get_total_ram()
    print("Total RAM:", total_ram, "GB")