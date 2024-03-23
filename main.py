import os
import time
from spot_controller import SpotController
import cv2
import http.client
from supabase import create_client, Client

url: str = os.environ.get("SUPABASE_URL")
key: str = os.environ.get("SUPABASE_KEY")
supabase: Client = create_client(url, supabase_key=key)

ROBOT_IP = "10.0.0.3"#os.environ['ROBOT_IP']
SPOT_USERNAME = "admin"#os.environ['SPOT_USERNAME']
SPOT_PASSWORD = "2zqa8dgw7lor"#os.environ['SPOT_PASSWORD']

def fetch(path = "/", method='GET'):
    # Url
    url='http://192.168.2.189:8000'
    
    # Define the URL and headers
    headers = {}

    # Create an HTTP connection
    conn = http.client.HTTPConnection(url.split("/")[2])

    # Send a GET request
    conn.request("GET", path, headers=headers)

    # Get the response
    response = conn.getresponse()

    # Print the response status and data
    print("Status:", response.status, response.reason)
    data = response.read()
    print("Data:", data.decode())

    # Close the connection
    conn.close()

def capture_image():
    camera_capture = cv2.VideoCapture(0)
    rv, image = camera_capture.read()
    camera_capture.release()
    path = f'/merklebot/job_data/camera_{time.time()}.jpg'
    cv2.imwrite(path, image)

    with open(path, 'rb') as f:
        res = supabase.storage.from_("spot").upload(file=f,path=path, file_options={"content-type": "image/jpeg"})
    
    return res


def main():
    with SpotController(username=SPOT_USERNAME, password=SPOT_PASSWORD, robot_ip=ROBOT_IP) as spot:
        res = capture_image()
        print(res)


if __name__ == '__main__':
    main()
