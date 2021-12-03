
sleep 24.58

#SIP
sudo sipp -sn uac 192.168.3.102:1234 &
sleep 70.56
pkill sipp

sleep 5.29

#WEB-RTC
sudo chromium-browser 192.168.3.101:8000 --no-sandbox &
sleep 51.72
pkill chromium