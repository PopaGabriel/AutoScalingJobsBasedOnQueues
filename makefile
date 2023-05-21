restart_base_setup:
	colima stop && \
	colima delete -y && \
	colima start --cpu 4 --memory 4 --disk 100 && \
	minikube stop && \
	minikube delete -y && \
	minikube start --memory 8192 --cpus 2 && \
	eval $(minikube -p minikube docker-env)

reinstall_krew:
	(
	set -x; cd "$(mktemp -d)" &&
	OS="$(uname | tr '[:upper:]' '[:lower:]')" &&
	ARCH="$(uname -m | sed -e 's/x86_64/amd64/' -e 's/\(arm\)\(64\)\?.*/\1\2/' -e 's/aarch64$/arm64/')" &&
	KREW="krew-${OS}_${ARCH}" &&
	curl -fsSLO "https://github.com/kubernetes-sigs/krew/releases/latest/download/${KREW}.tar.gz" &&
	tar zxvf "${KREW}.tar.gz" &&
	./"${KREW}" install krew
	) && \
	source ~/.zshrc

reinstall_rabbitmq:
	kubectl apply -f "https://github.com/rabbitmq/cluster-operator/releases/latest/download/cluster-operator.yml" && \
	kubectl krew install rabbitmq && \
	kubectl rabbitmq create rabbitmqserver && \
	kubectl rabbitmq get rabbitmq-server

install_krew:
	(
	set -x; cd "$(mktemp -d)" &&
	OS="$(uname | tr '[:upper:]' '[:lower:]')" &&
	ARCH="$(uname -m | sed -e 's/x86_64/amd64/' -e 's/\(arm\)\(64\)\?.*/\1\2/' -e 's/aarch64$/arm64/')" &&
	KREW="krew-${OS}_${ARCH}" &&
	curl -fsSLO "https://github.com/kubernetes-sigs/krew/releases/latest/download/${KREW}.tar.gz" &&
	tar zxvf "${KREW}.tar.gz" &&
	./"${KREW}" install krew
	) && \
	echo 'export PATH="${PATH}:${HOME}/.krew/bin"' >> ~/.zshrc && \
	source ~/.zshrc
