curl -LO https://github.com/kubernetes/minikube/releases/latest/download/minikube-linux-amd64

create deployment-declarative...
k create deployment kubernetes-bootcamp --image=gcr.io/google-samples/kubernetes-bootcamp:v1

Expose your deployment - 
k expose deployment/kubernetes-bootcamp --type="NodePort" --port 8080

To scale up and down replicasets - 
kubectl scale deployments/kubernetes-bootcamp --replicas=2


To clean up your local cluster - 
k delete deployments/kubernetes-bootcamp service/kubernetes-bootcamp

Reference-
https://minikube.sigs.k8s.io/docs/start/?arch=%2Flinux%2Fx86-64%2Fstable%2Fbinary+download#Ingress