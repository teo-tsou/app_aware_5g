
sleep 24.01

#SIP
sudo sipp -sn uac 192.168.3.102:1234 &
sleep 70.15
pkill sipp

sleep 5.06

#WEB-RTC
sudo chromium-browser 192.168.3.101:8000 --no-sandbox &
sleep 51.22
pkill chromium