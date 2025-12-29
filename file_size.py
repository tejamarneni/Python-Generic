import os

file_path = 'huge_data.csv'  # Replace with your file name

# 1. Get size in Bytes
size_bytes = os.path.getsize(file_path)

# 2. Convert to Gigabytes (GB)
size_gb = size_bytes / (1024 * 1024 * 1024)

# 3. Apply the "Rule of 10" (Conservative estimate)
estimated_ram_needed = size_gb * 10

print(f"File Size on Disk: {size_gb:.2f} GB")
print(f"Estimated RAM to load safely: {estimated_ram_needed:.2f} GB")

# 4. Simple Decision Logic
# Change this number to match your computer's actual RAM (e.g., 16, 32, 64)
my_computer_ram = 16 

if estimated_ram_needed > (my_computer_ram * 0.7): # Leave 30% buffer for OS
    print("⚠️ DANGER: This file is too big! Use chunksize.")
else:
    print("✅ SAFE: You can probably load this normally.")
