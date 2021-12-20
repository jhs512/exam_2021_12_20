from django.db import models

# Create your models here.

#todo
# - id : 주키
#   - reg_date : 생성날짜
#   - update_date : 수정날짜
#   - name : 상품명
#   - sale_name : 상품명(실제 고객에게 노출되는 이름)
#   - price : 원래가격
#   - sale_price : 실제판매가격(이 가격이 price 보다 낮다면, discount가 진행중이라는 뜻)
#   - hide_status : 0=보임, 1=숨김(1이면 쇼핑몰에 노출되지 않는다.)
#   - sold_out_status : 0=미품절, 1=품절(1이면 품절이라는 뜻)
#   - market_id : 이 상품이 소속되어 있는 마켓의 번호

class markets_market (models.Model):
    name = models.CharField(max_length=20, default='')
    price = models.IntegerField(default=0)

class products(models.Model):
    reg_date = models.DateTimeField()
    update_date = models.DateTimeField()
    sale_name = models.CharField(max_length=20, default='')
    sale_price = models.IntegerField(default=0)
    hide_status = models.BooleanField(default=0)
    sold_out_status = models.BooleanField(default=0)
    market_id = models.ForeignKey(markets_market, on_delete=models.CASCADE)


class products_product_opt (models.Model):
    name = models.ForeignKey(markets_market, on_delete=models.CASCADE)
    color = models.CharField(max_length=20, default='white')
    size = models.CharField(max_length=20, default='s')

class accounts_user(models.Model):
    loginId = models.CharField(max_length=20, default='')
    loginPw = models.CharField(max_length=20, default='')


# class cart_cart_item(models.Model):
