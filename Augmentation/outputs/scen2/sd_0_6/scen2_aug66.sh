
sleep 24.27

#SIP
sudo sipp -sn uac 192.168.3.102:1234 &
sleep 71.66
pkill sipp

sleep 4.63

#WEB-RTC
sudo chromium-browser 192.168.3.101:8000 --no-sandbox &
sleep 53.22
pkill chromium