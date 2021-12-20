# 문제 1

## 요구사항
- 메가여성의류쇼핑몰 A가 존재한다.
- A가 메가쇼핑몰인 이유는 다음과 같다.
- A는 자사의 고유 상품을 가지고 있지 않는다. 대신,
- 타 일반여성의류쇼핑몰들(이하 마켓, 테이블명 : markets__market)의 상품들을 올려두고,
- 고객이 그것들을 한꺼번에 주문할 수 있도록, 중간다리 역할을 한다.(지마켓 같은 느낌)
- 일반여성의류쇼핑몰(마켓)이 A에서 자사의 상품을 팔고 싶다면,
- 먼저 마켓등록부터 해야 한다.
- 모든 상품(테이블 명 : products_product)은 2가지의 옵션이 있다.
- 그 옵션은 색상와 사이즈이다.(EX : RED/55, RED/66)
- 고객은 상품을 장바구니에 담을 때,
- 상품 + 상품색상 + 상품사이즈를 선택한다.
- 상품에는 일반고객이 질문을 달 수 있다.
- 각 마켓들은 자사의 상품에 달린 질문에 대해서 응답을 할 수 있다.
- 그렇게 할 수 있는 마켓사용자용 관리자 페이지가 따로 존재한다. 
- 상품은 다음과 같은 정보로 구성된다.
  - id : 주키
  - reg_date : 생성날짜
  - update_date : 수정날짜
  - name : 상품명
  - sale_name : 상품명(실제 고객에게 노출되는 이름)
  - price : 원래가격
  - sale_price : 실제판매가격(이 가격이 price 보다 낮다면, discount가 진행중이라는 뜻)
  - hide_status : 0=보임, 1=숨김(1이면 쇼핑몰에 노출되지 않는다.)
  - sold_out_status : 0=미품절, 1=품절(1이면 품절이라는 뜻)
  - market_id : 이 상품이 소속되어 있는 마켓의 번호
- 상품테이블에 필드가 더 필요하다면 추가해도 된다.
- 주문, 주문품목, 결제, 배송을 제외한 나머지 부분의 DB 설계를 진행해주세요.
- 필수적으로 필요한 테이블은 다음과 같다.
- markets_marekt : 마켓
- products_product_opt : 상품옵션
- accounts_user : 회원정보
- cart_cart_item : 장바구니아이템
- 위 테이블들을 제외하고 추가할 수 있는 테이블은 3개 입니다.
- 추가하지 않아도 전혀 문제되지 않습니다.
- 정말로 필요하다고 생각되는게 추가로 더 있다면 추가해주세요.

## 제출양식
- 필요한 테이블들을 생성할 수 있는 SQL을 작성해주세요.
- MariaDB 최신버전을 기준으로 합니다.
- 외래키는 필요없습니다.
- 장고 마이그레이션 기능이 아닌, 혼자힘으로 SQL을 작성해주세요.
- 속도를 위해 인덱스도 추가해야 합니다.
- 각각의 테이블이 완성된 후, 데이터를 3, 4개 정도 넣어주세요.

## 제출
- 아래에 직접 SQL을 입력해주세요.
- 그리고 이 파일에 pr을 날려주세요.
```sql
show TABLES;
SELECT * FROM TABLES;

# 테이블을 모두 마이그레이션으로 만들어서 클론 테이블을 하나 테스트 겸 만들어 보았습니다.
CREATE TABLE adminPage_markets_market_clone(  
	id int primary key not null auto_INCREMENT,
	name varchar(32) not null,
	price int default 0);
	
insert into `adminPage_accounts_user` (loginId, loginPw) values ('sbsst', '1234');
INSERT INTO `adminPage_accounts_user` (loginId, loginPw) VALUES ('sbs1', '1234');
INSERT INTO `adminPage_accounts_user` (loginId, loginPw) VALUES ('sbs2', '1234');
select * from `adminPage_accounts_user`;

insert into `adminPage_markets_market` (`name`, `price`) values ('블라우스',20000);
INSERT INTO `adminPage_markets_market` (`name`, `price`) VALUES ('원피스',30000);
INSERT INTO `adminPage_markets_market` (`name`, `price`) VALUES ('헤링본코트',70000);
INSERT INTO `adminPage_markets_market` (`name`, `price`) VALUES ('중청 데님',55000);
SELECT * FROM `adminPage_markets_market`;

# 인덱스 생성을 위해 추가 기준 마련. 상의 하의 등등
alter table `adminPage_products` add `productType` varchar(10) not null default 'top';
# 컬럼 위치 옮기기
alter table `adminPage_products` modify column `productType` varchar(10) after `id`;
alter table `adminPage_products` modify column `productType` varchar(10) not null default 'top';

insert into `adminPage_products` (reg_date, update_date, sale_name, sale_price, hide_status, sold_out_status, market_id_id) 
	values ('2021-05-15', '2021-06-30', '대박할인 블라우스', '15000', 0,0,1);
insert into `adminPage_products` (reg_date, update_date, sale_name, sale_price, hide_status, sold_out_status, market_id_id) 
	values ('2021-08-20', '2021-08-20', '대박할인 원피스', '20000', 0,0,2);
insert into `adminPage_products` (reg_date, update_date, sale_name, sale_price, hide_status, sold_out_status, market_id_id) 
	values ('2021-09-15', '2021-09-19', '대박할인 헤링본코트', '55000', 0,0,3);	
INSERT INTO `adminPage_products` (productType, reg_date, update_date, sale_name, sale_price, hide_status, sold_out_status, market_id_id) 
VALUES ('bottom', '2021-01-21', '2021-06-19', '대박할인 중청데님', '22000', 0,0,4);	

SELECT * FROM `adminPage_products`;
delete from `adminPage_products` where id=10;

# 잘못 입력해서 수정
update `adminPage_products` set reg_date='2021-05-15', update_date='2021-06-30' where id=1;
update `adminPage_products` set market_id_id=2 where id=2;
SELECT * FROM `adminPage_products`;

# `adminPage_products`와 `adminPage_markets_market` 조인 조회
select prod.sale_name, mark.name from `adminPage_products` as prod, `adminPage_markets_market` as mark where prod.market_id_id = mark.id;
select prod.sale_name, mark.name from `adminPage_products` as prod inner join `adminPage_markets_market` as mark on prod.market_id_id = mark.id;

#인덱스 생성
create index productTypeIndex on `adminPage_products` (productType);
SHOW INDEX FROM `adminPage_products`;
#인덱스로 조회
explain select * from `adminPage_products`; #인덱스 안탐
explain select * from `adminPage_products` where productType='bottom'; #인덱스 탐


... 계속
```





