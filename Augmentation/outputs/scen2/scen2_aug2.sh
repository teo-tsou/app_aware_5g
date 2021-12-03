
sleep 25.84

#SIP
sudo sipp -sn uac 192.168.3.102:1234 &
sleep 69.58
pkill sipp

sleep 6.01

#WEB-RTC
sudo chromium-browser 192.168.3.101:8000 --no-sandbox &
sleep 51.52
pkill chromium