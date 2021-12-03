
sleep 25.69

#SIP
sudo sipp -sn uac 192.168.3.102:1234 &
sleep 69.8
pkill sipp

sleep 4.58

#WEB-RTC
sudo chromium-browser 192.168.3.101:8000 --no-sandbox --disable-application-cache &
sleep 51.57
pkill chromium
