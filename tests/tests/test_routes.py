    def test_read_product(self):
        """ It should Get a single Product """
        product = self._create_products(1)[0]
        response = self.client.get(f"{BASE_URL}/{product.id}")
        self.assertEqual(response.status_code, 200)
        data = response.get_json()
        self.assertEqual(data["name"], product.name)

    def test_update_product(self):
        """ It should Update an existing Product """
        test_product = self._create_products(1)[0]
        new_category = "Super Category"
        test_product.category = new_category
        response = self.client.put(f"{BASE_URL}/{test_product.id}", json=test_product.serialize())
        self.assertEqual(response.status_code, 200)
        updated_product = response.get_json()
        self.assertEqual(updated_product["category"], new_category)

    def test_delete_product(self):
        """ It should Delete a Product """
        product = self._create_products(1)[0]
        response = self.client.delete(f"{BASE_URL}/{product.id}")
        self.assertEqual(response.status_code, 204)
        response = self.client.get(f"{BASE_URL}/{product.id}")
        self.assertEqual(response.status_code, 404)

    def test_list_all_products(self):
        """ It should Get a list of Products """
        self._create_products(5)
        response = self.client.get(BASE_URL)
        self.assertEqual(response.status_code, 200)
        data = response.get_json()
        self.assertEqual(len(data), 5)

    def test_list_by_name(self):
        """ It should List Products by Name """
        self._create_products(1)
        test_product = ProductFactory(name="SearchByName")
        self.client.post(BASE_URL, json=test_product.serialize())
        response = self.client.get(BASE_URL, query_string=f"name={test_product.name}")
        self.assertEqual(response.status_code, 200)
        data = response.get_json()
        self.assertEqual(len(data), 1)
        self.assertEqual(data[0]["name"], test_product.name)

    def test_list_by_category(self):
        """ It should List Products by Category """
        self._create_products(1)
        test_product = ProductFactory(category="SearchByCategory")
        self.client.post(BASE_URL, json=test_product.serialize())
        response = self.client.get(BASE_URL, query_string=f"category={test_product.category}")
        self.assertEqual(response.status_code, 200)
        data = response.get_json()
        self.assertEqual(len(data), 1)
        self.assertEqual(data[0]["category"], test_product.category)

    def test_list_by_availability(self):
        """ It should List Products by Availability """
        self._create_products(1)
        test_product_available = ProductFactory(available=True)
        self.client.post(BASE_URL, json=test_product_available.serialize())
        test_product_unavailable = ProductFactory(available=False)
        self.client.post(BASE_URL, json=test_product_unavailable.serialize())

        response = self.client.get(BASE_URL, query_string="available=true")
        self.assertEqual(response.status_code, 200)
        data = response.get_json()
        self.assertEqual(len(data), 1)
        self.assertTrue(data[0]["available"])

        response = self.client.get(BASE_URL, query_string="available=false")
        self.assertEqual(response.status_code, 200)
        data = response.get_json()
        self.assertEqual(len(data), 1)
        self.assertFalse(data[0]["available"])
