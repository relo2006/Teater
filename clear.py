import os
import platform

current_os = platform.system()

if current_os == "Windows":
    os.system("cls")
elif current_os in ["Linux", "Darwin"]:
    os.system("clear")
else:
    print(f"Unsupported operating system: {current_os}")
