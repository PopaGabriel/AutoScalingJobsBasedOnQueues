build server1_image
port forward 5000:5000
port forward 5001:5001
locustfile
locust host -> http://127.0.0.1:5000