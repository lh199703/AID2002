with open("songzuer.jpg", "rb") as f1:
    with open("../../mm.jpg", "wb") as f2:
        while True:
            values = f1.read(100)
            f2.write(values)
            if not values:
                break


