
sleep 25.65

#SIP
sudo sipp -sn uac 192.168.3.102:1234 &
sleep 69.9
pkill sipp

sleep 5.25

#WEB-RTC
sudo chromium-browser 192.168.3.101:8000 --no-sandbox &
sleep 52.26
pkill chromium