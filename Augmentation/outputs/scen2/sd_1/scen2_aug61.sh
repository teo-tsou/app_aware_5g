
sleep 24.1

#SIP
sudo sipp -sn uac 192.168.3.102:1234 &
sleep 71.02
pkill sipp

sleep 4.64

#WEB-RTC
sudo chromium-browser 192.168.3.101:8000 --no-sandbox &
sleep 50.3
pkill chromium