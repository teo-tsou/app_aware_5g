
sleep 25.89

#SIP
sudo sipp -sn uac 192.168.3.102:1234 &
sleep 69.18
pkill sipp

sleep 5.4

#WEB-RTC
sudo chromium-browser 192.168.3.101:8000 --no-sandbox &
sleep 51.95
pkill chromium