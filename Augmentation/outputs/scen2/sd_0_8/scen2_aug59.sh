
sleep 26.39

#SIP
sudo sipp -sn uac 192.168.3.102:1234 &
sleep 69.62
pkill sipp

sleep 4.98

#WEB-RTC
sudo chromium-browser 192.168.3.101:8000 --no-sandbox &
sleep 51.97
pkill chromium