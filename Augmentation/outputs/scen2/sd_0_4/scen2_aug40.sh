
sleep 24.73

#SIP
sudo sipp -sn uac 192.168.3.102:1234 &
sleep 69.95
pkill sipp

sleep 5.23

#WEB-RTC
sudo chromium-browser 192.168.3.101:8000 --no-sandbox &
sleep 52.11
pkill chromium