
sleep 24.45

#SIP
sudo sipp -sn uac 192.168.3.102:1234 &
sleep 69.32
pkill sipp

sleep 5.05

#WEB-RTC
sudo chromium-browser 192.168.3.101:8000 --no-sandbox &
sleep 51.32
pkill chromium