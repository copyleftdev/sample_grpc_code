from __future__ import print_function
import pytest
import grpc
from faker import Faker
from tests.libs import helloworld_pb2, helloworld_pb2_grpc

locales = [
    "az_AZ",
    "ar_AA",
    "ar_PS",
    "hu_HU",
    "zh_TW",
    "zh_CN",
    "ru_RU",
    "sl_SI",
    "ja_JP",
    "ta_IN",
]


supported_locales_test_names = []
char_lengths = ["a" * 10, "a" * 100, "a" * 1000, "a" * 10000]
for l in locales:
    fake = Faker(f"{l}")
    supported_locales_test_names.append(fake.first_name())


@pytest.mark.parametrize("name", supported_locales_test_names)
def test_grpc_call_validate_supported_locale_handles_characters_correctly(name):
    first_name = fake.first_name()
    with grpc.insecure_channel("localhost:50051") as channel:
        stub = helloworld_pb2_grpc.GreeterStub(channel)
        response = stub.SayHello(helloworld_pb2.HelloRequest(name=first_name))
    assert f"Hello, {first_name}!" == response.message


@pytest.mark.parametrize("chars_set", char_lengths)
def test_min_max_values_for_name_parameter_respond_with_appropriate_response(chars_set):
    with grpc.insecure_channel("localhost:50051") as channel:
        stub = helloworld_pb2_grpc.GreeterStub(channel)
        response = stub.SayHello(helloworld_pb2.HelloRequest(name=chars_set))
    assert f"Hello, {chars_set}"
