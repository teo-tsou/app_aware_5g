
sleep 25.28

#SIP
sudo sipp -sn uac 192.168.3.102:1234 &
sleep 70.24
pkill sipp

sleep 3.32

#WEB-RTC
sudo chromium-browser 192.168.3.101:8000 --no-sandbox &
sleep 51.7
pkill chromium