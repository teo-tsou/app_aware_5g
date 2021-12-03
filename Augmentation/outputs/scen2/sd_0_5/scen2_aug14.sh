
sleep 24.9

#SIP
sudo sipp -sn uac 192.168.3.102:1234 &
sleep 69.48
pkill sipp

sleep 6.43

#WEB-RTC
sudo chromium-browser 192.168.3.101:8000 --no-sandbox --disable-application-cache &
sleep 52.38
pkill chromium
