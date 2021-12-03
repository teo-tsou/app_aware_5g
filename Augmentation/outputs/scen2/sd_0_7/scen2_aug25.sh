
sleep 24.24

#SIP
sudo sipp -sn uac 192.168.3.102:1234 &
sleep 70.65
pkill sipp

sleep 4.11

#WEB-RTC
sudo chromium-browser 192.168.3.101:8000 --no-sandbox &
sleep 52.36
pkill chromium