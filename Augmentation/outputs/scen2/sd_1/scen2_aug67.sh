
sleep 25.29

#SIP
sudo sipp -sn uac 192.168.3.102:1234 &
sleep 70.49
pkill sipp

sleep 5.11

#WEB-RTC
sudo chromium-browser 192.168.3.101:8000 --no-sandbox &
sleep 51.33
pkill chromium