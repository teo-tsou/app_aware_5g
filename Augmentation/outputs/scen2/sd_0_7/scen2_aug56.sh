
sleep 26.04

#SIP
sudo sipp -sn uac 192.168.3.102:1234 &
sleep 69.09
pkill sipp

sleep 5.18

#WEB-RTC
sudo chromium-browser 192.168.3.101:8000 --no-sandbox &
sleep 52.63
pkill chromium