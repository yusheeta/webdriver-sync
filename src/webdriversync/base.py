import platform
import sys
import json

class WebdriverSyncBase:
    @staticmethod
    def get_os_name():
        """Determine the name of the operating system.

        Returns:
            str: A string indicating the name of the operating system. Possible values are 'win' for Windows,
                'mac' for macOS, and 'linux' for Linux.
        """
        platform_name = platform.system()
        platform_list = {"Daarwin": "mac", "Windows": "win", "Linux": "linux"}
        if "CYGWIN" in platform_name:
            return "win"
        return platform_list[platform_name]
    
    @staticmethod
    def get_cpu_bitness():
        """Determine the bitness of the CPU architecture.

        Returns:
            str: A string indicating the CPU bitness. Possible values are '32' for a 32-bit CPU architecture
                and '64' for a 64-bit CPU architecture.
        """
        if sys.maxsize > 2**32:
            return 64
        else:
            return 32

    @staticmethod
    def get_platform_type(os_name, cpu_bitness):
        """Determine the platform type based on the operating system name and CPU bitness.

        Args:
            os_name (str): The name of the operating system. Possible values are 'win' for Windows,
                        'mac' for macOS, and 'linux' for Linux.
            cpu_bitness (str): A string indicating the CPU bitness. Possible values are '32' for a
                            32-bit CPU architecture and '64' for a 64-bit CPU architecture.
        """
        platform_type = os_name + str(cpu_bitness)
        return platform_type