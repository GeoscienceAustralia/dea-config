# Do stuff with the queue
add-to-queue:
	kubectl create -f fc-addqueue.yaml

kill-queue:
	kubectl delete -f fc-addqueue.yaml

redo-queue:
	make kill-queue
	make add-to-queue

logs:
	kubectl logs -f fc-addqueue   --namespace=alchemist-processor

getpods:
	kubectl get pods   --namespace=alchemist-processor


deploy-workers:
	kubectl create -f sandbox-deployment-processqueue-alchemist.yaml

update-workers:
	kubectl replace -f sandbox-deployment-processqueue-alchemist.yaml

undeploy-workers:
	kubectl delete -f sandbox-deployment-processqueue-alchemist.yaml

# deploy-autoscaler:
# 	kubectl create -f fc-processqueue-autoscaler-alextest.yaml

# update-autoscaler:
# 	kubectl replace -f fc-processqueue-autoscaler-alextest.yaml

# undeploy-autoscaler:
# 	kubectl delete -f fc-processqueue-autoscaler-alextest.yaml

get-cmd:
	kubectl exec -it -n alchemist-processor k8s-dev-6688874fbb-qs9bb bash
