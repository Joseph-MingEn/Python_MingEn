import tensorflow as tf
from tensorflow.keras.preprocessing import image_dataset_from_directory

# 定义目录路径
train_dir = 'C:/Users/TUMINGEN/Documents/kibo/dataset/train'
validation_dir = 'C:/Users/TUMINGEN/Documents/kibo/dataset/validation'

# 加载训练数据集
train_dataset = image_dataset_from_directory(
    train_dir,
    image_size=(224, 224),  # 调整图像大小
    batch_size=32,          # 批处理大小
    label_mode='int'        # 标签模式，选择'int'返回整数标签
)

# 打印类别名称以确认
class_names = train_dataset.class_names
print("Train Class names:", class_names)

# 加载验证数据集
validation_dataset = image_dataset_from_directory(
    validation_dir,
    image_size=(224, 224),
    batch_size=32,
    label_mode='int'
)

# 确认验证数据集类别名称一致
validation_class_names = validation_dataset.class_names
print("Validation Class names:", validation_class_names)

# 数据预处理（例如标准化）
def preprocess(image, label):
    image = tf.image.per_image_standardization(image)
    return image, label

train_dataset = train_dataset.map(preprocess)
validation_dataset = validation_dataset.map(preprocess)

# 获取类别数量
num_classes = len(class_names)

# 构建模型（与之前代码相同）
from tensorflow.keras.applications import MobileNetV2
from tensorflow.keras.layers import Dense, GlobalAveragePooling2D
from tensorflow.keras.models import Model

base_model = MobileNetV2(input_shape=(224, 224, 3), include_top=False, weights='imagenet')
base_model.trainable = False

x = base_model.output
x = GlobalAveragePooling2D()(x)
x = Dense(1024, activation='relu')(x)
predictions = Dense(num_classes, activation='softmax')(x)

model = Model(inputs=base_model.input, outputs=predictions)

model.compile(optimizer='adam',
              loss='sparse_categorical_crossentropy',
              metrics=['accuracy'])

# 训练模型
model.fit(train_dataset, epochs=10, validation_data=validation_dataset)

# 评估模型
test_loss, test_acc = model.evaluate(validation_dataset)
print('Test accuracy:', test_acc)

# 保存模型
model.save('kibo_model.h5')