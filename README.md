# Siri - Cheshire Cat integration

## Proof of Concept on interfacing Mac Shortcuts with Cheshire Cat

Inspired by [Yue-Yang](https://github.com/Yue-Yang/ChatGPT-Siri)'s work with OpenAI's ChatGPT Siri interface, I tried to make [Cheshire Cat](https://github.com/pieroit/cheshire-cat) talk with Siri on MAC.

### Requirements
* MacOSX Ventura or later versions
* [Homebrew](https://brew.sh)
* [websocat](https://github.com/vi/websocat)
* [Cheshire Cat](https://github.com/pieroit/cheshire-cat) installed locally, or at least on a reachable IP address.

### Architecture
The PoC is very simple. From Siri, it asks for a prompt from the user. Then it uses an [Apple Script](https://github.com/xdatap1/siri-cheshire-cat/blob/main/applescript.txt) to send the message to the Cheshire Cat and retrieve the response. After that, it extracts the response from the JSON with simple [JavaScript](https://github.com/xdatap1/siri-cheshire-cat/blob/main/javascript.txt) and returns it to the user. You can run this with a textual prompt or voice. 

### Installation

To download the shortcut, click [here](https://www.icloud.com/shortcuts/277345a499994b51a1bf03ac08fadb27).

After installing it, you should see this:

![](Siri-Cheshire-Cat.png)

If you see the following, you have the scripting actions disabled:

![](disabled-script-actions.png)

Go to Preferences / Advanced and click the "Allow Running Scripts" option to enable it.

![](script-enabling.png)

Currently, Cheshire Cat exposes a [websocket](https://en.wikipedia.org/wiki/WebSocket) as the only way to talk with it. Unfortunately, Apple Shortcuts doesn't support WebSockets, so I solved this problem with [websocat](https://github.com/vi/websocat), a command line wrapper to WebSocket.

To install [websocat](https://github.com/vi/websocat) on Mac OSX you can use [Homebrew](https://brew.sh) or [MacPorts](https://www.macports.org). I used [Homebrew](https://brew.sh). Once you have installed it, check the full command path to update the AppleScript eventually.

Open a Terminal and type:

> % which websocat
> 
> /opt/homebrew/bin/websocat
> 

If the path is different from the above, you need to update accordingly [Apple Script](https://github.com/xdatap1/siri-cheshire-cat/blob/main/applescript.txt) line 4. Also, if you have Cheshire Cat installed on a different machine than localhost, you need to update 3 as well.

![](apple-script-changes.png)

### Usage

You can test the Siri-Cheshire-Cat shortcut with the play button on the top of the window, and it prompts textually:

![](prompt1.png)

And it will provide the answer based on the previous conversations:

![](answer1.png)

If you start Siri and ask "Run Cheshire Cat" it will interact the same way but with voice.

### Final Notes
This is just a Prof of Concept to evaluate Cheshire Cat interfacing from other applications, have fun, and learn new stuff. Since it uses AppleScript works only on Mac and cannot be run on iPhone or iPad. It could be implemented in different, more elegant ways. Feel free to fork and adapt it as you prefer. It's not going to be maintained in any way.