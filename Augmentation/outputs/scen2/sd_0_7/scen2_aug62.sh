
sleep 24.69

#SIP
sudo sipp -sn uac 192.168.3.102:1234 &
sleep 69.61
pkill sipp

sleep 4.87

#WEB-RTC
sudo chromium-browser 192.168.3.101:8000 --no-sandbox &
sleep 51.43
pkill chromium