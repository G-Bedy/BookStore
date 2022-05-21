import sys

from paypalcheckoutsdk.core import PayPalHttpClient, SandboxEnvironment


class PayPalClient:
    def __init__(self):
        self.client_id = "AQJdXo97PCNmiAfZIG7jPFY8LEG1xjcIZ0-LX1ZCQ3DiyZ4t5-AkkBNwzi-cnh36mzTuwomQvJHK414N"
        self.client_secret = "EBTr2VFcQ-tACnpxieuVaDD8U47g6AkjLaEaFZvTcQ2Wv5ZyIHc0rMjivdFU82fB9ZDpv_5sAxN3WAfb"
        self.environment = SandboxEnvironment(client_id=self.client_id, client_secret=self.client_secret)
        self.client = PayPalHttpClient(self.environment)