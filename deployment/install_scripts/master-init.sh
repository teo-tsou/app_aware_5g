#!/bin/bash
kubeadm init --pod-network-cidr=10.244.0.0/16 --control-plane-endpoint=master && mkdir -p $HOME/.kube && sudo cp -i /etc/kubernetes/admin.conf $HOME/.kube/config && sudo chown $(id -u):$(id -g) $HOME/.kube/config && sudo kubectl apply -f https://raw.githubusercontent.com/coreos/flannel/master/Documentation/kube-flannel.yml && sleep 10 && kubectl delete --all po -n kube-system
sleep 5 && kubectl get po -A
kubeadm token create --print-join-command
