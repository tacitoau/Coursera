    @api.doc(\'get_products\')
    @api.marshal_with(product_model)
    def get(self, product_id):
        """ Returns a single Product """
        app.logger.info("Request to get product with id [%s]", product_id)
        product = Product.find(product_id)
        if not product:
            abort(404, "Product with id \'{}\' was not found.".format(product_id))
        return product.serialize()

    @api.doc(\'update_products\')
    @api.expect(product_model)
    @api.marshal_with(product_model)
    def put(self, product_id):
        """ Updates a Product """
        app.logger.info("Request to update product with id [%s]", product_id)
        product = Product.find(product_id)
        if not product:
            abort(404, "Product with id \'{}\' was not found.".format(product_id))
        product.deserialize(api.payload).update()
        return product.serialize()

    @api.doc(\'delete_products\')
    @api.response(204, \'Product deleted\')
    def delete(self, product_id):
        """ Deletes a Product """
        app.logger.info("Request to delete product with id [%s]", product_id)
        product = Product.find(product_id)
        if product:
            product.delete()
            app.logger.info(\'Product with id [%s] deleted!\', product_id)
        return \'\', 204

    @api.doc(\'list_products\')
    @api.expect(product_args, validate=True)
    @api.marshal_list_with(product_model)
    def get(self):
        """ Returns all of the Products """
        app.logger.info("Request to list products...")
        products = []
        name = product_args.parse_args()[\'name\']
        category = product_args.parse_args()[\'category\']
        available = product_args.parse_args()[\'available\']

        if name:
            products = Product.find_by_name(name)
        elif category:
            products = Product.find_by_category(category)
        elif available is not None:
            products = Product.find_by_availability(available)
        else:
            products = Product.all()

        results = [product.serialize() for product in products]
        app.logger.info("Returning %d products", len(results))
        return results
