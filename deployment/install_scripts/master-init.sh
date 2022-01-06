#!/bin/bash
sudo route delete default gw 10.0.1.200 eth0
sudo route add default gw 10.64.92.1 eth1
kubeadm init --pod-network-cidr=10.244.0.0/16 --control-plane-endpoint=master && mkdir -p $HOME/.kube && sudo cp -i /etc/kubernetes/admin.conf $HOME/.kube/config && sudo chown $(id -u):$(id -g) $HOME/.kube/config && sudo kubectl apply -f https://raw.githubusercontent.com/coreos/flannel/master/Documentation/kube-flannel.yml && sleep 10 && kubectl delete --all po -n kube-system
sleep 5 && kubectl get po -A
kubeadm token create --print-join-command
