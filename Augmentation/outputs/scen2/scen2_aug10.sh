
sleep 25.3

#SIP
sudo sipp -sn uac 192.168.3.102:1234 &
sleep 70.51
pkill sipp

sleep 3.82

#WEB-RTC
sudo chromium-browser 192.168.3.101:8000 --no-sandbox &
sleep 51.36
pkill chromium