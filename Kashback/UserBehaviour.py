from locust import HttpLocust, Locust, TaskSet, task
import requests.packages.urllib3
import time
import json

requests.packages.urllib3.disable_warnings()

##http://kasback.digiapt.com:5272/#!/home
class UserBehaviour(TaskSet):
    cookie=None
    sellerCokie=None
    def on_start(self):
        self.cookie=self.loginBuyer()
        self.sellerCokie=self.loginSeller()
    def loginBuyer(self):
        payload = {"email": "sachi.technocrat@gmail.com", "password": "Sachi!234"}
        response = self.client.post(
            "/auth", verify=False, json=payload, name='login')
        if response.status_code==200:
            print "cookie " +json.dumps(response.content)
            return response.cookies
    def loginSeller(self):
        payload={"email":"automationtrainer1@gmail.com","password":"Sachi!234"}
        response = self.client.post(
            "/auth", verify=False, json=payload, name='login')
        if response.status_code == 200:
            print "cookie " + json.dumps(response.content)
            return response.cookies
    @task(50)
    def filterElectronicsItem(self):
        payload={"category_ids":[6,12]}
        response = self.client.post(
            "/non_real_estate/product/filter?itemsPerPage=100&pageNo=1", verify=False, json=payload, cookies=self.sellerCokie,name='filter electronics item')
        response = self.client.post(
            "/category/", verify=False, json=payload,cookies=self.sellerCokie,
            name='get electronics category')
    @task(50)
    def additemsBySeller(self):
        payload={"name":"Apples","category_id":33,"brand":"American Apple","model_number":"1234","short_desc":"50 Kg Apples","long_desc":"50  KG Red american apples @100Rs/Kg","price":100,"quantity":50,"colour":"Red","margin_rate":50,"weight":"1","unit_id":"7","hsn_code":"2303","hsn_id":103}
        response=self.client.post("/non_real_estate",verify=False, json=payload, cookies=self.sellerCokie,name='add items by seller')
    @task(100)
    def getMainPage(self):
        response = self.client.get(
            "/#!/home" , verify=False, name='main Page')
        print("Main Page response code:", response.status_code)
        response = self.client.get(
            "/auth/isLoggedIn", verify=False, name='is logged In')
        print("Main Page is logged In response code:", response.status_code)
        response = self.client.get(
            "/real_estate", verify=False, name='/real_estate')
        print("Main Page category response code:", response.status_code)
        response = self.client.get(
            "/category/2", verify=False, name='category2')
        print("category 2 response code:", response.status_code)
        response = self.client.get(
             "/modules/home/views/home.client.view.html", verify=False, name='home page')
        print("Main Page category response code:", response.status_code)
        response = self.client.get(
            "/cart", verify=False, name='cart')
        print("cart view response code:", response.status_code)
        response = self.client.get(
            "/modules/auth/views/login.client.view.html", verify=False, name='login page')
        print("login page response code:", response.status_code)
        response = self.client.get(
            "/modules/non_real_estate_product/views/cart_2.client.view.html", verify=False, name='cart view')
        print("cart view response code:", response.status_code)

    @task(50)
    def getViewGroceries(self):
        response = self.client.get(
            "/modules/non_real_estate_product/views/viewAllGroceries.client.view.html", cookies=self.cookie, verify=False, name='Groceries1')
        print("groceries1 response code:", response.status_code)

    @task(50)
    def getViewItems(self):
        response = self.client.get(
            "/non_real_estate?isGroceries=true&itemsPerPage=10&pageNo=1", cookies=self.cookie, verify=False, name='Groceries2')
        print("groceries2 response code:", response.status_code)
    #/non_real_estate?isGroceries=true&itemsPerPage=10&pageNo=1


    @task(100)
    def getMainPage(self):
        response = self.client.get(
            "/category/2", verify=False, name='category')
        print("Main Page category response code:", response.status_code)

    @task(50)
    def getMainPage(self):
        payload={"email":"sachi.technocrat@gmail.com","password":"Sachi!234"}
        response = self.client.post(
            "/auth", verify=False,json=payload, name='login')
        print("login response code:", response.status_code)

    @task(50)
    def getProductView(self):
        response = self.client.get(
            "/modules/non_real_estate_product/views/viewNonRealEstateProduct.client.view.html", cookies=self.cookie, verify=False, name='view product list')
        print("View product response code:", response.status_code)
        response = self.client.get(
            "/non_real_estate/38", verify=False,
            name='view product item')
        print("View product response code:", response.status_code)
        response = self.client.get(
            "/category/ancestors/Mens", verify=False, cookies=self.cookie,
            name='view product item detail')
        print("View product item detail page response code:", response.status_code)
        response = self.client.get(
            "/category/ancestors/fresh%20vegetables", verify=False, cookies=self.cookie,
            name='get product search results')
        print("get product search results response code:", response.status_code)
    def getProducts(self):
        response = self.client.get(
            "/modules/non_real_estate_product/views/viewAllNonRealEstateProducts1.client.view.html", verify=False, cookies=self.cookie,
            name='view electronics item detail')
        print("View electronics item detail page response code:", response.status_code)

        response = self.client.get(
            "/modules/real_estate_product/views/comingSoon.client.view.html", verify=False,
            cookies=self.cookie,
            name='view real estate item detail')
        print("View real estate item detail page response code:", response.status_code)
        response = self.client.get(
            "/amenity", verify=False,
            cookies=self.cookie,
            name='view real estate amenities detail')
        print("View real estate item detail page response code:", response.status_code)
        response = self.client.get(
            "/modules/non_real_estate_product/views/viewAllGroceries.client.view.html", verify=False,
            cookies=self.cookie,
            name='view groceries item detail')
        print("View groceries item detail page response code:", response.status_code)
        response = self.client.get(
            "/non_real_estate?isGroceries=true&itemsPerPage=10&pageNo=1", verify=False,
            cookies=self.cookie,
            name='view groceries page 1')
        print("View groceries page 1 response code:", response.status_code)
        response = self.client.get(
            "/category/2", verify=False,
            cookies=self.cookie,
            name='view category 2')
        print("View category 2 response code:", response.status_code)

    @task(30)
    def getUserProfile(self):
        response = self.client.get(
            "/modules/user/views/userProfile.client.view.html", verify=False,
            cookies=self.cookie,
            name='view user profile')
        print("View user profile response code:", response.status_code)
        response = self.client.get(
            "/user/200", verify=False,
            cookies=self.cookie,
            name='view user profile 200')
        print("View user profile response code:", response.status_code)
    @task(5)
    def updateUserProfile(self):
        payload={"f_name":"Buyer","l_name":"Test","email":"sachi.technocrat@gmail.com","type":"buyer","phone":9560754084,"gender":"Male"}
        response=self.client.put("/user",json=payload,cookies=self.cookie, name='update user profile')
    def updateUserAddress(self):
        payload={"f_name":"Buyer","l_name":"Test","email":"sachi.technocrat@gmail.com","type":"buyer","phone":9560754084,"gender":"Male"}
        response=self.client.put("/address",json=payload,cookies=self.cookie, name='update user address')
    def updateUserAddress(self):
        response=self.client.get("/user/200",cookies=self.cookie, name='get user address')
    @task(20)
    def getFavouratories(self):
        response = self.client.get("/modules/non_real_estate_product/views/favourites.client.view.html", cookies=self.cookie, name='get favourateries')
    def getFavouratories2(self):
        response = self.client.get("/favourite", cookies=self.cookie, name='get favourateries2')
    def manageAddress(self):
        response = self.client.get("/modules/user/views/manageAddress1.client.view.html", cookies=self.cookie, name='manage address')
    def comingsoonePage(self):
        response = self.client.get("/modules/real_estate_product/views/comingSoon.client.view.html", cookies=self.sellerCokie,
                                   name='seller coming soon page')
    def viewSellerDashboard(self):
        response = self.client.get("/order/seller?itemsPerPage=10&pageNo=1", cookies=self.sellerCokie,
                                   name='seller coming soon page')
    @task(25)
    def buynow(self):
        payload={"product_id":29}
        response = self.client.post(
            "/order/buyNow", verify=False, json=payload, cookies=self.cookie,
            name='buynow')
        response = self.client.get(
            "/modules/non_real_estate_product/views/checkout.client.view.html", verify=False, json=payload, cookies=self.cookie,
            name='client checkout')
        response = self.client.get(
            "/address/user", verify=False, json=payload,
            cookies=self.cookie,
            name='get user address')
    def getAdd2Cart(self):
        payload={"product_id":36}
        response = self.client.get(
            "/cart", verify=False, json=payload, cookies=self.cookie,
            name='add 2 cart')
        print("add 2 cart response code:", response.status_code)
        checkoutpayload={"selection":[],"totalPoints":None,"totalPrice":600}
        response= self.client.get(
            "/modules/non_real_estate_product/views/cart_2.client.view.html", verify=False, cookies=self.cookie,
            name='view cart')
        print("view cart code:", response.status_code)
        response = self.client.get(
            "/cart", verify=False, cookies=self.cookie,
            name='view cart2')
        print("view cart code2:", response.status_code)
        response = self.client.post(
            "/order/checkout/", verify=False, json=checkoutpayload, cookies=self.cookie,
            name='checkout')
        print("checkout response code:", response.status_code)
        response = self.client.get(
            "/modules/non_real_estate_product/views/checkout.client.view.html", verify=False, json=payload, cookies=self.cookie,
            name='list checkout item')
        print("list checkout items response code:", response.status_code)
        response = self.client.get(
            "/address/user", verify=False, json=payload, cookies=self.cookie,
            name='get user address')
        print("get user address response code:", response.status_code)
    @task(100)
    def getProdSearchResults(self):
        response = self.client.get(
            "/non_real_estate/product/filter?isGroceries=true", cookies=self.cookie, verify=False, name='prod search result')
        print("prod search result:", response.status_code)
        response = self.client.get(
            "/auth/isLoggedIn", verify=False, name='Login page is logged In')
        print("Main Page is logged In response code:", response.status_code)

class Console(HttpLocust):


    task_set = UserBehaviour
    min_wait = 5000
    max_wait = 20000
