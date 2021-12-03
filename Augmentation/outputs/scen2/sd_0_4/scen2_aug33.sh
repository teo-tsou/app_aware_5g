
sleep 25.49

#SIP
sudo sipp -sn uac 192.168.3.102:1234 &
sleep 70.44
pkill sipp

sleep 4.75

#WEB-RTC
sudo chromium-browser 192.168.3.101:8000 --no-sandbox &
sleep 51.88
pkill chromium