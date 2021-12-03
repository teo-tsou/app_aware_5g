
sleep 23.93

#SIP
sudo sipp -sn uac 192.168.3.102:1234 &
sleep 70.36
pkill sipp

sleep 4.47

#WEB-RTC
sudo chromium-browser 192.168.3.101:8000 --no-sandbox &
sleep 51.48
pkill chromium