
sleep 23.63

#SIP
sudo sipp -sn uac 192.168.3.102:1234 &
sleep 69.83
pkill sipp

sleep 5.02

#WEB-RTC
sudo chromium-browser 192.168.3.101:8000 --no-sandbox &
sleep 54.21
pkill chromium