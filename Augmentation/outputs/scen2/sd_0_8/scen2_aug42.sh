
sleep 24.81

#SIP
sudo sipp -sn uac 192.168.3.102:1234 &
sleep 69.01
pkill sipp

sleep 5.57

#WEB-RTC
sudo chromium-browser 192.168.3.101:8000 --no-sandbox &
sleep 52.08
pkill chromium