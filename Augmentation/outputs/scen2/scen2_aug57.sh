
sleep 25.24

#SIP
sudo sipp -sn uac 192.168.3.102:1234 &
sleep 69.83
pkill sipp

sleep 6.81

#WEB-RTC
sudo chromium-browser 192.168.3.101:8000 --no-sandbox &
sleep 52.26
pkill chromium