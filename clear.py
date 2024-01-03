import os
import platform

# Get the operating system
current_os = platform.system()

# Check the operating system and clear the screen accordingly
if current_os == "Windows":
    os.system("cls")
elif current_os in ["Linux", "Darwin"]:  # "Darwin" corresponds to macOS
    os.system("clear")
else:
    print(f"Unsupported operating system: {current_os}")
