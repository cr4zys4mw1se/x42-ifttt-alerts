############################################################
# License: GNU GPLv3
#    x42 IFTTT Alerts - Receive notifications via the IFTTT app
#    Copyright (C) 2019  cr4zys4mw1se
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU General Public License as published by
#    the Free Software Foundation, either version 3 of the License, or
#    (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU General Public License for more details.
#
#    You should have received a copy of the GNU General Public License
#    along with this program.  If not, see <https://www.gnu.org/licenses/>.
############################################################
# Created by: cr4zys4mw1se
# Donation Addresses: https://github.com/cr4zys4mw1se/x42-ifttt-alerts/blob/master/README.md#donation-addresses
############################################################

import emoji, requests, time
from datetime import datetime

e=emoji
r=requests

def x42Balance():
    apiBase="http://IP:42220/api/"
    getBalance="Wallet/balance?WalletName="
    walletName="NAME"
    r=requests.get(apiBase+getBalance+walletName)
    tmpBalance=r.json()["balances"][0]["amountConfirmed"]
    tmpBal=float(tmpBalance)/100000000
    return tmpBal
def history():
    apiBase="http://IP:42220/api/"
    getHistory="Wallet/history?WalletName="
    walletName="NAME"
    r=requests.get(apiBase+getHistory+walletName)
    req=r.json()["history"][0]["transactionsHistory"][0]
    return req

x42list=[]
def alertMe():
    while True:
        now=datetime.now()
        current=x42Balance()
        sOr=history()
        if len(x42list) != 90:
            if not x42list:
                x42list.append(current)
            elif current not in x42list:
                if sOr["type"] == "staked":
                    report={}
                    report["value1"]=e.emojize(":grinning:\n\n", use_aliases=True)
                    report["value2"]=e.emojize(str(round(current,3))+" :tada:", use_aliases=True)
                    report["value3"]="\n\nTX: {}\n\n".format(sOr["id"])
                    r.post("https://maker.ifttt.com/trigger/STAKE-TRIGGERNAME/with/key/APIKEY", data=report)
                    x42list.clear()
                    x42list.append(current)
                elif sOr["type"] == "received":
                    report={}
                    report["value1"]=e.emojize(str(float(sOr["amount"]/100000000))+" x42 Received! :grinning:\n\n", use_aliases=True)
                    report["value2"]=e.emojize(str(round(current,3))+" :tada:", use_aliases=True)
                    report["value3"]="\n\nTX: {}\n\n".format(sOr["id"])
                    r.post("https://maker.ifttt.com/trigger/RECEIVED-TRIGGERNAME/with/key/APIKEY", data=report)
                    x42list.clear()
                    x42list.append(current)
            else:
                x42list.append(current)
        else:
            del x42list[0:88]
            alertMe()
        time.sleep(60.00)
try:
    now=datetime.now()
    print(e.emojize("   :mag_right:Started at: "+str(now.strftime("%r, on %m/%d/%Y:mag:")), use_aliases=True),end="\r")
    alertMe()
except ConnectionRefusedError:
    print(e.emojize("          :scream: Connection was Refused. :scream:          ", use_aliases=True))
    warn={}
    warn["value1"]=e.emojize("\n:warning:", use_aliases=True)
    warn["value2"]=e.emojize(":warning:\n", use_aliases=True)
    r.post("https://maker.ifttt.com/trigger/CONNECTIONERROR-TRIGGERNAME/with/key/APIKEY", data=warn)
    time.sleep(30.00)
    alertMe()
except KeyboardInterrupt:
    print(e.emojize("     :frowning: IFTTT alerts have been cancelled. :frowning:     ", use_aliases=True))
