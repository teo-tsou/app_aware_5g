
sleep 24.49

#SIP
sudo sipp -sn uac 192.168.3.102:1234 &
sleep 69.56
pkill sipp

sleep 5.28

#WEB-RTC
sudo chromium-browser 192.168.3.101:8000 --no-sandbox &
sleep 52.59
pkill chromium