import hazelcast

client = hazelcast.HazelcastClient()

distributed_map = client.get_map("py-lab-map").blocking()

for i in range(1000):
    distributed_map.put(i, f"py-value-{i}")

print(f"Запис завершено. Розмір мапи: {distributed_map.size()}")
print("Тепер можна перевіряти розподіл в Management Center.")

client.shutdown()