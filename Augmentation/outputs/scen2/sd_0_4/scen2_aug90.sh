
sleep 24.77

#SIP
sudo sipp -sn uac 192.168.3.102:1234 &
sleep 70.34
pkill sipp

sleep 4.85

#WEB-RTC
sudo chromium-browser 192.168.3.101:8000 --no-sandbox &
sleep 52.82
pkill chromium