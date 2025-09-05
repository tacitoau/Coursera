    def test_read_a_product(self):
        """ It should Read a Product """
        product = ProductFactory()
        product.create()
        found_product = Product.find(product.id)
        self.assertIsNotNone(found_product)
        self.assertEqual(found_product.id, product.id)
        self.assertEqual(found_product.name, product.name)
        self.assertEqual(found_product.category, product.category)
        self.assertEqual(found_product.available, product.available)
        self.assertEqual(found_product.price, product.price)

    def test_update_a_product(self):
        """ It should Update a Product """
        product = ProductFactory()
        product.create()
        self.assertIsNotNone(product.id)
        product.category = "Updated Category"
        product.update()
        found_product = Product.find(product.id)
        self.assertEqual(found_product.category, "Updated Category")

    def test_delete_a_product(self):
        """ It should Delete a Product """
        product = ProductFactory()
        product.create()
        self.assertEqual(len(Product.all()), 1)
        product.delete()
        self.assertEqual(len(Product.all()), 0)

    def test_list_all_products(self):
        """ It should List all Products in the database """
        products = ProductFactory.create_batch(5)
        for product in products:
            product.create()
        self.assertEqual(len(Product.all()), 5)

    def test_find_by_name(self):
        """ It should Find a Product by Name """
        ProductFactory(name="Test Product").create()
        ProductFactory(name="Another Product").create()
        products = Product.find_by_name("Test Product")
        self.assertEqual(len(products), 1)
        self.assertEqual(products[0].name, "Test Product")

    def test_find_by_category(self):
        """ It should Find a Product by Category """
        ProductFactory(category="Electronics").create()
        ProductFactory(category="Food").create()
        products = Product.find_by_category("Electronics")
        self.assertEqual(len(products), 1)
        self.assertEqual(products[0].category, "Electronics")

    def test_find_by_availability(self):
        """ It should Find Products by Availability """
        ProductFactory(available=True).create()
        ProductFactory(available=False).create()
        available_products = Product.find_by_availability(True)
        self.assertEqual(len(available_products), 1)
        self.assertTrue(available_products[0].available)
        unavailable_products = Product.find_by_availability(False)
        self.assertEqual(len(unavailable_products), 1)
        self.assertFalse(unavailable_products[0].available)
