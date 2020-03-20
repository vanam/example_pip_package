
import numpy as np

# Context variable
TRANSFORMATION_CTX = None


class Transformation(object):
    """
    Generic affine transformation.
    """

    def __init__(self, matrix: np.ndarray):
        """

        :param matrix: Affine matrix of shape `[3, 3]`
        """
        self._matrix = matrix

    def __call__(self, vector: list) -> list:
        """
        Call transformation on a 2D vector
        :param vector: 2D vector [x, y]
        :return: Transformed 2D vector
        """
        if len(vector) == 2:
            vector = vector + [1]

        vector = np.asarray([vector]).T

        return list(np.dot(self._matrix, vector).T[0][0:2])

    def __matmul__(self, other: 'Transformation'):
        """
        Compose transformations.
        """
        return Transformation(np.dot(self._matrix, other._matrix))

    @property
    def matrix(self) -> np.ndarray:
        """
        :return: Affine matrix of shape `[3, 3]` of the transformation.
        """
        return self._matrix

    @property
    def reverse_matrix(self) -> np.ndarray:
        """
        :return: Affine matrix of shape `[3, 3]` of the reverse transformation.
        """
        return np.linalg.inv(self._matrix)

    def __enter__(self):
        """
        Operation performed upon entering a context using 'with'.
        """
        global TRANSFORMATION_CTX
        TRANSFORMATION_CTX = self @ TRANSFORMATION_CTX

    def __exit__(self, *args):
        """
        Operation performed upon exiting a context using 'with'.
        """
        global TRANSFORMATION_CTX
        TRANSFORMATION_CTX = Transformation(self.reverse_matrix) @ TRANSFORMATION_CTX


class Scaling(Transformation):
    """
    2D scaling.
    """

    def __init__(self, scale: int):
        """
        |s 0 0|
        |0 s 0|
        |0 0 1|

        :param scale: Symmetric scaling (same in <em>x</em> and <em>y</em>)
        """
        matrix = np.eye(3)
        matrix[0][0] = scale
        matrix[1][1] = scale
        super().__init__(matrix)


class Translation(Transformation):
    """
    2D translation.
    """

    def __init__(self, shift: list):
        """
        |1 0 x|
        |0 1 y|
        |0 0 1|

        :param shift: Translation [x, y]
        """
        matrix = np.eye(3)
        matrix[0][2] = shift[0]
        matrix[1][2] = shift[1]
        super().__init__(matrix)


# Init transformation context
TRANSFORMATION_CTX = Scaling(1)


def transform(vector: list) -> list:
    """
    Transform vector 2D vector using current transformation in context.
    :param vector: 2D vector [x, y]
    :return:
    """
    return TRANSFORMATION_CTX(vector)

