
sleep 23.13

#SIP
sudo sipp -sn uac 192.168.3.102:1234 &
sleep 67.86
pkill sipp

sleep 4.95

#WEB-RTC
sudo chromium-browser 192.168.3.101:8000 --no-sandbox &
sleep 52.34
pkill chromium