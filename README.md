# AI-driven Application-Aware 5G Network on Kubernetes:

A cloud-native 5G Network based on OAI platform, fully deployed on Kubernetes, enhanced with AI Unit to forecast the interactions between end-users and applications, and to improve the Quality of Experience of the users in real-time by utilizing the FlexRAN Controller.

If you find this project useful in your research, please consider citing:

 ```
  @INPROCEEDINGS{cnert,
AUTHOR="Theodoros Tsourdinis and Ilias Chatzistefanidis and Nikos Makris and
Thanasis Korakis",
TITLE="{AI-driven} Service-aware Real-time Slicing for beyond {5G} Networks",
BOOKTITLE="IEEE INFOCOM WKSHPS: Computer and Networking Experimental Research using
Testbeds (CNERT 2022) (INFOCOM WKSHPS CNERT 2022)",
MONTH=may,
YEAR=2022,
}
```

![alt text]([https://github.com/[username]/[reponame]/blob/[branch]/image.jpg?raw=true](https://github.com/teo-tsou/app_aware_5g/blob/master/deployment/experimental%20(2).png)

**DEMO:**


[![DEMO](https://img.youtube.com/vi/2scoAJRxJrY/0.jpg)](https://www.youtube.com/watch?v=2scoAJRxJrY)


## Installation Guide:

### A) Install on Nitos Testbed (Highly Recommended)

1) Create a User Account, Get a Slice & Reserve Nodes on the Testbed

Check the documentation:
http://nitlab.inf.uth.gr/doc/accessing_nitos.html
   

2) Load the images on the nodes:

Tested on Nodes: node055, node084, node085, node054, node065, node057

node055: USRP B210 Node - Use it as a Kubernetes worker
node084: Simple Node - Use it as a Kubernetes worker
node086: Simple Node- Use it as Kubernetes Master Node

node054, node065 & node057: HUAWEI LTE Dongles Nodes - Use them as UEs 

For the Kubernetes Cluster (use the specific nodes):
```
root@host:~# ssh -X slicename@nitlab3.inf.uth.gr
slicename@nitlab3:~$ omf load -i app-aware-node.ndz -t node055,node084,node085
```

For the UEs (use the specific nodes):

`slicename@nitlab3:~$ omf load -i app-aware-ue.ndz -t node054,node065,node057`

After the load completes, access the nodes through ssh:
e.g.: 

`slicename@nitlab3:~$ ssh -X root@node086`


#### Cluster Installation:

1) Assign Unique Hostname for Each Server Node (**use the same hostnames**)

    For Master Node:
    
    `root@node086:~# sudo hostnamectl set-hostname master`

    For Worker:
    
    `root@node085:~# sudo hostnamectl set-hostname cloud-worker`

    Specifically for the USRP worker:
    
    `root@node055:~# sudo hostnamectl set-hostname antenna-worker`

    Add Host File Info
    Now we will log in to **each machine** and edit the /etc/hosts configuration file using this command.

    ```
    root@host:~# tee -a /etc/hosts< 192.168.50.58 master
    > 192.168.50.38 cloud-worker
    > 192.168.50.178 antenna-worker
    > EOF
    ```

    note: The IPs are random.

 2) Init Cluster through scripts:

    ```
    root@master:~# bash master-init.sh

    kubeadm join master:6443 --token 1iv0jy.04ngrum11g1jvrya --discovery-token-ca-cert-hash sha256:3651eeb28835fc1b94d8f626be8467024f80ed77cef5c89d4c78940f7d79bf8d 

    ```

3) Join Worker Nodes to Cluster:

    `root@cloud-worker:~#  kubeadm join master:6443 --token 1iv0jy.04ngrum11g1jvrya --discovery-token-ca-cert-hash sha256:3651eeb28835fc1b94d8f626be8467024f80ed77cef5c89d4c78940f7d79bf8d `

    `root@antenna-worker:~#  kubeadm join master:6443 --token 1iv0jy.04ngrum11g1jvrya --discovery-token-ca-cert-hash sha256:3651eeb28835fc1b94d8f626be8467024f80ed77cef5c89d4c78940f7d79bf8d `

4) Install NFS to Cluster through scripts:

    On the Master Node:

    ```
    root@master:~#  bash master-nfs.sh

    ```
    On the Worker Nodes:

    ```
    root@cloud-worker:~# bash workers-nfs.sh

    ```

    ```
    root@antenna-worker:~# bash workers-nfs.sh

    ```

    Let’s ensure we can read/write to the shared directory. On one worker, touch a file:

    `touch /mnt/nfs_client_files/ok.txt`

    On another worker, look for the file:

    `ls /mnt/nfs_client_files/ | grep ok.txt`

    If the file exists, you’re good to go.

5) Deploy Storages (Local-Host Provisioner, NFS Provisioner) & Multus CNI:

    On the Master Node:

    `root@master:~# bash deploy-storages.sh`




