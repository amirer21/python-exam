import requests

# Set the server's address (replace with the appropriate address)
server_url = 'http://localhost:8080/getDeviceInfo'

try:
    print('try!')
    response = requests.get(server_url)
    if response.status_code == 200:
        device_info = response.json()
        print("Received Device Info:")
        print("Screen Width:", device_info['screen_width'])
        print("Screen Height:", device_info['screen_height'])
        print("Platform:", device_info['platform'])
        print("Platform Version:", device_info['platform_version'])
        print("Product Model:", device_info['product_model'])
        print("Build Target Country:", device_info['build_target_country'])
        print("Build Version Release:", device_info['build_version_release'])
        print("Hardware Revision:", device_info['hw_revision'])
        print("Revision:", device_info['revision'])
        print("OS Version:", device_info['os_version'])
    else:
        print(f"Failed to retrieve Device Info. Status code: {response.status_code}")
except requests.exceptions.RequestException as e:
    print(f"Error: {e}")
