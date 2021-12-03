
sleep 26.71

#SIP
sudo sipp -sn uac 192.168.3.102:1234 &
sleep 69.51
pkill sipp

sleep 3.02

#WEB-RTC
sudo chromium-browser 192.168.3.101:8000 --no-sandbox &
sleep 52.71
pkill chromium