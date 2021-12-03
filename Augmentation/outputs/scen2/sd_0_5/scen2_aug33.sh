
sleep 24.35

#SIP
sudo sipp -sn uac 192.168.3.102:1234 &
sleep 70.39
pkill sipp

sleep 5.58

#WEB-RTC
sudo chromium-browser 192.168.3.101:8000 --no-sandbox &
sleep 52.21
pkill chromium