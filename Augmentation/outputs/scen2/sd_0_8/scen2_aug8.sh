
sleep 24.28

#SIP
sudo sipp -sn uac 192.168.3.102:1234 &
sleep 69.62
pkill sipp

sleep 5.26

#WEB-RTC
sudo chromium-browser 192.168.3.101:8000 --no-sandbox &
sleep 51.07
pkill chromium