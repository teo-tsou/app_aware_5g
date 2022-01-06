#!/bin/bash

sudo modprobe 8021q
sudo vconfig add eth1 200
ifconfig eth1.200 up
sudo brctl addbr br0
sudo brctl addif br0 eth1.200
ifconfig br0 up
