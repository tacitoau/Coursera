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
