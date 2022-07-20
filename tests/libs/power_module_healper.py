import grpc
# import power_module_pb2_grpc, power_module_pb2
# assuming these are the name's of the proto files

class PowerModuleUtil(object):

    def __init__(self, host: str):
        self.host = host
        self.channel = grpc.insecure_channel(self.host)

    def set_manual_mode(self, status: bool) -> str:
        """This method can set Manual Mode to True/False"""
        stub = power_module_pb2_grpc.PowerModuleStub(self.channel)
        response = stub.setState(power_module_pb2.Mode(status=status))
        return response.status

    def set_fan_speed(self, speed: int) -> str:
        """This method will set speed of charger fan"""
        stub = power_module_pb2_grpc.PowerModuleStub(self.channel)
        response = stub.setFanSpeed(power_module_pb2.Fan(speed=speed))
        return response.speed