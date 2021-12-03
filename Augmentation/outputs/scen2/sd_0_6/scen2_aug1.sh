
sleep 25.3

#SIP
sudo sipp -sn uac 192.168.3.102:1234 &
sleep 69.85
pkill sipp

sleep 4.74

#WEB-RTC
sudo chromium-browser 192.168.3.101:8000 --no-sandbox &
sleep 52.39
pkill chromium