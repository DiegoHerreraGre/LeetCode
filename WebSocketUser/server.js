import express from 'express';
import {engine} from 'express-handlebars';
import * as path from "node:path";
import {server as WebSocketServer} from 'websocket';
import http from 'http';
import dirname from './dirname.cjs'

const app = express();
const port = 8080;
const __dirname = dirname;

app.engine('handlebars', engine());
app.set('view engine', 'handlebars');
app.set('views', path.join(__dirname, 'views'))
app.listen(port, () => {
	console.log(`Listening in ${port}`);
});
app.get('/', (req, res) => {
	res.render('index')
})

const server = http.createServer((req, res) => {
	console.log(`${new Date()} Request received for ${req.url}`);
});

server.listen(8080, () => console.log(`${new Date()} Server listening on port 8080`));

const wsServer = new WebSocketServer({
	httpServer: server,
	autoAcceptConnections: false,
});

const originIsAllowed = (origin) => true;

wsServer.on('request', (req) => {
	if (!originIsAllowed(req.origin)) {
		req.reject();
		console.log(`${new Date()} Connection from origin ${req.origin} rejected.`);
		return;
	}
	const connection = req.accept('echo-protocol', req.origin);
	console.log(`${new Date()} Connection accepted.`);

	connection.on('message', (message) => {
		let logMessage;
		switch (message.type) {
			case 'utf8':
				logMessage = `Received message: ${message.utf8Data}`;
				connection.sendUTF(message.utf8Data);
				break;
			case 'binary':
				logMessage = `Received Binary Message of ${message.binaryData.length} bytes`;
				connection.sendBytes(message.binaryData);
				break;
			default:
				logMessage = 'Unrecognized message type';
		}
		console.log(logMessage);
	});

	connection.on('close', (reasonCode, description) =>
		console.log(`${new Date()} Peer ${connection.remoteAddress} disconnected.`));
});