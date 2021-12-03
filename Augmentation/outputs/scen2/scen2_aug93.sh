
sleep 25.93

#SIP
sudo sipp -sn uac 192.168.3.102:1234 &
sleep 71.16
pkill sipp

sleep 3.83

#WEB-RTC
sudo chromium-browser 192.168.3.101:8000 --no-sandbox &
sleep 51.43
pkill chromium