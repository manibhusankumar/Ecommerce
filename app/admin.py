from django.contrib import admin

# Register your models here.
from app.models import HomeBanner,LiveSaleSection,ShoppingX,TrendingDeals,Cart,Post

admin.site.register(HomeBanner)
admin.site.register(LiveSaleSection)
admin.site.register(ShoppingX)
admin.site.register(TrendingDeals)
admin.site.register(Cart)
admin.site.register(Post)