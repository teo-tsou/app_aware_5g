#!/bin/bash

sudo apt-get install -y nfs-common && sudo mkdir -p /mnt/nfs_client_files && echo 'master:/mnt/nfs_server_files        /mnt/nfs_client_files     nfs     auto    0       0' >> /etc/fstab && mount -a

