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
DROP DATABASE IF EXISTS mega_shop;
CREATE DATABASE mega_shop;
USE mega_shop;

CREATE TABLE products_product (
    size INT(10) NOT NULL, 
    color VARCHAR(30) NOT NULL,
    product_id INT AUTO_INCREMENT UNIQUE NOT NULL, 
    `comment` TEXT,
    reg_date DATETIME NOT NULL,
    PRIMARY KEY(product_id)
);

DROP TABLE products_product;

INSERT INTO products_product
SET size = 44,
color = 'RED',
product_id = 1,
reg_date = NOW();

INSERT INTO products_product
SET size = 55,
color = 'BLUE',
reg_date = NOW();

INSERT INTO products_product
SET size = 66,
color = 'GREEN',
reg_date = NOW();

SELECT *
FROM products_product;

DROP TABLE markets_market;

CREATE TABLE markets_market (
    market_id INT AUTO_INCREMENT UNIQUE NOT NULL,
    market_name TEXT NOT NULL,
    PRIMARY KEY(market_id)

);

INSERT INTO markets_market
SET market_id = 1,
market_name = 'A';

INSERT INTO markets_market
SET market_name = 'B';

INSERT INTO markets_market
SET market_name = 'C';

SELECT *
FROM markets_market;

CREATE TABLE products_product_opt (
    size INT(10) NOT NULL,
    color VARCHAR(30) NOT NULL,
    product_id INT AUTO_INCREMENT UNIQUE,
    reg_date DATETIME NOT NULL,
    update_date DATETIME,
    product_name VARCHAR(100) NOT NULL,
    sale_name VARCHAR(100) NOT NULL,
    price INT(20) NOT NULL,
    sale_price INT(20),
    hide_status INT(1) NOT NULL,
    sold_out_status INT(1) NOT NULL,
    market_id INT NOT NULL, 
    PRIMARY KEY(product_id)

);

DROP TABLE products_product_opt;

INSERT INTO products_product_opt
SET size = 55,
color = 'RED',
reg_date = NOW(),
update_date = NULL,
product_name = '코트',
sale_name = '코트',
price = 60000,
sale_price = 60000,
hide_status = 0,
sold_out_status = 0,
market_id = 1;

INSERT INTO products_product_opt
SET size = 55,
color = 'BLUE',
reg_date = NOW(),
update_date = NULL,
product_name = '조끼',
sale_name = '조끼',
price = 50000,
sale_price = 50000,
hide_status = 0,
sold_out_status = 0,
market_id = 2;

INSERT INTO products_product_opt
SET size = 44,
color = 'BLACK',
reg_date = NOW(),
update_date = NULL,
product_name = '셔츠',
sale_name = '셔츠',
price = 100000,
sale_price = 100000,
hide_status = 0,
sold_out_status = 0,
market_id = 1;

SELECT *
FROM products_product_opt;

CREATE TABLE account_user (
    account_id INT AUTO_INCREMENT UNIQUE NOT NULL,
    email VARCHAR(100) NOT NULL,
    PRIMARY KEY(account_id)
    
);

INSERT INTO account_user
SET account_id = 1,
email = 'ABC@gmail.com';

INSERT INTO account_user
SET email = 'ABC@gmail.com';

INSERT INTO account_user
SET email = 'ABCDEF@gmail.com';

SELECT *
FROM account_user;

CREATE TABLE cart_cart_item (
    product_id INT NOT NULL,
    account_id INT UNIQUE NOT NULL,
    sale_name VARCHAR(100) NOT NULL,
    sale_price INT(20)
    
);

DROP TABLE cart_cart_item;

INSERT INTO cart_cart_item
SET product_id = 3,
account_id = 1,
sale_name = '셔츠',
sale_price = 100000;

SELECT *
FROM cart_cart_item;
```





