
sleep 24.78

#SIP
sudo sipp -sn uac 192.168.3.102:1234 &
sleep 69.55
pkill sipp

sleep 5.41

#WEB-RTC
sudo chromium-browser 192.168.3.101:8000 --no-sandbox &
sleep 50.94
pkill chromium