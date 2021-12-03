
sleep 25.19

#SIP
sudo sipp -sn uac 192.168.3.102:1234 &
sleep 69.15
pkill sipp

sleep 4.84

#WEB-RTC
sudo chromium-browser 192.168.3.101:8000 --no-sandbox &
sleep 52.2
pkill chromium