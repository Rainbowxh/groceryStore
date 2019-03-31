# ES6

## 块级作用于绑定

### let 和 const 声明

1. let 将变量的作用域限制在当前代码块中,并且失去作用于提升.(临时死区)
1. let 禁止重复声明
1. const 是 let 的超集,一旦声明不能够更爱.
1. 再循环体中,使用 let 定义的变量将不能够在外部访问
1. 在循环闭包中,不需要调用函数表达式
   ```js
   for (let i = 0; i < 10; i++) {
     funs.push(function() {
       console.log(i);
     });
   }
   // 0,1,2,3,4,5,6,7,8,9
   ```
1. key-in 操作的时候 const

---

## 字符串和正则表达式

---

## 函数

### 函数参数的默认值

```js
function Request(url, timeout = 200) {}
```

```js
function getValue() {
  return 5;
}
function set(first, second = getValue()) {}
set(1); // 6
```

### 默认的临时死区域

- 函数的默认值不能够访问函数体内部的声明变量

### 内建运算符

```js
let math = [1, 2, 3, 4, 5];
Math.max(...math);
```

### name 属性

- 添加默认属性
  ```js
  function sth() {}
  console.log(sth.name); //sth
  ```

### new.target

```js
function Person() {
  if (typeof new.target !== "undefined") {
    this.name = name;
  } else {
    throw new Error();
  }
}
let person = Person("ddd");
let notAPerson = Person.call(person, "xxx");
```

### 箭头函数

- 箭头函数没有 this 绑定:和最近一层费箭头函数的 this 绑定,否则被设置为全局变量
- 箭头函数没有 arguments

---

## 扩展对象

## 解构

## Symbol

私有名称的创建非字符串属性名称设计的

- symbol 的使用

```js
let firstname = new Symbol();
let person = [];
person[firstname] = "nico";
console.log(person[firstname]);
```

---

## Set 和 Map

### Set 集合

- 定义:st 是一种含有 相互独立 非重复值 的一种有序列表
- 不同属性的值不会进行强制转
- 使用: `let set = new Set([1,2,3])`
- 转化为数组: `array = [...set]`

### Map 的使用

- 定义: Map 是一种存储着许多 键值对 的有序表,
- 使用:　`let map = new Map(); map.set(key,value)`
- 方法: 和 Set 集合通用方法
  - `has(key)`
  - `delete(key)`
  - `clear()`
- 遍历: `map.forEach((value,key,ownerMap) => {})`

---

## Iterator 和 Generator

### Iterator 迭代器

- 定义:专门为迭代过程设计的专有接口，有 next 方法,每次调用都返回 value

### Generator 生成器

- 定义: 返回迭代器的一种函数, 使用`function *Generator()`来
- 使用:

```js
function* createGenerator() {
  for (let i = 0; i < 10; i++) {
    yield i;
  }
}
console.log(createGenerator.next());
console.log(createGenerator.next());
console.log(createGenerator.next());
```

- 默认迭代器: `let num of items`只里面 js 默认迭代器
- 创建可迭代的对象

```js
let collection = {
    items: [];
    *[Symbol.iterator]() {
        for(let item of items){
            yield item;
        }
    }
}
items.push(1);
items.push(2);
items.push(3);
for (let x of collection){
    console.log(x) // 1,2,3
}
```
### 集合对象
在js中有三种集合对象`Map,Array,Set`,当中包含了三种迭代器
- `entries()` 多个键值对`[key,value]`
- `values` 为集合的值 `value`
- `keys()` 为键值 `key`

### 字符串迭代器
- 使用: `let key = "abcdeee"; for(let c of message){}`

### NodeList 迭代器
- 使用 `let divs = document.getElementByTagName(div); fo(let div of divs){}`
---


## Promise

这里放一篇文章,目前认为是我看过写的最好的一篇,没有之一  
[Javascript Promise简介](https://developers.google.com/web/fundamentals/primers/promises?hl=zh-cn)  
[异步函数 - 提高 Promise 的易用性](https://developers.google.com/web/fundamentals/primers/async-functions?hl=zh-cn)

---

## Proxy 和 Reflection
