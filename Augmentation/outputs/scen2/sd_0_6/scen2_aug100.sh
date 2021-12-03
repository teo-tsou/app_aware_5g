
sleep 23.96

#SIP
sudo sipp -sn uac 192.168.3.102:1234 &
sleep 69.49
pkill sipp

sleep 6.57

#WEB-RTC
sudo chromium-browser 192.168.3.101:8000 --no-sandbox &
sleep 52.42
pkill chromium