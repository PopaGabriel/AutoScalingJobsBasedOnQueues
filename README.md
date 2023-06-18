# Get images
docker pull python:3.11.2-slim-buster
docker pull rabbitmq:alpine

# Secret creation
kubectl apply -f secret.yaml

# RabbitMQ
build rabbitmq-inhouse:latest
build server1_image:latest

# Deployments
kubectl apply -f rabbitmq-server/k8s/deployment...
kubectl apply -f server2/k8s/...

# Prometheus
helm repo add prometheus-community https://prometheus-community.github.io/helm-charts
helm repo update
helm install prometheus-stack prometheus-community/kube-prometheus-stack
helm install prometheus prometheus-community/prometheus

# Grafana
helm repo add grafana https://grafana.github.io/helm-charts
helm repo update
kubectl get secret — namespace default grafana -o yaml
echo “password_value” | openssl base64 -d ; echo
echo “username_value” | openssl base64 -d ; echo
Conect to grafana and add datasource, cluster-IP of service with good port for prometheus server

# Service monitor for prometheus

# Scalers
kubectl apply -f https://github.com/kedacore/keda/releases/download/v2.10.1/keda-2.10.1.yaml
kubectl apply -f server1_keda_deployment



port forward 5000:5000
port forward 5001:5001


locustfile
locust host -> http://127.0.0.1:5000

https://medium.com/globant/setup-prometheus-and-grafana-monitoring-on-kubernetes-cluster-using-helm-3484efd85891
GXPudY7B3cPX3VjAzCowl2YsIK5h6zlFq3WrXatu
admin