from fastapi.logger import logger


def simple_encrypt(image,file_name,key):
    try:    
        image = bytearray(image)
        for index, values in enumerate(image):
            image[index] = values ^ key
        fin = open(f"app/uploads/encrypt_{file_name}", 'wb')
        fin.write(image)
        fin.close()
    except Exception:
        logger.info("error")


def simple_decrypt(source,key):
    try:
        fin = open(f"app/uploads/encrypt_{source}", 'rb')
        image = fin.read()
        fin.close()
            
        image = bytearray(image)
        for index, values in enumerate(image):
            image[index] = values ^ key
        
        fin = open(f"app/uploads/decrypt_{source}.jpg", 'wb')
        fin.write(image)
        fin.close()
    except Exception:
        logger.info("error")

    