from locust import HttpUser, task, between


class QuickstartUser(HttpUser):
<<<<<<< Updated upstream
    def on_start(self):
        response = self.client.post(
            "/accounts/api/v2/jwt/create/",data={
            "email": "mmd@admin.com",
            "password": "123"
        }).json()

        self.client.headers = {"Authorization": f"Bearer {response.get('access', None)}"}
=======

    def on_start(self):
        response = self.client.post(
            "/accounts/api/v2/jwt/create/",
            data={"email": "mmd@admin.com", "password": "123"},
        ).json()

        self.client.headers = {
            "Authorization": f"Bearer {response.get('access', None)}"
        }
>>>>>>> Stashed changes

    @task
    def post_list(self):
        self.client.get("/blog/api/v1/post/post/")

    @task
    def category_list(self):
        self.client.get("/blog/api/v1/post/cat/")
<<<<<<< Updated upstream
=======

    @task
    def tag_list(self):
        self.client.get("/blog/api/v1/post/tag/")

    @task
    def index_blog(self):
        self.client.get("/blog/index/")

    @task
    def index_blog(self):
        self.client.get("/blog/index")
>>>>>>> Stashed changes
