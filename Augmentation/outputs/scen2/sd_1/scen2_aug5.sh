
sleep 24.05

#SIP
sudo sipp -sn uac 192.168.3.102:1234 &
sleep 69.56
pkill sipp

sleep 4.82

#WEB-RTC
sudo chromium-browser 192.168.3.101:8000 --no-sandbox &
sleep 50.97
pkill chromium