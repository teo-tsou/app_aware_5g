
sleep 24.43

#SIP
sudo sipp -sn uac 192.168.3.102:1234 &
sleep 70.19
pkill sipp

sleep 5.04

#WEB-RTC
sudo chromium-browser 192.168.3.101:8000 --no-sandbox &
sleep 52.4
pkill chromium