# Do stuff with the queue
add-to-queue:
	kubectl create -f fc-addqueue-alextest.yaml

kill-queue:
	kubectl delete -f fc-addqueue-alextest.yaml

redo-queue:
	make kill-queue
	make add-to-queue

deploy-workers:
	kubectl create -f fc-processqueue-alextest.yaml

update-workers:
	kubectl replace -f fc-processqueue-alextest.yaml

undeploy-workers:
	kubectl delete -f fc-processqueue-alextest.yaml

deploy-autoscaler:
	kubectl create -f fc-processqueue-autoscaler-alextest.yaml

update-autoscaler:
	kubectl replace -f fc-processqueue-autoscaler-alextest.yaml

undeploy-autoscaler:
	kubectl delete -f fc-processqueue-autoscaler-alextest.yaml

get-cmd:
	kubectl exec -it -n alchemist-processor k8s-dev-6688874fbb-b68gc bash
