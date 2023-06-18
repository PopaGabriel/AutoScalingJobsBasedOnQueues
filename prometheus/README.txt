Pentru a ridica serviciul de prometheus trebuie date urmatpoarele comenzi

helm repo add prometheus-community https://prometheus-community.github.io/helm-charts
helm repo update
helm install prometheus prometheus-community/prometheus
