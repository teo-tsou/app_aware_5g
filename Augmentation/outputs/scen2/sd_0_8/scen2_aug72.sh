
sleep 24.53

#SIP
sudo sipp -sn uac 192.168.3.102:1234 &
sleep 68.56
pkill sipp

sleep 5.47

#WEB-RTC
sudo chromium-browser 192.168.3.101:8000 --no-sandbox &
sleep 52.09
pkill chromium