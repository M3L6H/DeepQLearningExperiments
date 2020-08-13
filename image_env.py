from PIL import Image


class Vector2D:
  def __init__(self, x=0, y=0):
    self.x, self.y = x, y
    
    if isinstance(x, list) or isinstance(x, tuple):
      self.x = x[0]
      self.y = y[0]
    elif isinstance(x, Vector2D):
      self.x = x.x
      self.y = x.y


  def __add__(self, other):
    if isinstance(other, Vector2D):
      return Vector2D(self.x + other.x, self.y + other.y)
    elif isinstance(other, list) or isinstance(other, tuple):
      return Vector2D(self.x + other[0], self.y + other[1])
    elif isinstance(other, int) or isinstance(other, float):
      return Vector2D(self.x + other, self.y + other)
    else:
      return NotImplemented


  def __sub__(self, other):
    if isinstance(other, Vector2D):
      return Vector2D(self.x - other.x, self.y - other.y)
    elif isinstance(other, list) or isinstance(other, tuple):
      return Vector2D(self.x - other[0], self.y - other[1])
    elif isinstance(other, int) or isinstance(other, float):
      return Vector2D(self.x - other, self.y - other)
    else:
      return NotImplemented


  # Performs dot multiplication in the case of another vector
  def __mul__(self, other):
    if isinstance(other, Vector2D):
      return self.x * other.x + self.y * other.y
    elif isinstance(other, list) or isinstance(other, tuple):
      return self.x * other[0] + self.y * other[1]
    elif isinstance(other, int) or isinstance(other, float):
      return Vector2D(self.x * other, self.y * other)


class Window:
  def __init__(self, size, pos=Vector2D(0, 0), zoom=1):
    self.size = size
    self.pos = pos
    self.zoom = zoom

  
  def __update_image(self):
    self.pix = Image.open(self.image_path).thumbnail(self.size * self.zoom).load()

  
  def __set_zoom(self, zoom):
    if not self.image_path:
      raise RuntimeError("Cannot set zoom without image!")

    self.zoom = zoom
    self.__update_image()


  def set_image(self, image_path):
    self.image_path = image_path
    self.__update_image()

  
  def zoom_in(self):
    self.__set_zoom(self.zoom + 1)


  def zoom_out(self):
    if self.zoom > 1:
      self.__set_zoom(self.zoom - 1)


  def translate(self, offset):
    # We translate proportionally to the zoom level to avoid losing ourselves
    # when we are zoomed closer
    self.pos += offset * self.zoom


class ImageEnv:
  def __init__(self, window_size=64, num_windows=16):
    self.window_size = window_size
    self.num_windows = num_windows

    print(f"Initialized image environment with\n\twindow_size: { window_size }\n\tnum_windows: { num_windows }")


  def set_image(self, image_path):
    self.image_path = image_path
    self.image = Image.open(image_path)
    self.pix = self.image.load()
    print(f"Loaded { image_path }")


env = ImageEnv()
path = r"C:\Users\Michael\Desktop\Images\Ahsoka\Ahsoka-Hi-Res-0SFW-01.jpg"
env.set_image(path)
