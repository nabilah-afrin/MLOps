import requests

# test ping endpoint

# response = requests.get("https://68df7367c04ecee45380f1b8_63c33943.lb.poridhi.io/ping")
response = requests.get("http://127.0.0.1:8000/ping")
print(f"Status: {response.status_code}")
print(f"Response: {response.json()}")

# Test hello endpoint
response = requests.get("http://127.0.0.1:8000/hello/Ada?greeting=Hi")
print("Status:", response.status_code)
print("Response:", response.json())