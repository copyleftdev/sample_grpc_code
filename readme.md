# POC example grpc & pytest


Library requirements
```shell
pip install grpcio
pip install grpcio-tools
pip install pytest
```

Instructions
1. Run grpc server located in ```python tests/libs/greeter_server.py```
2. run sample tests ``` pytest tests/```

Bonus:
added what a healper class could look like when interacting with a grpc server located: ```tests/libs/power_module_healper.py```