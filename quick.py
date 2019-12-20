class PretrainedEmbedding(tf.keras.layers.Layer):
    """Non-trainable embedding layer."""

    def __init__(self, embeddings, rate=0.1):
        """"Instantiate the layer using a pre-defined embedding matrix."""
        self.embeddings = tf.constant(embeddings)
        # if you want to add some dropout (or normalization, etc.)
        self.dropout = tf.keras.layers.Dropout(rate=rate)

    def call(self, inputs, training=None):
        """Embed some input tokens and optionally apply dropout."""
        output = tf.nn.embedding_lookup(self.embeddings, inputs)
        return self.dropout(output, training=training)


my_model = tf.keras.models.Sequential([
    tf.keras.Input(input_shape, dtype=tf.int64),
    PretrainedEmbedding(embeddings_array),
    # insert any model architecture here
])
