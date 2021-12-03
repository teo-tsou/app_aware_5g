
sleep 25.92

#SIP
sudo sipp -sn uac 192.168.3.102:1234 &
sleep 71.05
pkill sipp

sleep 4.44

#WEB-RTC
sudo chromium-browser 192.168.3.101:8000 --no-sandbox &
sleep 52.74
pkill chromium