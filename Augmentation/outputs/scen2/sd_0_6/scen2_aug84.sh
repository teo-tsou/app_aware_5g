
sleep 25.21

#SIP
sudo sipp -sn uac 192.168.3.102:1234 &
sleep 70.29
pkill sipp

sleep 5.84

#WEB-RTC
sudo chromium-browser 192.168.3.101:8000 --no-sandbox &
sleep 52.31
pkill chromium