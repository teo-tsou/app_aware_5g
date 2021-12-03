
sleep 27.98

#SIP
sudo sipp -sn uac 192.168.3.102:1234 &
sleep 70.75
pkill sipp

sleep 5.23

#WEB-RTC
sudo chromium-browser 192.168.3.101:8000 --no-sandbox &
sleep 50.51
pkill chromium