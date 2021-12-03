
sleep 23.72

#SIP
sudo sipp -sn uac 192.168.3.102:1234 &
sleep 69.71
pkill sipp

sleep 6.11

#WEB-RTC
sudo chromium-browser 192.168.3.101:8000 --no-sandbox &
sleep 51.22
pkill chromium