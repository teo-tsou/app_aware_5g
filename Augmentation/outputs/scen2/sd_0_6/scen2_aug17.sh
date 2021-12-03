
sleep 24.05

#SIP
sudo sipp -sn uac 192.168.3.102:1234 &
sleep 70.54
pkill sipp

sleep 4.91

#WEB-RTC
sudo chromium-browser 192.168.3.101:8000 --no-sandbox &
sleep 51.31
pkill chromium