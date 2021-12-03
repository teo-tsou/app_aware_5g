
sleep 25.16

#SIP
sudo sipp -sn uac 192.168.3.102:1234 &
sleep 68.88
pkill sipp

sleep 3.22

#WEB-RTC
sudo chromium-browser 192.168.3.101:8000 --no-sandbox &
sleep 53.76
pkill chromium