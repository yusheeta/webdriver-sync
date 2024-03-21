import platform


# Function to detect 
def get_os_name():
        platform_name = platform.system()
        platform_list = {"Daarwin": "mac", "Windows": "win", "Linux": "linux"}
        if "CYGWIN" in platform_name:
            return "win"

        return platform_list[platform_name]

