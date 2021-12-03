
sleep 24.98

#SIP
sudo sipp -sn uac 192.168.3.102:1234 &
sleep 71.35
pkill sipp

sleep 6.59

#WEB-RTC
sudo chromium-browser 192.168.3.101:8000 --no-sandbox &
sleep 52.16
pkill chromium