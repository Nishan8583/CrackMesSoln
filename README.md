# Here lies writeup for some reversing challanges
## These binary are not created by me and i have downloaded from various resources

# Notes: 
Interesting Vulns:
1. Steam symlink, registry: a symlink is created with steams registry, that key has admin privs, change image path to executable and restart service:

Writeup: https://amonitoring.ru/article/steamclient-0day/
Exploit:https://github.com/roflsandwich/Steam-EoP/blob/master/SteamEoP.ps1
