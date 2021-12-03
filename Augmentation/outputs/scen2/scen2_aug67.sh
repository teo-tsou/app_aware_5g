
sleep 24.48

#SIP
sudo sipp -sn uac 192.168.3.102:1234 &
sleep 69.48
pkill sipp

sleep 5.33

#WEB-RTC
sudo chromium-browser 192.168.3.101:8000 --no-sandbox &
sleep 51.07
pkill chromium