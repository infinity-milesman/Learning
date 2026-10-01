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














---

---
# ---------- Redis (database tier) ----------

---

---
# ---------- API (shell-less image: traefik/whoami is built FROM scratch) ----------

---
# BUG #1: targetPort is 8081 but the app listens on 8080

---
# ---------- Frontend (also shell-less) ----------

---

---
# ---------- Locked-down service: NetworkPolicy blocks everything except frontend ----------
# (kind's default CNI does not enforce NetworkPolicy, so this is for reading/analysis practice)

---
# ---------- BUG #2: CrashLoopBackOff (bad flag, and no shell to investigate) ----------

