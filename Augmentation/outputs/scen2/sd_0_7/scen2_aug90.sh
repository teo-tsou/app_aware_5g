
sleep 26.26

#SIP
sudo sipp -sn uac 192.168.3.102:1234 &
sleep 69.58
pkill sipp

sleep 4.76

#WEB-RTC
sudo chromium-browser 192.168.3.101:8000 --no-sandbox &
sleep 52.04
pkill chromium