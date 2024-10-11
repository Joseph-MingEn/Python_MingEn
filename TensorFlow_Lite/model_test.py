import tensorflow as tf
import numpy as np

# 加载 TensorFlow Lite 模型
interpreter = tf.lite.Interpreter(model_path='C:/Users/TUMINGEN/AndroidStudioProjects/imageport2/app/src/main/assets/model.tflite')
interpreter.allocate_tensors()

# 获取输入和输出张量的信息
input_details = interpreter.get_input_details()
output_details = interpreter.get_output_details()

# 准备一个随机输入样本，形状与模型输入形状一致
input_shape = input_details[0]['shape']
input_data = np.array(np.random.random_sample(input_shape), dtype=np.float32)

# 设置输入张量
interpreter.set_tensor(input_details[0]['index'], input_data)

# 运行推理
interpreter.invoke()

# 获取输出张量
output_data = interpreter.get_tensor(output_details[0]['index'])
print("Output data:", output_data)
