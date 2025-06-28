import hazelcast
import time

client = hazelcast.HazelcastClient()
map_name = "increment-map-nolock"
increment_map = client.get_map(map_name).blocking()

if increment_map.size() == 0:
    increment_map.lock("key")
    try:
        if increment_map.is_empty():
            increment_map.put("key", 0)
    finally:
        increment_map.unlock("key")
time.sleep(2)


for _ in range(10_000):
    value = increment_map.get("key")
    value += 1
    increment_map.put("key", value)


time.sleep(5)
final_value = increment_map.get("key")
print(f"Фінальне значення: {final_value}")

client.shutdown()