
sleep 25.37

#SIP
sudo sipp -sn uac 192.168.3.102:1234 &
sleep 69.04
pkill sipp

sleep 4.38

#WEB-RTC
sudo chromium-browser 192.168.3.101:8000 --no-sandbox &
sleep 51.54
pkill chromium