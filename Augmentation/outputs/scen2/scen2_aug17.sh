
sleep 25.48

#SIP
sudo sipp -sn uac 192.168.3.102:1234 &
sleep 70.22
pkill sipp

sleep 6.12

#WEB-RTC
sudo chromium-browser 192.168.3.101:8000 --no-sandbox &
sleep 51.9
pkill chromium