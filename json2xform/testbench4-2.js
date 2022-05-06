[
[{
"children":["Phrase Parser"]
"connections":[{
"receivers":[{
"receiver":{
"component":"Phrase Parser"
"port":"phrase"}}]
"senders":[{
"sender":{
"component":"_me"
"port":"phrase"}}]},{
"receivers":[{
"receiver":{
"component":"_me"
"port":"food order"}}]
"senders":[{
"sender":{
"component":"Phrase Parser"
"port":"order no choices"}}]},{
"receivers":[{
"receiver":{
"component":"_me"
"port":"food order"}}]
"senders":[{
"sender":{
"component":"Phrase Parser"
"port":"order with choices"}}]}]
"id":"cell_7"
"inputs":["phrase"]
"name":"Order Taker"
"outputs":["food order"]
"synccode":""}]]
