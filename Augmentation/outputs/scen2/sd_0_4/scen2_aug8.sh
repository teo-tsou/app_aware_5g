
sleep 25.24

#SIP
sudo sipp -sn uac 192.168.3.102:1234 &
sleep 69.74
pkill sipp

sleep 5.35

#WEB-RTC
sudo chromium-browser 192.168.3.101:8000 --no-sandbox &
sleep 52.34
pkill chromium