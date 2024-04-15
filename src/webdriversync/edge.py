import os
import requests

def download_edgedriver(edge_version, platform, output_dir="."):
    """Download EdgeDriver based on the provided version and platform.

    Args:
        edge_version (str): The version of Edge.
        platform (str): The platform for which EdgeDriver is needed. It can be one of the following:
            - "linux64": for 64-bit Linux
            - "mac-arm64": for Apple Silicon Mac (arm64 architecture)
            - "mac-x64": for 64-bit Intel Mac
            - "win32": for 32-bit Windows
            - "win64": for 64-bit Windows
        output_dir (str, optional): The directory where the EdgeDriver should be saved. Defaults to the current directory.

    Returns:
        str: The path to the downloaded EdgeDriver.

    Raises:
        ValueError: If an unsupported platform is provided.
        Exception: If the download fails.
    """
    base_url = "https://msedgedriver.azureedge.net"
    

    platform_type = {
        "linux64": "linux64",
        "mac-arm64": "mac-arm64",
        "mac-x64": "mac-x64",
        "win32": "win32",
        "win64": "win64"
    }.get(platform)

    if platform_type is None:
        raise ValueError("Unsupported Platform")

    edgedriver_url = f"{base_url}/{edge_version}/edgedriver_{platform_type}.zip"

    # Construct the output path
    filename = os.path.basename(edgedriver_url)
    output_path = os.path.join(output_dir, filename)

    # Download the EdgeDriver
    try:
        response = requests.get(edgedriver_url)
        response.raise_for_status()
        with open(output_path, "wb") as f:
            f.write(response.content)
    except Exception as e:
        raise Exception(f"Failed to download EdgeDriver: {str(e)}")

    return output_path

download_edgedriver("123.0.2420.97", "win64", output_dir=".")
