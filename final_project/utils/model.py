"""
The inception module layer.
The hourglass model, and its forward pass.
"""
import tensorflow as tf
from tensorflow.keras import layers, models

class Inception(layers.Layer):
    """Create inception module as a custum layer."""
    def __init__(self, input_dim=256, output_dim=256, inter_dim=32, size=[1, 3, 5, 7], name="C1_E1"):
        """
        Input
        - input_dim: reserved
        - output_dim: num of filters for conv1~4
        - inter_dim: num of filters for 1x1 conv
        - size: 1X4 list, filter size for conv1~4
        """
        super(Inception, self).__init__(name = name)
        # Block1
        self.Block1_conv1 = layers.Conv2D(output_dim/4, size[0], padding='SAME') # Conv1
        self.Block1_bn1 = layers.BatchNormalization()
        self.Block1_relu1 = layers.ReLU()
        # Block2
        self.Block2_conv1 = layers.Conv2D(inter_dim, 1, padding='SAME') # 1x1 conv
        self.Block2_bn1 = layers.BatchNormalization()
        self.Block2_relu1 = layers.ReLU()
        self.Block2_conv2 = layers.Conv2D(output_dim/4, size[1], padding='SAME') # Conv2
        self.Block2_bn2 = layers.BatchNormalization()
        self.Block2_relu2 = layers.ReLU()
        # Block3
        self.Block3_conv1 = layers.Conv2D(inter_dim, 1, padding='SAME') # 1x1 conv
        self.Block3_bn1 = layers.BatchNormalization()
        self.Block3_relu1 = layers.ReLU()
        self.Block3_conv2 = layers.Conv2D(output_dim/4, size[2], padding='SAME') # Conv3
        self.Block3_bn2 = layers.BatchNormalization()
        self.Block3_relu2 = layers.ReLU()
        # Block4
        self.Block4_conv1 = layers.Conv2D(inter_dim, 1, padding='SAME') # 1x1 conv
        self.Block4_bn1 = layers.BatchNormalization()
        self.Block4_relu1 = layers.ReLU()
        self.Block4_conv2 = layers.Conv2D(output_dim/4, size[3], padding='SAME') # Conv4
        self.Block4_bn2 = layers.BatchNormalization()
        self.Block4_relu2 = layers.ReLU()        

    def call(self, inputs):
        """
        Inception module forward.
        Input
        - inputs: inception module inputs
        Return
        - concatenated convolution result
        """
        # Block1 forward
        out1 = self.Block1_conv1(inputs) # pass Conv1
        out1 = self.Block1_bn1(out1)
        out1 = self.Block1_relu1(out1)
        # Block2 forward
        out2 = self.Block2_conv1(inputs) # pass 1x1 conv
        out2 = self.Block2_bn1(out2)
        out2 = self.Block2_relu1(out2)
        out2 = self.Block2_conv2(out2) # pass Conv2
        out2 = self.Block2_bn2(out2)
        out2 = self.Block2_relu2(out2)
        # Block3 forward
        out3 = self.Block3_conv1(inputs) # pass 1x1 conv
        out3 = self.Block3_bn1(out3)
        out3 = self.Block3_relu1(out3)
        out3 = self.Block3_conv2(out3) # pass Conv3
        out3 = self.Block3_bn2(out3)
        out3 = self.Block3_relu2(out3)
        # Block4 forward
        out4 = self.Block4_conv1(inputs) # pass 1x1 conv
        out4 = self.Block4_bn1(out4)
        out4 = self.Block4_relu1(out4)
        out4 = self.Block4_conv2(out4) # pass Conv2
        out4 = self.Block4_bn2(out4)
        out4 = self.Block4_relu2(out4)

        return tf.concat([out1, out2, out3, out4], axis=3) # concatenation along the third axis
# end of class Inception

