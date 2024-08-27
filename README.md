# converter
Decimal, Binary, Hexadecimal Converter
This application is a simple converter which can convert from/to: DEC, BIN, HEX

This solution aims to complete the homework assigned by Platomics GmbH.The pack is available in docker which can be deployed from:
ghcr.io/kissge83/converter:latest

The application is using Flask (micro web framework).
Basically, the converter is using port 8080 to avoid conflicts, but you can choose any other port for your purpose, please adjust the port number in the relevant section if this is your willing.

The application is designed to run in a docker container with Kubernetes.

The heartbeat of the application can called:

http://YOURIP:8080/health

USAGE:

There are two methods how you can use this simple calculator.

Option A)

You need to call the server on port 8080 -as standard- in the following way:

http://<IP>:8080/convert/VALUE/INPUT-FORMAT/OUTPUT-FORMAT

The INPUT-FORMAT and OUTPUT-FORMAT can be:
- dec
- bin
- hex

Examples: 

http://YOURIP:8080/convert/1010/bin/dec

http://YOURIP:8080/convert/10/dec/bin


Just so you know, you will get back the result in the required format.You can convert in any combination of the above formats.

Option B)

There is a simple webpage as well where you can use the converter: 

http://YOURIP:8080
