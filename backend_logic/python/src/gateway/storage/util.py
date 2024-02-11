import pika, json

def upload(f, fs, channel, access):
  try:
    fid = fs.put(f)
  except Exception as e:
    print(e)
    return f"internal server code, can't upload", 500

  message = {
    "video_fid": str(fid),
    "mp3_fid" : None,
    "username": access["username"],
  }

  try:
    channel.basic_publish(
      exchange="",
      routing_key="video",
      body= json.dumps(message),
      properties=pika.BasicProperties(
        delivery_mode=pika.spec.PERSISTENT_DELIVERY_MODE
      ),
    )
  except Exception as err:
    fs.delete(fid)
    print(err)
    return f"error on upload", 500