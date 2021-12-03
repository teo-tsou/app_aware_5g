
sleep 27.27

#SIP
sudo sipp -sn uac 192.168.3.102:1234 &
sleep 69.29
pkill sipp

sleep 4.95

#WEB-RTC
sudo chromium-browser 192.168.3.101:8000 --no-sandbox &
sleep 53.97
pkill chromium