
sleep 25.1

#SIP
sudo sipp -sn uac 192.168.3.102:1234 &
sleep 70.31
pkill sipp

sleep 5.2

#WEB-RTC
sudo chromium-browser 192.168.3.101:8000 --no-sandbox &
sleep 53.16
pkill chromium