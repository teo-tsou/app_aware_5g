
sleep 25.07

#SIP
sudo sipp -sn uac 192.168.3.102:1234 &
sleep 69.82
pkill sipp

sleep 4.69

#WEB-RTC
sudo chromium-browser 192.168.3.101:8000 --no-sandbox &
sleep 51.69
pkill chromium