
sleep 24.59

#SIP
sudo sipp -sn uac 192.168.3.102:1234 &
sleep 70.14
pkill sipp

sleep 4.99

#WEB-RTC
sudo chromium-browser 192.168.3.101:8000 --no-sandbox &
sleep 51.27
pkill chromium