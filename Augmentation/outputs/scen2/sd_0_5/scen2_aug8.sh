
sleep 25.05

#SIP
sudo sipp -sn uac 192.168.3.102:1234 &
sleep 69.72
pkill sipp

sleep 4.75

#WEB-RTC
sudo chromium-browser 192.168.3.101:8000 --no-sandbox &
sleep 52.23
pkill chromium