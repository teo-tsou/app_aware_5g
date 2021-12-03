
sleep 24.68

#SIP
sudo sipp -sn uac 192.168.3.102:1234 &
sleep 71.12
pkill sipp

sleep 4.92

#WEB-RTC
sudo chromium-browser 192.168.3.101:8000 --no-sandbox &
sleep 52.08
pkill chromium