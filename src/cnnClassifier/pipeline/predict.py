from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing import image
import numpy as np
import os


class PredictionPipeline:
    def __init__(self, filename):
        self.filename = filename

    def predict(self):
        # load model
        model = load_model(os.path.join("artifacts", "training", "model.keras"))

        imagename = self.filename
        test_image = image.load_img(imagename, target_size=(224, 224))
        test_image = image.img_to_array(test_image)
        test_image = np.expand_dims(test_image, axis=0)
        result = np.argmax(model.predict(test_image), axis=1)
        print(f"class predicted: {result}")

        if result[0] == 0:
            prediction = "Coccidiosis"
            return [{"image": prediction}]
        else:
            prediction = "Healthy"
            return [{"image": prediction}]


if __name__ == "__main__":
    try:
        filename = (
            r"artifacts\data_ingestion\Chicken-fecal-images\Healthy\healthy.12.jpg"
        )
        predictor = PredictionPipeline(filename=filename)
        pred = predictor.predict()
        print(f"Predicted label: {pred}")
    except Exception as e:
        raise e
