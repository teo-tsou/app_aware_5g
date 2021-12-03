
sleep 24.5

#SIP
sudo sipp -sn uac 192.168.3.102:1234 &
sleep 69.54
pkill sipp

sleep 3.78

#WEB-RTC
sudo chromium-browser 192.168.3.101:8000 --no-sandbox &
sleep 53.22
pkill chromium