
sleep 24.7

#SIP
sudo sipp -sn uac 192.168.3.102:1234 &
sleep 70.21
pkill sipp

sleep 4.66

#WEB-RTC
sudo chromium-browser 192.168.3.101:8000 --no-sandbox &
sleep 52.2
pkill chromium