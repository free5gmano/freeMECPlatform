import base64
client_id = "0ulJa3GBEnsNAYUPwAxURrNyEi55Vr30VRytmavi"
secret = "w4RzeaDLtcoENlr5MMi7r6tTEU6M2EqTlGLvPzRLnS6y0O0aJBRi6Q1R4ji33LaLqte2M4lhFgtTBgfwVGUWeJtrmtxB31QAaCons2I49PKBng24Cqw1KSOGmEP3NaWO"
credential = "{0}:{1}".format(client_id, secret)
print(base64.b64encode(credential.encode("utf-8")))
