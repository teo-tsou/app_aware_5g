
sleep 25.01

#SIP
sudo sipp -sn uac 192.168.3.102:1234 &
sleep 68.69
pkill sipp

sleep 3.49

#WEB-RTC
sudo chromium-browser 192.168.3.101:8000 --no-sandbox &
sleep 51.48
pkill chromium