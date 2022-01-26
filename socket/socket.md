##

close() releases the resource associated with a connection but does not necessarily close the connection immediately. If you want to close the connection in a timely fashion, call shutdown() before close().

I dont get clear idea behind but for client site i beleive case shuld be like this 

Client: 

send -> shutdown
listen (wait here)

then in the end you can close() the client socket /... 

server received aftre shutdown method used in client side , detect EOF by refceiving 0 bytes. Then understand connection going lstening mode. 

Also other recommondation when you done with your (client) socket because automatical process takes time

(Probably) in client site your socket running in the thread, dont kill thread manuelly . That cused problem (client just hang the connection according to server) os, finish your process in client site (with close() ) and wait thread automatically dissapears 