#### Deploy AI Containerized 5G Network & Applications:

On the antenna-worker Node:

`root@antenna-worker:~# bash usrp_on.sh`

 On the Master Node:
```
    root@master:~# cd app_aware/deployment/
    root@master:~/app_aware/deployment/ bash deploy-all

```
Wait until all pods are running.

#### UE Connectivity:

1) Turn USB Dongles on **for each of UE**:

e.g
`root@node076:~# lte_dongle -o`

2) Connect to the Network

For each UE:

   `root@node054:~# minicom -D /dev/ttyUSB1` 

   `root@node065:~# minicom -D /dev/ttyUSB0` 

   `root@node057:~# minicom -D /dev/ttyUSB1` 


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
 root@ue:~# bash attach-ip.sh
```

Then do the same for the next UE.


#### Create Traffic:

On the UEs:

```
root@ue:~# cd app_aware/scenarios/scenario3/
root@ue:~/app_aware/scenarios/scenario3/ bash ue1.sh
```

(for UE2: bash ue2.sh , for UE3: bash ue3.sh)

#### On-Demand Resource Provisioning:

Watch the logs on the Master Node:
   For App-Aware Predictor:
    
   `root@master:~# kubectl logs -f oai-spgwu-86bfc8f9f7-2zrf2 -c predictor -n oai`
    
   For FlexRAN:
    
   `root@master:~# kubectl logs -f flexran-588f7bc566-8kmjd -c predictor -n oai`



#### Employ Kubeflow Pipeline:


1) First, destroy the 5G Deployment and the apps:

`root@master:~/app_aware/deployment/ bash destroy-all.sh`

On the Master Node:

2) Create a database and a table inside MySQL Container: 

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

3) Install Kubeflow:
    
    On the Master Node:
```
    root@master:~# cd app_aware/deployment/kubeflow/install
    root@master:~/app_aware/deployment/kubeflow/install tar -xzvf kfctl_v1.0.2-0-ga476281_linux.tar.gz
    root@master:~/app_aware/deployment/kubeflow/install ./kfctl apply -V -f kfctl_k8s_istio.v1.0.2.yaml
```
After the installation, wait until all pods are running.


Deploy the 5G Network and the Applications:

`root@master:~/app_aware/deployment/ bash deploy-all.sh`




4) Deploy the pipeline volume:

`root@master:~# cd app_aware/deployment/kubeflow/pipeline-files`
`root@master:~/app_aware/deployment/kubeflow/pipeline-files kubectl create -f kubeflow-nfs-volume.yml`

Compile the pipeline script which will generate a yaml manifest (called app-aware-pipeline.yaml) the one will be uploaded to 
Kubeflow Pipelines service in order to run the pipeline:

`root@master:~/app_aware/deployment/kubeflow/pipeline-files python3 pipeline.py`

Then upload the yaml file in master_ip:31380 kubeflow service






















### B) Install on a Different Testbed

#### Minimum Requirements:

- 6 Nodes (3 Nodes for the cluster and 3 Nodes for the UEs):  Ubuntu bionic 18.04.2 LTS amd64/ Kernel 4.7.2 Low Latency | Cores=4 Mem=8G Root-disk=40G
- 1 of the Cluster Nodes equipped with SDR USRP Device, preferably: ETTUS USRP B210 USB (anntena-worker)
- All the UE nodes equipped with LTE Dongles 
- SIM cards configuration :
1. mcc = 460 
2. mnc = 99 
3. Ki: 000102030405060708090A0B0C0D0E0F 
4. Opcode: (HSS) 00112233445566778899aabbccddeeff
5. plmnid: 46099





#### Cluster Installation:

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
    root@host:~# sudo swapoff -a
    root@host:~# sed -i '/ swap / s/^\(.*\)$/#\1/g' /etc/fstab
```

3) Assign Unique Hostname for Each Server Node (**use the same hostnames**)

    For Master Node:
       `root@host:~# sudo hostnamectl set-hostname master`

    For Worker:
       `root@host:~# sudo hostnamectl set-hostname cloud-worker`

    Specifically for the USRP worker:
       `root@host:~# sudo hostnamectl set-hostname antenna-worker`

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
    root@master:~/app_aware/deployment/install_scripts bash master-init.sh
                            
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


#### Deploy AI Containerized 5G Network & Applications:

1) **It is highly recommended** before the deployment, to download the images **on both of the Worker Nodes**:

```
REPOSITORY                     TAG   
ttsourdinis/oai-parser         latest
MySQL                          5.6   
ttsourdinis/oai-spgwc          latest
cassandra                      3.11  
ttsourdinis/flexran-agent     v2.2.1
ttsourdinis/oai-build         latest
ttsourdinis/webrtc            latest
ttsourdinis/oai-spgwu         latest
ttsourdinis/oai-hss           latest
ttsourdinis/oai-mme           latest
ttsourdinis/web-server        latest
ttsourdinis/sipp              latest

```


