import hazelcast
import time

client = hazelcast.HazelcastClient()
increment_map = client.get_map("increment-map-optimistic").blocking()
increment_map.put_if_absent("key", 0)
start_time = time.time()

for _ in range(10_000):
    while True:
        old_value = increment_map.get("key")
        if old_value is None:
            old_value = 0

        new_value = old_value + 1
        if increment_map.replace_if_same("key", old_value, new_value):
            break

end_time = time.time()
print(f"Завершено за {end_time - start_time:.2f} секунд.")

time.sleep(5)
final_value = increment_map.get("key")
print(f"Фінальне значення: {final_value}")

client.shutdown()