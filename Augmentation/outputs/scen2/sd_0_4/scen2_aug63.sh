
sleep 24.87

#SIP
sudo sipp -sn uac 192.168.3.102:1234 &
sleep 69.98
pkill sipp

sleep 4.68

#WEB-RTC
sudo chromium-browser 192.168.3.101:8000 --no-sandbox &
sleep 52.31
pkill chromium