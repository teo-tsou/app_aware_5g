
sleep 25.3

#SIP
sudo sipp -sn uac 192.168.3.102:1234 &
sleep 70.01
pkill sipp

sleep 4.8

#WEB-RTC
sudo chromium-browser 192.168.3.101:8000 --no-sandbox &
sleep 53.52
pkill chromium