
sleep 23.79

#SIP
sudo sipp -sn uac 192.168.3.102:1234 &
sleep 69.11
pkill sipp

sleep 4.85

#WEB-RTC
sudo chromium-browser 192.168.3.101:8000 --no-sandbox &
sleep 52.45
pkill chromium