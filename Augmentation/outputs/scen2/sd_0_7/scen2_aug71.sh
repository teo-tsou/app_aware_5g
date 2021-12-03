
sleep 25.12

#SIP
sudo sipp -sn uac 192.168.3.102:1234 &
sleep 69.51
pkill sipp

sleep 4.77

#WEB-RTC
sudo chromium-browser 192.168.3.101:8000 --no-sandbox &
sleep 51.35
pkill chromium