
sleep 24.92

#SIP
sudo sipp -sn uac 192.168.3.102:1234 &
sleep 70.82
pkill sipp

sleep 6.4

#WEB-RTC
sudo chromium-browser 192.168.3.101:8000 --no-sandbox &
sleep 52.56
pkill chromium