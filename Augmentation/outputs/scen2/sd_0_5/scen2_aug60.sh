
sleep 25.04

#SIP
sudo sipp -sn uac 192.168.3.102:1234 &
sleep 71.36
pkill sipp

sleep 4.97

#WEB-RTC
sudo chromium-browser 192.168.3.101:8000 --no-sandbox &
sleep 52.58
pkill chromium