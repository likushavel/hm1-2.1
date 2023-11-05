class Camera:
  def take_picture(self):
    print("Taking picture...")

class MobilePhone:
  def make_call(self):
    print("Making call...")

class CameraPhone(Camera,MobilePhone):
  def answer_call(self):
    print("Answering call...")

camera_phone = CameraPhone()
camera_phone.take_picture()
camera_phone.make_call()
camera_phone.answer_call()