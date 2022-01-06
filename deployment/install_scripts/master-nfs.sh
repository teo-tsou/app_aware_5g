!/bin/bash
sudo apt-get install -y nfs-kernel-server && sudo mkdir -p /mnt/nfs_server_files && echo '/mnt/nfs_server_files  *(rw,insecure,sync,no_subtree_check,no_root_squash)' >> /etc/exports && exportfs -a && exportfs -a

