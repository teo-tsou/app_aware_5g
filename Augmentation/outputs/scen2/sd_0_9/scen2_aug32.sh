
sleep 25.23

#SIP
sudo sipp -sn uac 192.168.3.102:1234 &
sleep 70.41
pkill sipp

sleep 4.74

#WEB-RTC
sudo chromium-browser 192.168.3.101:8000 --no-sandbox &
sleep 53.04
pkill chromium