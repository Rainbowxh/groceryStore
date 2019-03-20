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
        if(typeof new.target !== "undefined"){
            this.name = name;
        }else{
            throw new Error();
        }
    }
    let person = Person("ddd");
    let notAPerson = Person.call(person,"xxx");
```

### 箭头函数
- 箭头函数没有this绑定:和最近一层费箭头函数的this绑定,否则被设置为全局变量
- 箭头函数没有arguments

---

## 扩展对象

## 解构

## Symbol

## Set 和 Map

## Iterator 和 Generator

## 类

## Promise

## Proxy 和 Reflection
