import hazelcast
import time

client = hazelcast.HazelcastClient()
increment_map = client.get_map("increment-map-pessimistic").blocking()
increment_map.put_if_absent("key", 0)
start_time = time.time()

for _ in range(10_000):
    increment_map.lock("key")
    try:
        value = increment_map.get("key")
        value += 1
        increment_map.put("key", value)
    finally:
        increment_map.unlock("key")

end_time = time.time()
print(f"Завершено за {end_time - start_time:.2f} секунд.")

time.sleep(5)
final_value = increment_map.get("key")
print(f"Фінальне значення: {final_value}")

client.shutdown()