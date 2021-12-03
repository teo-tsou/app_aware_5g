
sleep 24.04

#SIP
sudo sipp -sn uac 192.168.3.102:1234 &
sleep 71.03
pkill sipp

sleep 5.34

#WEB-RTC
sudo chromium-browser 192.168.3.101:8000 --no-sandbox &
sleep 53.55
pkill chromium