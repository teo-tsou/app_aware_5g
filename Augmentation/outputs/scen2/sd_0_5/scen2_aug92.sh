
sleep 24.61

#SIP
sudo sipp -sn uac 192.168.3.102:1234 &
sleep 70.02
pkill sipp

sleep 5.55

#WEB-RTC
sudo chromium-browser 192.168.3.101:8000 --no-sandbox --disable-application-cache &
sleep 51.89
pkill chromium
