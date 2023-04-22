# cheshire-cat-web-bridge
### A Rest API bridge to Cheshire Cat Websocket PoC

This is a proof of concept of a REST API Bridge to the Cheshire Cat WebSocket. It is an evolution of the [Siri Cheshire Cat integration](https://github.com/xdatap1/siri-cheshire-cat) Proof of Concept.

### Requirements
* Python
	* Flask
	* Flask-Cors
	* websockets

### Installation

To install Python requirements, run

> pip install -r requirements.txt

And then run the app.py

> python3 app.py

It will start listening at port 3500. To test it, just run open test.html with your browser. It should work as the following. If not, try to make it work with the web first since the next step is harder to debug. If you need help with debugging, try the app-verbose.py, which shows on the terminal what is receiving from the user and the Cheshire Cat.

![](webtest.png)
 
 If it works as expected, you can try the next step: make it work with Siri!
 
 Install the shortcut from [here](https://www.icloud.com/shortcuts/880466f7577e4bbf9325e2be38f3fb52). Open it; it should look like the following:
 
 ![](Shortcut.png)
 
 Edit the text to insert your IP address (mine is 192.168.1.4) and test it.
 
 As the [previous version](https://github.com/xdatap1/siri-cheshire-cat) works in both text and voice.
 
 Now you can activate wifi on your iPhone or iPad and try it also from your iOS devices.
 
 
### Final Notes
This is just a Prof of Concept to evaluate Cheshire Cat interfacing from other applications, have fun, and learn new stuff. To get a little help, I must confess that I used ChatGPT. So the code might be redundant and not very elegant. Feel free to fork and adapt it as you prefer. It's not going to be maintained in any way.