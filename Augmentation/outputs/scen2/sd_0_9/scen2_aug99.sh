
sleep 27.43

#SIP
sudo sipp -sn uac 192.168.3.102:1234 &
sleep 70.23
pkill sipp

sleep 4.22

#WEB-RTC
sudo chromium-browser 192.168.3.101:8000 --no-sandbox &
sleep 51.8
pkill chromium