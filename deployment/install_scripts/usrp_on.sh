sudo route add default gw 10.0.1.200 eth0
curl 10.1.0.55/usrpoff
curl 10.1.0.55/usrpon
sudo route delete default gw 10.0.1.200 eth0

