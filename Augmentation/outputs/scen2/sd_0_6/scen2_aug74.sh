
sleep 24.53

#SIP
sudo sipp -sn uac 192.168.3.102:1234 &
sleep 70.92
pkill sipp

sleep 5.04

#WEB-RTC
sudo chromium-browser 192.168.3.101:8000 --no-sandbox &
sleep 52.38
pkill chromium