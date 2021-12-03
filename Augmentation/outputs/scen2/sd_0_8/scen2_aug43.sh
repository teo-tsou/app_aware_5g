
sleep 25.18

#SIP
sudo sipp -sn uac 192.168.3.102:1234 &
sleep 70.0
pkill sipp

sleep 4.83

#WEB-RTC
sudo chromium-browser 192.168.3.101:8000 --no-sandbox &
sleep 52.65
pkill chromium