from rest_framework import serializers

from logistic.models import Product, Stock, StockProduct


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ['title', 'description']


class ProductPositionSerializer(serializers.ModelSerializer):
    class Meta:
        model = StockProduct
        fields = ['product', 'quantity', 'price']


class StockSerializer(serializers.ModelSerializer):
    positions = ProductPositionSerializer(many=True)

    class Meta:
        model = Stock
        fields = ['address', 'positions']

    def create(self, validated_data):
        positions = validated_data.pop('positions')
        stock = super().create(validated_data)
        for position in positions:
            StockProduct.objects.create(stock=stock, **position)
        return stock

    def update(self, instance, validated_data):
        positions_data = validated_data.pop('positions')
        stock = super().update(instance, validated_data)
        for position_data in positions_data:
            product = position_data['product']
            quantity = position_data['quantity']
            price = position_data['price']
            position = StockProduct.objects.filter(stock=instance, product=product).first()
            if position is not None:
                position.quantity = quantity
                position.price = price
                position.save()
            else:
                StockProduct.objects.create(stock=instance, product=product, quantity=quantity, price=price)
        return stock
