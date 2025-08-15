import requests
import sys
import os

def health_check():
    try:
        # Obtener la URL del servicio
        url = os.environ.get('RENDER_EXTERNAL_URL', 'http://localhost:5000')
        response = requests.get(f"{url}/", timeout=10)
        if response.status_code == 200:
            print("Health check passed")
            return True
        else:
            print(f"Health check failed: Status {response.status_code}")
            return False
    except Exception as e:
        print(f"Health check failed: {e}")
        return False

if __name__ == "__main__":
    if health_check():
        sys.exit(0)
    else:
        sys.exit(1)
