
sleep 25.28

#SIP
sudo sipp -sn uac 192.168.3.102:1234 &
sleep 69.15
pkill sipp

sleep 4.69

#WEB-RTC
sudo chromium-browser 192.168.3.101:8000 --no-sandbox &
sleep 51.59
pkill chromium