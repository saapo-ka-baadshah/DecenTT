# DecenTT Notes

- Every DecenTT client should have two running clients:
    - MQTT Client
    - IPFS Client


---

## MQTT Client Notes
- MQTT Client Subscriptions are internally threaded and are closed when client closes

- Hence add compatiblity to the IPFS Client as well. IPFS Client closing should close all active threads

- DecenTT as well!!

---

## DecenTT Client Notes

### How to decide the switching between IPFS and MQTT ??
- based on topic
- based on sender
- based on message

### Based on Topic
- categorization:
    - based on a Neural Network -> Invisible
    - based on a prefix/suffix -> Manual -> **This approach is used in this research !**

### Based on Sender
- categorization:
    - based on a Neural Network -> Invisible
    - flagging the sender -> Manual

### Based on Message
- categorization:
    - based on a Neural Network -> Invisible
    - based on a prefix/suffix -> Manual