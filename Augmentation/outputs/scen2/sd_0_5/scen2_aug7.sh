
sleep 25.43

#SIP
sudo sipp -sn uac 192.168.3.102:1234 &
sleep 71.37
pkill sipp

sleep 4.05

#WEB-RTC
sudo chromium-browser 192.168.3.101:8000 --no-sandbox --disable-application-cache &
sleep 52.19
pkill chromium
