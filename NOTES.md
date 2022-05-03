Using case4.drawio, fb.pl contains:

```
das_fact(connection, cell_6, cell_13).
das_fact(sender, cell_13, sender{component:"Order 2 Taker",port:"ot food order"}).
das_fact(receiver, cell_13, receiver{component:"Test Bench",port:"tbo1"}).
das_fact(connection, cell_6, cell_13).
das_fact(sender, cell_13, sender{component:"Order 2 Taker",port:"ot food order"}).
das_fact(receiver, cell_13, receiver{component:"Test Bench",port:"tbo1"}).
```

The connection is listed twice.  It should be listed only once.

Check: connections.md

---

2 edges in fb.pl
das_fact(kind,...,edge) is created in 3 places:
1. contains_edge1.md
2. contains_edge2.md
3. contains_edge3.md

