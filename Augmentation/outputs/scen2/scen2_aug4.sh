
sleep 25.87

#SIP
sudo sipp -sn uac 192.168.3.102:1234 &
sleep 70.13
pkill sipp

sleep 4.94

#WEB-RTC
sudo chromium-browser 192.168.3.101:8000 --no-sandbox &
sleep 51.41
pkill chromium