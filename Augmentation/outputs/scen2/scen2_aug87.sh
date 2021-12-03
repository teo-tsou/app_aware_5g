
sleep 24.93

#SIP
sudo sipp -sn uac 192.168.3.102:1234 &
sleep 69.37
pkill sipp

sleep 6.27

#WEB-RTC
sudo chromium-browser 192.168.3.101:8000 --no-sandbox &
sleep 52.32
pkill chromium