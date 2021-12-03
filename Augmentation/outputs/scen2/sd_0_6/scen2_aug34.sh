
sleep 24.96

#SIP
sudo sipp -sn uac 192.168.3.102:1234 &
sleep 69.79
pkill sipp

sleep 5.71

#WEB-RTC
sudo chromium-browser 192.168.3.101:8000 --no-sandbox &
sleep 51.1
pkill chromium