# from tasks import add

# # Call the Celery task asynchronously
# result = add.delay(4, 6)

# # Do other work while the task is being processed...

# # Retrieve the result of the task (if needed)
# print("Task result:", result.get())



import redis

# Create a Redis client
redis_client = redis.Redis(host='localhost', port=6379, db=0)
