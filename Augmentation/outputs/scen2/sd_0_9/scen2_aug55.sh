
sleep 24.2

#SIP
sudo sipp -sn uac 192.168.3.102:1234 &
sleep 71.54
pkill sipp

sleep 4.96

#WEB-RTC
sudo chromium-browser 192.168.3.101:8000 --no-sandbox &
sleep 53.63
pkill chromium