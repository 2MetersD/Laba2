import hazelcast
import time

client = hazelcast.HazelcastClient()
queue = client.get_queue("bounded-py-queue").blocking()

print(f"Consumer ({client.name}) чекає на завдання...")

while True:
    item = queue.take()
    print(f"Consumer ({client.name}): прочитав {item}")
    time.sleep(0.5)