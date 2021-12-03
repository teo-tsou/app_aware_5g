
sleep 25.01

#SIP
sudo sipp -sn uac 192.168.3.102:1234 &
sleep 69.85
pkill sipp

sleep 5.16

#WEB-RTC
sudo chromium-browser 192.168.3.101:8000 --no-sandbox &
sleep 51.89
pkill chromium