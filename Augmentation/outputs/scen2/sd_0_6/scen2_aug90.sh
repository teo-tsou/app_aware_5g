
sleep 25.22

#SIP
sudo sipp -sn uac 192.168.3.102:1234 &
sleep 70.22
pkill sipp

sleep 5.44

#WEB-RTC
sudo chromium-browser 192.168.3.101:8000 --no-sandbox &
sleep 51.55
pkill chromium