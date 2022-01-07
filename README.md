# app_aware

### Cluster Installation:

1) Install Docker for Each Server Node:

```
    root@host:~# sudo apt-get install docker.io
    root@host:~# sudo systemctl enable docker
    root@host:~# sudo systemctl start docker
```

2) Install Kubernetes (v1.21.0) for Each Server Node:

```
    root@host:~# curl -s https://packages.cloud.google.com/apt/doc/apt-key.gpg | sudo apt-key add
    root@host:~# sudo apt-add-repository "deb http://apt.kubernetes.io/ kubernetes-xenial main"
    root@host:~# sudo apt install kubeadm=1.21.0-00 kubectl=1.21.0-00 kubelet=1.21.0-00
    root@host:~# sudo apt-mark hold kubeadm kubelet kubectl
    root@host:~# sudo swapoff –a
```

3) Assign Unique Hostname for Each Server Node (**use the same hostnames**)

    For Master Node:
       `sudo hostnamectl set-hostname master`

    For Worker:
       `sudo hostnamectl set-hostname cloud-worker`

    Specifically for the USRP worker:
       `sudo hostnamectl set-hostname antenna-worker`

    Add Host File Info
    Now we will log in to **each machine** and edit the /etc/hosts configuration file using this command.

    ```
    root@host:~# tee -a /etc/hosts< 192.168.50.58 master
    > 192.168.50.38 cloud-worker
    > 192.168.50.178 antenna-worker
    > EOF
    ```

    note: The IPs are random.

 4) Init Cluster through scripts:

    ```
    root@master:~# cd app_aware/deployment/install_scripts
    root@master:~/app_aware/deployment/install_scripts bash master_init.sh
                            
    kubeadm join master:6443 --token 1iv0jy.04ngrum11g1jvrya --discovery-token-ca-cert-hash sha256:3651eeb28835fc1b94d8f626be8467024f80ed77cef5c89d4c78940f7d79bf8d 

    ```

5) Join Worker Nodes to Cluster:

    `root@cloud-worker:~#  kubeadm join master:6443 --token 1iv0jy.04ngrum11g1jvrya --discovery-token-ca-cert-hash sha256:3651eeb28835fc1b94d8f626be8467024f80ed77cef5c89d4c78940f7d79bf8d `

    `root@antenna-worker:~#  kubeadm join master:6443 --token 1iv0jy.04ngrum11g1jvrya --discovery-token-ca-cert-hash sha256:3651eeb28835fc1b94d8f626be8467024f80ed77cef5c89d4c78940f7d79bf8d `

6) Install NFS to Cluster through scripts:

    On the Master Node:

    ```
    root@master:~# cd app_aware/deployment/install_scripts
    root@master:~/app_aware/deployment/install_scripts bash master-nfs.sh

    ```
    On the Worker Nodes:

    ```
    root@cloud-worker:~# cd app_aware/deployment/install_scripts
    root@cloud-worker:~/app_aware/deployment/install_scripts bash workers-nfs.sh

    ```

    ```
    root@antenna-worker:~# cd app_aware/deployment/install_scripts
    root@antenna-worker:~/app_aware/deployment/install_scripts bash workers-nfs.sh
    ```

    Let’s ensure we can read/write to the shared directory. On one worker, touch a file:

    `touch /mnt/nfs_client_files/ok.txt`

    On another worker, look for the file:

    `ls /mnt/nfs_client_files/ | grep ok.txt`

    If the file exists, you’re good to go.

7) Deploy Storages (Local-Host Provisioner , NFS Provisioner) & Multus CNI:

    On the Master Node:

    `root@master:~/app_aware/deployment/install_scripts bash deploy-storages.sh`

8) Install Kubeflow:
    
    On the Master Node:
```
    root@master:~# cd app_aware/deployment/kubeflow/install
    root@master:~/app_aware/deployment/kubeflow/install tar -xzvf kfctl_v1.0.2-0-ga476281_linux.tar.gz
    root@master:~/app_aware/deployment/kubeflow/install ./kfctl apply -f kfctl_k8s_istio.v1.0.2.yaml
```
After the installation, wait until all pods are running.


### Deploy AI Containerized 5G Network & Applications:

 On the Master Node:
```
    root@master:~# cd app_aware/deployment/
    root@master:~/app_aware/deployment/ bash deploy-all.sh

```
Wait until all pods are running.


### UE Applications Install & Network Connectivity:

1) Install Applications for Each UE:

For SIPp:

```
root@ue:~# cd app_aware/deployment/ue/sipp_installer sudo chmod +x sipp_installer.sh
root@ue:~/app_aware/deployment/ue/sipp_installer  sudo ./sipp_installer.sh
```

For Chromium: 
    `root@ue:~# sudo apt install chromium-browser`


2) Connect to the Network

For each UE:

   `root@ue:~# minicom -D /dev/ttyUSB1`

(For easy copy paste run on serial console: ^az -> t -> f -> change from 0 to 1 -> enter -> enter)

Enter the following:
```
at+cgdcont=0,"IP","apn.oai.svc.cluster.local"
at+cgdcont=1,"IP","apn.oai.svc.cluster.local"
```

Turn off the antenna until the 5G network is up:
`at+cfun=0`

When the CU/DU pods are running then:
`at+cfun=1`

Then enter:
`at^ndisdup=1,1`

Finally, enter:
`at^dhcp?`

If it returns IP in hex form, then exit minicom and:

```
 root@ue:~# dhclient wwan0
 root@ue:~# ifconfig wwan0 netmask 255.255.255.0 -arp
 root@ue:~# route add -net 192.168.3.0/24 gw 192.168.20.1
```

### Create Traffic:

On the UEs:

```
root@ue:~# cd app_aware/scenarios/scenario3/
root@ue:~/app_aware/scenarios/scenario3/ bash ue1.sh
```

(for UE2: bash ue2.sh , for UE3: bash ue3.sh)

### On-Demand Resource Provisioning:

Watch the logs on the Master Node:
    For App-Aware Predictor:
   `root@master:~# kubectl logs -f oai-spgwu-86bfc8f9f7-2zrf2 -c predictor -n oai`
    
    For FlexRAN:
   `root@master:~# kubectl logs -f flexran-588f7bc566-8kmjd -c predictor -n oai`
                    

### Employ Kubeflow Pipeline:

On the Master Node:

Create a database and a table inside MySQL Container: 

```
root@master:~# kubectl exec -ti mysql-63082529-2z3ki bash
mysql-63082529-2z3ki@root:~#  mysql -h mysql -ppassword
mysql> CREATE DATABASE oai;
mysql> CREATE TABLE oai.app_data(
Packet_Num varchar(6),
Time_packet varchar(6),
Source varchar(15),
Destination varchar(15),
Protocol varchar(12),
Length_packet varchar(6)
```


Deploy the 5G Network and the Applications:

`root@master:~/app_aware/deployment/ bash deploy-all.sh`




Deploy the pipeline volume:

`root@master:~# cd app_aware/deployment/kubeflow/pipeline-files`
`root@master:~/app_aware/deployment/kubeflow/pipeline-files kubectl create -f kubeflow-nfs-volume.yml`

Compile the pipeline script which will generate a yaml manifest (called app-aware-pipeline.yaml) the one will be uploaded to 
Kubeflow Pipelines service in order to run the pipeline:

`root@master:~/app_aware/deployment/kubeflow/pipeline-files python3 pipeline.py`
