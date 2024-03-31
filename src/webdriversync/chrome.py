class ChromeDriverManager:

  def construct_chromedriver_url(chrome_version, platform):
    """Construct the URL to download Chromedriver based on the provided Chrome version and platform.

      Args:
          chrome_version (str): The version of Chrome.
          platform (str): The platform for which Chromedriver is needed. It can be one of the following:
              - "linux64": for 64-bit Linux
              - "mac-arm64": for Apple Silicon Mac (arm64 architecture)
              - "mac-x64": for 64-bit Intel Mac
              - "win32": for 32-bit Windows
              - "win64": for 64-bit Windows

      Returns:
          str: The URL to download the corresponding Chromedriver ZIP file.

      Raises:
          ValueError: If an unsupported platform is provided.
    """
    base_url = "https://storage.googleapis.com/chrome-for-testing-public"

    platform_type = {
          "linux64": "linux64",
          "mac-arm64": "mac-arm64",
          "mac-x64": "mac-x64",
          "win32": "win32",
          "win64": "win64"
      }.get(platform)

    if platform_type is None:
      raise ValueError("Unsupported Platform")

    return f"{base_url}/{chrome_version}/{platform_type}/chromedriver-{platform_type}.zip"
