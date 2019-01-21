import graphene

from graphene_django.types import DjangoObjectType

from marketplace_cart.models import Product, Cart, MetaCart
# from marketplace_backend.marketplace_car.models import Product, Cart


class ProductType(DjangoObjectType):
    class Meta:
        model = Product

class CartType(DjangoObjectType):
    class Meta:
        model = Cart

class MetaCartType(DjangoObjectType):
    class Meta:
        model = MetaCart

class PurchaseProduct(graphene.Mutation):
    class Arguments:
        id = graphene.String()
    purchase_successful = graphene.Boolean()
    product = graphene.Field(ProductType)

    @staticmethod
    def mutate(root, info, id, **input):
        purchase_successful=False
        product_retrieved = Product.objects.get(pk=id)
        if product_retrieved.inventory_count !=0:
            purchase_successful=True
            product_retrieved.inventory_count-=1
            product_retrieved.save()

        return PurchaseProduct(purchase_successful=purchase_successful)

class Mutation(graphene.ObjectType):
    purchase_product = PurchaseProduct.Field()

class Query(object):
    all_product = graphene.List(ProductType)
    
    product = graphene.Field(ProductType,id=graphene.Int())
    
    all_cart = graphene.List(CartType)
    # all_ingredients = graphene.List(IngredientType)

    def resolve_all_product(self,info):
        return Product.objects.all()

    def resolve_all_cart(self,info):
        return Cart.objects.all()

    def resolve_product(self, info, **kwargs):
        id = kwargs.get('id')
        title = kwargs.get('title')
        price = kwargs.get('price')
        inventory_count = kwargs.get('inventory_count')

        if id is not None and inventory_count !=0 :
            return Product.objects.get(pk=id)
        return None

