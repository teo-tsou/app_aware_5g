
sleep 24.59

#SIP
sudo sipp -sn uac 192.168.3.102:1234 &
sleep 70.22
pkill sipp

sleep 4.56

#WEB-RTC
sudo chromium-browser 192.168.3.101:8000 --no-sandbox &
sleep 51.67
pkill chromium