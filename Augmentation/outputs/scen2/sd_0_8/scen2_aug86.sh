
sleep 25.24

#SIP
sudo sipp -sn uac 192.168.3.102:1234 &
sleep 71.09
pkill sipp

sleep 4.52

#WEB-RTC
sudo chromium-browser 192.168.3.101:8000 --no-sandbox &
sleep 51.73
pkill chromium