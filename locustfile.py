from locust import HttpUser, task, between

class LoadTestUser(HttpUser):
    wait_time = between(1, 2)  # seconds between tasks

    @task(2)  # weighted to run more frequently
    def get_trans_status(self):
        headers = {
            "Content-Type": "application/json"
        }
        payload = {
            "app_id": "",
            "app_key": "",
            "transaction_ref_no": "250507051666"
        }
        self.client.post("/v3/CashoutRestV2.svc/GetTransStatus", json=payload, headers=headers)

    @task(1)
    def get_invoice_status(self):
        headers = {
            "Content-Type": "application/json"
        }
        payload = {
            "app_id": "",
            "app_key": "",
            "transaction_ref_no": "test446"
        }
        self.client.post("/v3/interapi.svc/GetInvoiceStatusV3", json=payload, headers=headers)
