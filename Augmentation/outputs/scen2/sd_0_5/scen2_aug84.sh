
sleep 25.16

#SIP
sudo sipp -sn uac 192.168.3.102:1234 &
sleep 71.95
pkill sipp

sleep 5.14

#WEB-RTC
sudo chromium-browser 192.168.3.101:8000 --no-sandbox &
sleep 51.96
pkill chromium