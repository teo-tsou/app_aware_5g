
sleep 24.78

#SIP
sudo sipp -sn uac 192.168.3.102:1234 &
sleep 68.93
pkill sipp

sleep 4.95

#WEB-RTC
sudo chromium-browser 192.168.3.101:8000 --no-sandbox &
sleep 52.99
pkill chromium