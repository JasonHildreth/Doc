
var requestsArray = []; // Dynamic array to store the HTTP requests

/* Adds a listener to the onBeforeRequest event and stores a copy of
   the request to the requests array */
chrome.webRequest.onBeforeRequest.addListener( function(info) {
	console.log(info.url);
	requestsArray.push(info.url);
}, { urls: ["<all_urls>"] },[/* no options */]);

/* Adds a listener to the onConnect event, which signals the page has
   completed, and sends copies of the DOM and requests to the content
	 script */
chrome.runtime.onConnect.addListener(function(port) {
	/*
	// Process the DOM into a message and send to the content script
	port.postMessage({message: "_BEGIN_DOM_"});
	console.log(JSON.stringify(domJSON.toJSON(document.body)))
	port.postMessage({message: "" + JSON.stringify(domJSON.toJSON(document.body))});
	port.postMessage({message: "_END_DOM_"});
	*/

	// Traverse the requests array and send to the content script
	var i = 0;
	var length = requestsArray.length;
	var prefix = "BEGIN_HTTP_REQUEST_";
	var suffix = "_END_HTTP_REQUEST_"
	//port.postMessage({message: "_BEGIN_REQUESTS_"});
	for (i = 0; i < length; i++) {
		var message_with_tag = prefix + requestsArray[i] + suffix;
		console.log(message_with_tag);
		//port.postMessage({ message: "" + requestsArray[i] });
		port.postMessage({message: "" + message_with_tag });
	}
	//port.postMessage({message: "_END_REQUESTS_"});
});