class Hourglass(models.Model):
    """Create Hourglass model using Inception layers."""
    def __init__(self, input_height = 240, input_width = 320, name="model"):
        """
        The model has 20 inception modules and 2 Conv2D layers.
        Input
        - input_width
        - input_height
        - name
        """
        super(Hourglass, self).__init__(name = name)
        # First layer
        self.H1 = layers.Conv2D(filters=128, kernel_size=3, padding='SAME', name='H1') # H1
        # Channel1
        self.C1_E1 = Inception(256, 256, 32, [1, 3, 5, 7], 'C1_E1') # 20x15
        self.C1_E2 = Inception(256, 256, 32, [1, 3, 5, 7], 'C1_E2')
        self.C1_E3 = Inception(256, 256, 32, [1, 3, 5, 7], 'C1_E3')
        self.C1_E4 = Inception(256, 256, 32, [1, 3, 5, 7], 'C1_E4') # 40x30
        self.C1_E5 = Inception(256, 256, 32, [1, 3, 5, 7], 'C1_E5')
        # Channel2
        self.C2_E1 = Inception(256, 256, 32, [1, 3, 5, 7], 'C2_E1') # 80x60
        self.C2_F1 = Inception(256, 256, 64, [1, 3, 7, 11], 'C2_F1')
        self.C2_E2 = Inception(256, 256, 32, [1, 3, 5, 7], 'C2_E2') # 40x30
        self.C2_E3 = Inception(256, 256, 32, [1, 3, 5, 7], 'C2_E3')
        self.C2_E4 = Inception(256, 256, 32, [1, 3, 5, 7], 'C2_E4')
        self.C2_F2 = Inception(256, 256, 64, [1, 3, 7, 11], 'C2_F2')
        # Channel3
        self.C3_B1 = Inception(128, 128, 32, [1, 3, 5, 7], 'C3_B1') # 160x120
        self.C3_C1 = Inception(128, 128, 64, [1, 3, 7, 11], 'C3_C1')
        self.C3_B2 = Inception(128, 128, 32, [1, 3, 5, 7], 'C3_B2') #  80x60
        self.C3_D1 = Inception(128, 256, 32, [1, 3, 5, 7], 'C3_D1')
        self.C3_E1 = Inception(256, 256, 32, [1, 3, 5, 7], 'C3_E1')
        self.C3_G1 = Inception(256, 128, 32, [1, 3, 5, 7], 'C3_G1')
        # Channel4
        self.C4_A1 = Inception(128, 64, 64, [1, 3, 7, 11], 'C4_A1') # 320x240
        self.C4_B1 = Inception(128, 128, 32, [1, 3, 5, 7], 'C4_B1') # 160x120
        self.C4_B2 = Inception(128, 128, 32, [1, 3, 5, 7], 'C4_B2')
        self.C4_B3 = Inception(128, 128, 32, [1, 3, 5, 7], 'C4_B3')
        self.C4_A2 = Inception(128, 64, 64, [1, 3, 7, 11], 'C4_A2')
        # Last layer
        self.H2 = layers.Conv2D(filters=1, kernel_size=3, padding='SAME', activation='relu', name='H2') # H2
        

    def call(self, inputs):
        """
        Hourglass model forward.
        Input
        - inputs: images, with size [240, 320, 3]
        Return
        - depth result
        """
        out_H1 = self.H1(inputs) # 320x240x128
        out_C4_A1 = self.C4_A1(out_H1) # 320x240x64
        out_C4_B1 = self.C4_B1(layers.AveragePooling2D(pool_size=(2, 2), name='C4_pooling')(out_H1)) # 160x120x128
        out_C4_B2 = self.C4_B2(out_C4_B1) # 160x120x128
        out_C3_B1 = self.C3_B1(out_C4_B2) # 160x120x128
        out_C3_C1 = self.C3_C1(out_C3_B1) # 160x120x128
        out_C3_B2 = self.C3_B2(layers.AveragePooling2D(pool_size=(2, 2), name='C3_pooling')(out_C4_B2)) # 80x60x128
        out_C3_D1 = self.C3_D1(out_C3_B2) # 80x60x256
        out_C2_E1 = self.C2_E1(out_C3_D1) # 80x60x256
        out_C2_F1 = self.C2_F1(out_C2_E1) # 80x60x256
        out_C2_E2 = self.C2_E2(layers.AveragePooling2D(pool_size=(2, 2), name='C2_pooling')(out_C3_D1)) # 40x30x256
        out_C2_E3 = self.C2_E3(out_C2_E2) # 40x30x256
        out_C1_E4 = self.C1_E4(out_C2_E3) # 40x30x256
        out_C1_E5 = self.C1_E5(out_C1_E4) # 40x30x256
        out_C1_E1 = self.C1_E1(layers.AveragePooling2D(pool_size=(2, 2), name='C1_pooling')(out_C2_E3)) # 20x15x256
        out_C1_E2 = self.C1_E2(out_C1_E1) # 20x15x256
        out_C1_E3 = layers.UpSampling2D(size=(2, 2), name='C1_up')(self.C1_E3(out_C1_E2)) # 40x30x256
        out_C1_add = layers.Add(name='C1_add')([out_C1_E5, out_C1_E3]) # 40x30x256
        out_C2_E4 = self.C2_E4(out_C1_add) # 40x30x256
        out_C2_F2 = layers.UpSampling2D(size=(2, 2), name='C2_up')(self.C2_F2(out_C2_E4)) # 80x60x256
        out_C2_add = layers.Add(name='C2_add')([out_C2_F1, out_C2_F2]) # 80x60x256
        out_C3_E1 = self.C3_E1(out_C2_add) # 80x60x256
        out_C3_G1 = layers.UpSampling2D(size=(2, 2), name='C3_up')(self.C3_G1(out_C3_E1)) # 160x120x128
        out_C3_add = layers.Add(name='C3_add')([out_C3_C1, out_C3_G1]) # 160x120x128
        out_C4_B3 = self.C4_B3(out_C3_add) # 160x120x128
        out_C4_A2 = layers.UpSampling2D(size=(2, 2), name='C4_up')(self.C4_A2(out_C4_B3)) # 320x240x64
        out_C4_add = layers.Add(name='C4_add')([out_C4_A1, out_C4_A2])
        out_H2 = self.H2(out_C4_add) # 320x240x1
        
        return out_H2
    
    def my_summary(self, input_width = 320, input_height = 240):
        """
        This function is defined to substitute the original .summary() function, so that
        the Output Shape can be fully displayed instead of showing a lot of "multiple".
        """
        x = layers.Input(shape=(input_height, input_width, 3), name='Input_image')
        return models.Model(inputs=[x], outputs=self.call(x)).summary()
    def plot_network(self, input_width = 320, input_height = 240, name = 'model_Hourglass.png'):
        """
        This function is defined to plot the whole model.
        """
        x = layers.Input(shape=(input_height, input_width, 3), name='Input_image')
        return tf.keras.utils.plot_model(models.Model(inputs=[x], outputs=self.call(x)), to_file= name, show_shapes=True, show_layer_names=True)