For example: 
`root@cloud-worker:~# docker pull ttsourdinis/oai-parser`

`root@antenna-worker:~# docker pull ttsourdinis/flexran-agent:v2.2.1`



2) Edit the cassandra.yaml file to add the subscriber 3 UEs:

On the config_map section, for example:

```
INTO vhss.users_imsi (imsi, msisdn, access_restriction, key, mmehost, mmeidentity_idmmeidentity,
    mmerealm, rand, sqn, subscription_data) VALUES ('460990010001045', 0033663000021,
    41, '000102030405060708090A0B0C0D0E0F', 'oai-mme.oai.svc.cluster.local', 4, 'oai.svc.cluster.local',
    '2683b376d1056746de3b254012908e0e', 96, '{\"Subscription-Data\":{\"Access-Restriction-Data\":41,\"Subscriber-Status\":0,\"Network-Access-Mode\":2,\"Regional-Subscription-Zone-Code\":[\"0x0123\",\"0x4567\",\"0x89AB\",\"0xCDEF\",\"0x1234\",\"0x5678\",\"0x9ABC\",\"0xDEF0\",\"0x2345\",\"0x6789\"],\"MSISDN\":\"0x0033663000021\",\"AMBR\":{\"Max-Requested-Bandwidth-UL\":50000000,\"Max-Requested-Bandwidth-DL\":100000000},\"APN-Configuration-Profile\":{\"Context-Identifier\":0,\"All-APN-Configurations-Included-Indicator\":0,\"APN-Configuration\":{\"Context-Identifier\":0,\"PDN-Type\":0,\"Served-Party-IP-Address\":[\"10.0.0.1\",\"10.0.0.2\"],\"Service-Selection\":\"apn.oai.svc.cluster.local\",\"EPS-Subscribed-QoS-Profile\":{\"QoS-Class-Identifier\":9,\"Allocation-Retention-Priority\":{\"Priority-Level\":15,\"Pre-emption-Capability\":0,\"Pre-emption-Vulnerability\":0}},\"AMBR\":{\"Max-Requested-Bandwidth-UL\":50000000,\"Max-Requested-Bandwidth-DL\":100000000},\"PDN-GW-Allocation-Type\":0,\"MIP6-Agent-Info\":{\"MIP-Home-Agent-Address\":[\"172.26.17.183\"]}}},\"Subscribed-Periodic-RAU-TAU-Timer\":0}}');\nINSERT

```    

3) Deploy:

 On the Master Node:
```
    root@master:~# cd app_aware/deployment/
    root@master:~/app_aware/deployment/ bash deploy-all

```
Wait until all pods are running.


#### UE Applications Install & Network Connectivity:

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

#### Create Traffic:

On the UEs:

```
root@ue:~# cd app_aware/scenarios/scenario3/
root@ue:~/app_aware/scenarios/scenario3/ bash ue1.sh
```

(for UE2: bash ue2.sh , for UE3: bash ue3.sh)

#### On-Demand Resource Provisioning:

Watch the logs on the Master Node:
   For App-Aware Predictor:
   `root@master:~# kubectl logs -f oai-spgwu-86bfc8f9f7-2zrf2 -c predictor -n oai`
    
   For FlexRAN:
   `root@master:~# kubectl logs -f flexran-588f7bc566-8kmjd -c predictor -n oai`
                    

#### Employ Kubeflow Pipeline:


1) First, destroy the 5G Deployment and the apps:

`root@master:~/app_aware/deployment/ bash destroy-all`

On the Master Node:

2) Create a database and a table inside MySQL Container: 

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

3) Install Kubeflow:
    
    On the Master Node:
```
    root@master:~# cd app_aware/deployment/kubeflow/install
    root@master:~/app_aware/deployment/kubeflow/install tar -xzvf kfctl_v1.0.2-0-ga476281_linux.tar.gz
    root@master:~/app_aware/deployment/kubeflow/install ./kfctl apply -V -f kfctl_k8s_istio.v1.0.2.yaml
```
After the installation, wait until all pods are running.


Deploy the 5G Network and the Applications:

`root@master:~/app_aware/deployment/ bash deploy-all.sh`




4) Deploy the pipeline volume:

`root@master:~# cd app_aware/deployment/kubeflow/pipeline-files`
`root@master:~/app_aware/deployment/kubeflow/pipeline-files kubectl create -f kubeflow-nfs-volume.yml`

Compile the pipeline script which will generate a yaml manifest (called app-aware-pipeline.yaml) the one will be uploaded to 
Kubeflow Pipelines service in order to run the pipeline:

`root@master:~/app_aware/deployment/kubeflow/pipeline-files python3 pipeline.py`

Then upload the yaml file in master_ip:31380 kubeflow service

