
sleep 23.48

#SIP
sudo sipp -sn uac 192.168.3.102:1234 &
sleep 68.75
pkill sipp

sleep 5.96

#WEB-RTC
sudo chromium-browser 192.168.3.101:8000 --no-sandbox &
sleep 48.86
pkill chromium