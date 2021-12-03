
sleep 24.74

#SIP
sudo sipp -sn uac 192.168.3.102:1234 &
sleep 70.46
pkill sipp

sleep 5.49

#WEB-RTC
sudo chromium-browser 192.168.3.101:8000 --no-sandbox --disable-application-cache &
sleep 52.14
pkill chromium
