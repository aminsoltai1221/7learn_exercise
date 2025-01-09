from abc import ABC,abstractmethod


# دکوریتور برای اطلاع‌رسانی به ناظران
def update_decorator(fn):
    def wrapper(self, state):  # دریافت self برای دسترسی به دستگاه
        result = fn(self, state)  # اجرای تابع اصلی
        for observer in self.obsrevers:  # اطلاع‌رسانی به تمام ناظران
            observer.update(state)
        return result
    return wrapper

class Device():
    
    obsrevers = []
    
    def __init__(self):
        self.state = "off"
    
    def switch_state(self, state):
        self.state = state
        self.update_state(state)
        
    @update_decorator    
    def update_state(self, state):
        match state:
            case "off":
                print(f"Device is {state}")
            case "on":
                print(f"Device is {state}")
            case "sleep":
                print(f"Device is {state}")



class Observer(ABC):
    @abstractmethod
    def update(self, state):
        pass


class Light(Observer):
    def update(self, state):
        print(f"Light reacts to state: {state}")


class Sound(Observer):
    def update(self, state):
        print(f"Sound reacts to state: {state}")


class USB(Observer):
    def update(self, state):
        print(f"USB reacts to state: {state}")



from abc import ABC, abstractmethod


# دکوریتور برای اطلاع‌رسانی به ناظران
def update_decorator(fn):
    def wrapper(self, state):  # دریافت self برای دسترسی به دستگاه
        result = fn(self, state)  # اجرای تابع اصلی
        for observer in self.obsrevers:  # اطلاع‌رسانی به تمام ناظران
            observer.update(state)
        return result
    return wrapper


class Device:
    def __init__(self):
        self.state = "off"
        self.obsrevers = []  # لیست ناظران

    def add_observer(self, observer):
        self.obsrevers.append(observer)  # اضافه کردن ناظر

    def switch_state(self, state):
        self.state = state
        self.update_state(state)

    @update_decorator
    def update_state(self, state):
        match state:
            case "off":
                print(f"Device is {state}")
            case "on":
                print(f"Device is {state}")
            case "sleep":
                print(f"Device is {state}")


class Observer(ABC):
    @abstractmethod
    def update(self, state):
        pass


class Light(Observer):
    def update(self, state):
        print(f"Light reacts to state: {state}")


class Sound(Observer):
    def update(self, state):
        print(f"Sound reacts to state: {state}")


class USB(Observer):
    def update(self, state):
        print(f"USB reacts to state: {state}")


# استفاده از کد
device = Device()

# ایجاد ناظران
light = Light()
sound = Sound()
usb = USB()

# اضافه کردن ناظران به دستگاه
device.add_observer(light)
device.add_observer(sound)
device.add_observer(usb)

# تغییر وضعیت دستگاه
device.switch_state("on")  # روشن کردن دستگاه
device.switch_state("off")  # خاموش کردن دستگاه
device.switch_state("sleep")  # حالت خواب
