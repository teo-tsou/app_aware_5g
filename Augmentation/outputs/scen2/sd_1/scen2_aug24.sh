
sleep 24.39

#SIP
sudo sipp -sn uac 192.168.3.102:1234 &
sleep 70.97
pkill sipp

sleep 4.21

#WEB-RTC
sudo chromium-browser 192.168.3.101:8000 --no-sandbox &
sleep 51.32
pkill chromium