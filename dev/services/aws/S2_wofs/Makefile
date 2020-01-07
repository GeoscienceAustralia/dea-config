# Do stuff with the queue
add-to-queue:
	kubectl create -f wofs-addqueue.yaml

kill-queue:
	kubectl delete -f wofs-addqueue.yaml

redo-queue:
	make kill-queue
	make add-to-queue

deploy-workers:
	kubectl create -f wofs-processqueue.yaml

update-workers:
	kubectl replace -f wofs-processqueue.yaml

undeploy-workers:
	kubectl delete -f wofs-processqueue.yaml


get-cmd:
	kubectl exec -it -n alchemist-processor k8s-dev-6688874fbb-b68gc bash
