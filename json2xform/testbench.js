[
[%name "HTML Button"
{
"children":[]
"connections":[]
"id":"cell_12"
"inputs":[]
"name":"HTML Button"
"outputs":["click"]
"synccode":"me.send (&quot;click&quot;, true);"}]
[%name "Phrase Faker"
{
"children":[]
"connections":[]
"id":"cell_15"
"inputs":["go"]
"name":"Phrase Faker"
"outputs":["short phrase""long phrase"]
"synccode":"&lt;div&gt;&amp;nbsp; &amp;nbsp; me.send (&quot;long phrase&quot;, &quot;I Want A Hamburger With Ketchup And Bacon And Pickles&quot;);&lt;/div&gt;&lt;div&gt;&lt;br&gt;&lt;/div&gt;"}]
[%name "Phrase Parser"
{
"children":[]
"connections":[]
"id":"cell_22"
"inputs":["phrase"]
"name":"Phrase Parser"
"outputs":["order no choices""order with choices""parse error""hook error"]
"synccode":""}]
[%name "Test Bench"
{
"children":["HTML Button""Phrase Faker""Order Taker"]
"connections":[{
"receivers":[{
"receiver":{
"component":"Phrase Faker"
"port":"go"}}]
"senders":[{
"sender":{
"component":"HTML Button"
"port":"click"}}]},{
"receivers":[{
"receiver":{
"component":"Order Taker"
"port":"phrase"}}]
"senders":[{
"sender":{
"component":"Phrase Faker"
"port":"short phrase"}}]},{
"receivers":[{
"receiver":{
"component":"Order Taker"
"port":"phrase"}}]
"senders":[{
"sender":{
"component":"Phrase Faker"
"port":"long phrase"}}]},{
"receivers":[{
"receiver":{
"component":"Test Bench"
"port":"food order"}}]
"senders":[{
"sender":{
"component":"Order Taker"
"port":"food order"}}]}]
"id":"cell_6"
"inputs":[]
"name":"Test Bench"
"outputs":["food order"]
"synccode":""}]
[%name "Order Taker"
{
"children":["Phrase Parser"]
"connections":[{
"receivers":[{
"receiver":{
"component":"Phrase Parser"
"port":"phrase"}}]
"senders":[{
"sender":{
"component":"Order Taker"
"port":"phrase"}}]},{
"receivers":[{
"receiver":{
"component":"Order Taker"
"port":"food order"}}]
"senders":[{
"sender":{
"component":"Phrase Parser"
"port":"order no choices"}}]},{
"receivers":[{
"receiver":{
"component":"Order Taker"
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
