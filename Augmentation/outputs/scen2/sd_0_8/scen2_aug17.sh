
sleep 24.94

#SIP
sudo sipp -sn uac 192.168.3.102:1234 &
sleep 69.82
pkill sipp

sleep 5.43

#WEB-RTC
sudo chromium-browser 192.168.3.101:8000 --no-sandbox &
sleep 52.7
pkill chromium