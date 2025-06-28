import hazelcast
import time

client = hazelcast.HazelcastClient()
queue = client.get_queue("bounded-py-queue").blocking()

for i in range(1, 101):
    print(f"Producer: додаю {i}")
    queue.put(i)
    time.sleep(0.1)

print("Producer завершив роботу.")
client.shutdown()