
sleep 23.16

#SIP
sudo sipp -sn uac 192.168.3.102:1234 &
sleep 71.9
pkill sipp

sleep 5.24

#WEB-RTC
sudo chromium-browser 192.168.3.101:8000 --no-sandbox &
sleep 54.31
pkill chromium