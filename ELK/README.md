kubectl apply -f https://raw.githubusercontent.com/rancher/local-path-provisioner/master/deploy/local-path-storage.yaml

helm repo add elastic https://helm.elastic.co
helm install elasticsearch elastic/elasticsearch
