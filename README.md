# x42 IFTTT Alerts

A Python Script that communicates with your x42-FullNode.

The script will check your x42-FullNode every **60** seconds to determine if you have staked a block or received an x42 deposit. If a block has been staked, you will receive an "App" Notification via IFTTT. If a deposit is received, a similar alert will trigger notifying how much was deposited. Both alerts will contain the TX id.


##### Notification Preview:
![Received Transaction](https://i.postimg.cc/9F6Q2kJV/received.png) ![Staked Block](https://i.postimg.cc/pTL2kMXQ/staked.png)


# Contents:
   * [Requirements](#requirements)
      * [IFTTT](#ifttt)
   * [Edits Required](#edits-required)
   * [How-To](#how-to)
      * [Applet Configuration](#applet-configuration)
   * [Side-Notes](#side-notes)
___


## Requirements:
1. [x42-FullNode](https://github.com/x42protocol/X42-FullNode)
2. Python 3.x *`(Personal Preference: Python3-dev [sudo apt install python3-dev])`*
3. Pip3 *`sudo apt install python3-pip`*
4. Requests `pip3 install requests`
5. Emoji `pip3 install emoji`
6. IFTTT Account and Application

### IFTTT
* [IFTTT Account](https://ifttt.com/join)
  * [IFTTT Android App](https://play.google.com/store/apps/details?id=com.ifttt.ifttt&utm_source=/&utm_medium=web)
  * [IFTTT iOS App](https://itunes.apple.com/app/apple-store/id660944635?mt=8)


## Edits Required:
* General edits that _**need**_ to be made to `ifttt.py`:
  * `apiBase="http://IP:42220/api/"` - Replace **IP** based on node configuration with either `127.0.0.1`, `localhost` or the **INTERNAL IP** (ex. `192.168.1.205`) of the Node. _**The x42.conf may need editing, check [Side-Notes](#side-notes) for more information**_
  * `walletName="NAME"` - Replace **NAME** with your x42 Wallet name (**`NAME`**`.wallet.json`, *do **not** append* `.wallet.json`)
  * `r.post("https://maker.ifttt.com/trigger/TRIGGERNAME/with/key/APIKEY", data=)` - There are **3** entries of `r.post()` that need edits. Replace **TRIGGERNAME** with the IFTTT *Event Name* and the **APIKEY** with your *Webhooks* URL (ex. `WbSpblmUBWY16RH5AtTWORSbwJNpFH8zKVNckNtP095`)


## How-To:
You have a few options on how to run the script. You can run it on a separate device within the same network, or on the device running the x42-FullNode.
1. **Same Device** - Use nohup *(Linux and Mac)*... Command: `nohup python3 -u ifttt.py &` - press *Enter* twice and you're done.
    * Nohup will output information to `nohup.out`
2. **Separate Device** - Use the regluar command `python3 ifttt.py` *OR* the nohup command above.
  * If you _**ONLY**_ have Python 3.x installed without Python 2.x you can use the command `python ifttt.py` instead of `python3 ifttt.py`
    * *Nohup* is **not** available for Windows. A possible alternative to run *minimized* is `start /min python ifttt.py` - Take this command with a grain of salt though as I use Linux not Windows. You *may* have access to nohup if you're using [WSL on Windows 10](https://docs.microsoft.com/en-us/windows/wsl/install-win10).


## Applet Configuration:
  * This script **_REQUIRES_ 3** IFTTT applets:
    1. Staked: ```Block staked! {{Value1}}Your new x42 balance is: {{Value2}} {{Value3}}Reported on: {{OccurredAt}}```
    2. Received: ```{{Value1}}Your new x42 balance is: {{Value2}} {{Value3}}Reported on: {{OccurredAt}}```
    3. Connection Error: ```The connection was refused while checking your Balance. Your x42 Node may be down! {{Value1}}Retrying in 30s...{{Value2}} Reported on: {{OccurredAt}}```

**Create the Applet(s)**:
  1. *My Applets*
  2. *New Applet*
  3. *if* **THIS** = *Webhooks*
  4. *Trigger* = Receive a Web Request
  5. **TRIGGERNAME** `(stake, received, connect_error)`
  6. *Then* = _**Notifications**_
  7. *Send a notification from the **IFTTT** app*
  8. *Message* = use config(s) above.
  9. _**Create Action**_


## Side-Notes:
  * For _**my**_ personal configuration *(not advised)*, I adjusted the `x42.conf` and edited the line `apiuri=` under `####API Settings####`. Set `apiuri=http://0.0.0.0` to allow the use of the *internal IP* and/or *localhost* in the `apiBase` rather than `127.0.0.1` only. 
    * **NOTE**: Port *42220* is _**NOT**_ open *externally* and I **DO NOT** advise opening it _**EVER**_. Leave the port _**CLOSED**_ to prevent *external* network access to your node api.
  * If you're using a VPS: 
    1. *Do **NOT** edit the `apiuri`* in the `x42.conf`.
    2. Set the `apiBase` IP to `127.0.0.1`.
    3. If you're not binding the port to your local system, use the **Same Device** option in the [How-To](#how-to).
    * *If* you *are* binding the port locally, you will still use `127.0.0.1` for the IP in the `apiBase` using the **Separate Device** option in the [How-To](#how-to) instead.
---


### *Donation Addresses:*
  * **x42:** XKCm56Q4GmxRYbk3aS8seAQaHdtUDpgEfx
  * **BTC:** 145QLo9jopWK3Z7h43fEgTy7AbUA239Ghz
  * **LTC:** LVkLucNkv43Zwpqx1Vb1mymnQR2YLPXzZR


### *To-Do:*
- [x] Add IFTTT Python Script
- [x] IFTTT Applet Configurations
- [x] IFTTT Notification Image(s)/Preview
- [ ] ~~Re-organize readme? *(:thinking:)*~~
- [x] Add License
- [ ] Script Adjustments? *(possibly add `x42 sent` alert)*
- [ ] ?
