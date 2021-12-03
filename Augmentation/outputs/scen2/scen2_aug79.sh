
sleep 26.7

#SIP
sudo sipp -sn uac 192.168.3.102:1234 &
sleep 70.21
pkill sipp

sleep 4.71

#WEB-RTC
sudo chromium-browser 192.168.3.101:8000 --no-sandbox &
sleep 52.97
pkill chromium