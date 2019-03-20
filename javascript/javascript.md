# JavaScript

    Javascript含义:ECMAScript ,DOM和BOM组成的能够全面编程的一门语言
    ESCMAScript:ECMAScript是由网景的布兰登·艾克开发的一种脚本语言的标准化规范.

## 基本概念

### 1. 语法:类 C 语言的语法

- 区分大小写
- 标识符： \_abc 　\$abc
- 注释
- 严格模式

  > ECMAScript 5 的严格模式是采用具有限制性 JavaScript 变体的一种方式，从而使代码显示地 脱离“马虎模式/稀松模式/懒散模式“（sloppy）模式。
  > 严格模式不仅仅是一个子集：它的产生是为了形成与正常代码不同的语义。不支持严格模式与支持严格模式的浏览器在执行严格模式代码时会采用不同行为.  
  > 所以在没有对运行环境展开特性测试来验证对于严格模式相关方面支持的情况下，就算采用了严格模式也不一定会取得预期效果。严格模式代码和非严格模式代码可以共存，因此项目脚本可以渐进式地采用严格模式.  
  > 模式对正常的 JavaScript 语义做了一些更改。  
  > 严格模式通过抛出错误来消除了一些原有静默错误。  
  > 严格模式修复了一些导致 JavaScript 引擎难以执行优化的缺陷：有时候，相同的代码，严格模式可以比非严格模式下运行得更快。
  > 严格模式禁用了在 ECMAScript 的未来版本中可能会定义的一些语法。
  >
  > 1.  在严格模式下, 试图删除不可删除的属性时会抛出异常(之前这种操作不会产生任何效果):
  > 2.  严格模式要求一个对象内的所有属性名在对象内必须唯一。
  > 3.  严格模式要求函数的参数名唯一.
  > 4.  严格模式禁止八进制数字语法.
  > 5.  ECMAScript 6 中的严格模式禁止设置 primitive 值的属性

- 语句 : var a = 'abc';
- 关键字和保留字

### 2. 数据类型

基本数据类型有: null undefined number string boolean symbol

复杂数据类型: objec

1. typeof 操作符号
   - typeof 操作符号能够判断:undefined boolean string number object function 中的一个类型
   - typeof null 时候可能会返回 object 或者 function 根据浏览器的版本不同而定
1. Undefined
   - 含义: 变量被声明但是没有被初始化
   - `var c; console.log(c === undefined); // true`
   - 问题:　`console.log(typeof d); // undefined`使用 typeof 来检测变量的类型时候,如果变量没有声明的时候依旧会抛出 undefined
1. null
   - 含义:表示 z 还有一个值的 s 数据类型
   - `null == undefined; //true`
   - `null === undefined; // false`
   - `typeof null; // Object`
1. boolean
   - 含义: 表示 true 和 false
   - 可以被转化为 true 的方式:
     - 非空字符串
     - 非零数字
     - 任何对象:　[] {}
   - 可以被转化为 false 的方式:
     - false
     - ""
     - null
     - undefined
     - 0 and NaN
1. number
   - 含义: 表示整数和浮点数类型.
   - 浮点数字类型: `var float = 1.1;`
   - 大数类型:　`var bigdecimal = 3.125e7`
   - NaN: 本来要返回数值的操作没有返回数字，避免抛出错误
   - isNaN: 不能够被转换为数字的类型返回 true
   - parsInt: 转换为数值,能够转换不同进制的数字
1. string
   - 含义: 字符串类型
   - 在不知道转换指是 null 或者 define 时候, 使用 String()来进行转换
1. object:
   - 含义: 一组数据和服务的合集(提供服务的对象)
   - constructor(): 构造函数,保存创建当前函数的图像
   - hasOwnProperty(): 检查当前实例中是否存在(不在原型当中)
   - isPropertyof(): 是否是另一个对象的原型 比较`a._proto_ === b.prototype`
   - toString()
   - toLocalString()
   - valueOf(): 返回对象的所有数值

### 3. 操作符号

1. 一元操作符:
   ```js
   var age = 0;
   console.log(++age); //1
   console.log(age); //1
   console.log(age++); //1
   console.log(age); //2
   ```
1. 位操作符

   - NOT : 按照位数取非

   ```js
   var a = 9; //000...001001
   var b = ~a; //111...110110  b ==-10
   ```

   - AND

   ```js
   var a = 25; // 11001
   var b = 3; // 00011
   var c = a & b; // 00001 c == 1
   ```

   - OR:　可以通过交换的形式来达到交换数值的效果

   ```js
   var a = 25; //  11001
   var b = 3; //  00011
   var c = a ^ b; //  11010 c == 26
   var d = a ^ b ^ b; //  11001 d == a == 25
   function swap(a, b) {
     b = a ^ b;
     a = b ^ a;
     b = a ^ b;
   }
   ```

   - 左移: |= 异或 取出 cap 币 cap 最大的 2 的 n 次,用来分配完全二叉树

   ```js
   static final int tableSizeFor(int cap) {
       int n = cap - 1;
       n |= n >>> 1;
       n |= n >>> 2;
       n |= n >>> 4;
       n |= n >>> 8;
       n |= n >>> 16;
       return (n < 0) ? 1 : (n >= MAXIMUM_CAPACITY) ?  MAXIMUM_CAPACITY : n + 1;
   }
   ```

   - 无符号右移动
   - 有符号右移动

### 4. 语句

1. do-while: 后测语句
1. while:　前测语句
1. for-in: 用来枚举对象属性，没有顺序！！
1. break-continue: 跳出循环，跳出当前循环

### 5. 函数

1. 没有重载,可以自我实现

   ```js
   //通过判断arguments的长度来进行判断
   function overload() {
     switch (arguments.length) {
       case 1:
         break;
       case 2:
         break;
       case 3:
         break;
     }
   }
   ```

   ```js
   function addMethod(object, name, fn) {
     var old = object[name]; //把前一次添加的方法存在一个临时变量old里面
     object[name] = function() {
       // 重写了object[name]的方法
       // 如果调用object[name]方法时，传入的参数个数跟预期的一致，则直接调用
       if (fn.length === arguments.length) {
         return fn.apply(this, arguments); // 否则，判断old是否是函数，    如果是，就调用old
       } else if (typeof old === "function") {
         return old.apply(this, arguments);
       }
     };
   }
   ```

1.

## 变量作用域和内存问题

1. 基本引用类型
   - 动态属性 `var name ="Nico" name.age = 16;console.log(name) //wrong`
   - \*复制变量:
   1. q1:`var num1 = 1; var num2 = num1`;  
      其中的问题在于 num2 是否保存了 num1 的引用?  
      不是 num1 和 num2 中的值是完全独立的,1 是 num1 中的一个副本
   1. q2: 这里面 obj2 保存了 obj1 中的值的副本,但是 obj1 中保存的是一个指针,只想堆内存中的 Object()中的引用.
      ```js
      var obj1 = new Object();
      var obj2 = obj1;
      obj1.name = "Nico";
      console.log(obj2); //"Nico"
      ```
   1. 检测类型:
      - typeof: 检测基础类型的方法
      - instanceOf: 检测引用用类型的方法
      - isPropertyOf: 检测原型的方法.
1. 执行环境和作用域  
   执行环境: execution context 定义了变量或函数有权限访问其他数据
   AO 活动对象  
   scope 范围  
   execution context stack 执行栈  
    [创建函数对象](http://yanhaijing.com/es5/#239)
   ```js
   method.[[scope]] = [globalContext.vo]
   ECStack = [globalContext,methodContext]
   methodContext = {
       Scope: method.[[scope]]
   }
   methodContext = {
       AO:{undefined}
       Scope: method.[[scope]]
   }
   methodContext = {
       AO:{
           arguments: {}
           value: undefined
       }
       Scope: method.[[scope]]
   }
   methodContext = {
       AO:{
           arguments: {}
           value: undefined
       }
       Scope: [AO,method.[[scope]]]
   }
   ```


    methodContext = {
        AO:{
            arguments: {}
            value: method.value
        }
        Scope: [AO,method.[[scope]]]
    }
    ECStack  = [globalContext];
    ```

1. this 的问题  
    含义:

   > this 关键字执行为当前执行环境的 ThisBinding。  
   >  [具体流程参照](http://yanhaijing.com/es5/#151)：  
   >  [函数调用流程](http://yanhaijing.com/es5/#164)

   混乱的原因是由于 js 本身的加载机制决定的,简单的说是根据执行环境做确定的

   ```js
   fucntion foo() {
       return function(){
           console.log(this);
       }
   }
   foo()();
   //这个相当于执行了foo()  ();所在的memberexpression 为foo();
   //foo()不是引用,他是函数执行的一个结果,返回了一个匿名函数
   //这样的画就变成了 noname();
   //对于noname来说,他所在的环境是windows
   //这样隐式变成了 window.noname();
   //引用是window,name: noname
   //this绑定在当前引用或者环境上
   //this-> window
   ```

1. gc 机制
   - 标记清楚: 进入环境{,标记,出环境}消除
   - 计数清楚: 少用闭包,可能造成内存泄露

## 引用类型

1. Object
1. Array

   - `Array instanceof Array` or `Object.prototype.toString.call(arr) == [Object Array]`
   - `valueOf`: 返回数组 ; `toString`返回逗号相隔开的字符串
   - 栈方法:`push` `pop`
   - 队列方法:
     - `shift` : 移除数组的第一项并且能够返回该项
     - `unshift`: 在数组的前段添加任一项数并且返回新数组的长度
   - 重排序:
     - `sort`:
   - 操作方式:
     - `slice`: 基于当前数组,创建一或者多项数组
       - `slice(n)` 从 n 项开始到最后,分割
       - `slice(start,end)` 从 start 到 end 项数分割
       - `slice(-1,-2)`从倒数一个到倒数两个分割
     - `splice` :
       - `splice(n,x)` 从 n 项开始删除 x 个,返回新数组
       - `splice(n,x,sth)` 从 n 项开始删除 x 个并添加 sth
   - 位置方法
     - `indexOf` 从头开始查找,如果有返回项数,如果没有则返回-1
   - 迭代方法

     - `every`
     - `filter`

     ```

     ```

     - `forEach`
     - `map`
     - `some`: 如果有一个满足就返回 true

   - 缩小方法:
     - `reduce`

1. Date
1. RegExp
1. Function
   - 没有重载,后定义的会覆盖前面定义的函数
   - 函数声明: `function a() {}` 函数声明会变量提升
   - 函数表达式: `var a = function(){}` 函数表达式不会变量提升
   - 函数的属性和方法:
     - `Method.call(this,a,b,c)`
     - `Method.apply(this,arguments)`
     ```js
     //simpple Realized
     Object.prototype.callRealize(object,fn,arguments){
         object.fn = this;
         object.fn();
         delete object.fn
     }
     ```
1. 包装类型
   - boolean
   - number
   - string
1. 内置对象
   - global
   - math

## 面向对象设计

1. 对象: 具有属性能够提供服务的集合(卧姿挤硕得)

```js
var person = new Object()
person.name = "nico";
person.age = 29;
person.sayName = function() {
    alert(this.name)
}
Object.prototype.sayAge = function() {
    alert(this.name)
}
function Object(){
    var obj = {},
    obj._proto_ = Object.prototye
    Object.call(obj)
}
```

- 属性类型
  - `__configureable__`
  - `Enumerable`: 能否被 for-in 返回 默认 true
  - `value`: 数据属性
  - `writeable`: 是否可写
- 访问器具属性:  
   访问器具属性不包含数值,包含 getter 和 setter 属性(vue 的双向数据绑定基于此处)

  - `configurable` 能否修改属性,默认 true
  - `enumerable` 能否被修改
  - `getter` 默认值为 undefined
  - `set` 默认值为 undefined

  访问器属性不能够直接定义,使用`Object.definProperty`来使用.同时可以使用`Object.defineProperties`来定义多个属性  
   通过`Object.getOwnPropertyDescriptor`来过去给定属性的匹配方式,并且可以设置

1.  创建对象

    - 设计模式中的工厂模式

      ```typescript
      class Factory {
        constructor() {}
        public create(onwer: String): Product {
          let p = createProduct(owner);
          return p;
        }
        public createProduct(owner: String): Product {
          return new Product(owner);
        }
      }
      class Product {
        private name: String;
        constructor(name) {
          this.name = name;
        }
        public use(): void {
          console.log(name + " used");
        }
        public getUser(): String {
          return this.name;
        }
      }
      ```

    - 构造函数函数

      ```js
      function person(name, age) {
        this.name = name;
        this.age = age;
        this.showName = function() {
          console.log(this.name);
        };
      }
      let person1 = new Person("nico", 19);
      let person2 = new Person("Kirito", 19);
      ```

      - 隐式创建了新的对象,并将属性和方法给了新对象
      - 没有 return
      - 利用构造函数创建实例,需要在每个例子中需要绑定一个方法

    - 原型模式
      ```js
      function Person(name) { this.name = "elicxh"}
      Person.prototype.say = function() {alert(this.name)}
      Person.prototype.ss = () => {alert(this.name))}
      let person1 = new Person("abc");
      person1.say() // abc
      person1.ss() // elicxh 可以用来确定原型中的数值是什么,利用箭头函数
      ```
    - 原型问题
      ```js
      function Person() {}
      let person1 = new person();
      /**
       * 其中的关系可以分为两部分:
       * 1.对于person这个类来说:
       *  console.log(Person) : ƒ Person() {}
       *  console.log(Person.prototype): 
            {constructor: f Person
             __proto__: Object}
       *  Person.prototype ---->> Person Prototype
       *  Person Prototype.constructor ---->> Person
       * 简单的来说 Person指向了Person.prototype,同时*Person.protype.consturctor 指向了Person(prototype会无线循环)
       * 2.对于person1这个实例,
       *  person1.__proto___ 属性指向 Person Prototype
       *  person1.__proto__ ===>>> person1.protoype
      */
      ```
      但是这样做会有一个明显的缺点,如果 Person 中有修改其本身值的函数,则会造成所有原型链上的所有属性进行修改.  
       特别注意几种情况:
      ```js
          function Person() {}
          //这里生成的person　是指向没有修改的Person prototype
          let person = new Person();
          //修改了Person中的prototype
          Person.prototype.sayName() {alert(name)}
          //切断了原型,如果要这么定义,放在一切生成实例之前.
          Person.prototype= {
              name: "ncio";
          }
          //新建了一个Person对象
          let person1 = new Person();
      ```

1.  继承

- 原型链  
   基本思想:利用原型让一个引用类型继承灵异了引用类型的属性和方法．

  ```js
  function A() {
    this.propertyA = "a";
  }
  A.prototype.say = function() {
    return this.property;
  };
  function B() {
    this.propertyB = "b";
  }
  //继承了A
  B.prototype = new A();
  B.prototype.abc = function() {
    return this.propertyB;
  };
  ```

  谨慎使用此方法,不能够直接替换 B.prototype = {} 会导致 new A() 失效

- 构造函数继承
  ```js
  function Father(name) {
    this.name = name;
  }
  function Son() {
    //相当于调用了父类的属性,不能够继承Father.prototype中的方法和属性
    Father.call(this, "Father");
    //添加了实例属性
    this.name = "Son";
  }
  //但是会造成,无法函数复用
  Father.isPrototypeOf(Son) === false;
  ```
- 组合继承
  ```js
  function Father(name) {
    this.name = name;
  }
  Father.prototype.getName = function() {
    console.log(this.name);
  };
  function Son() {
    //相当于调用了父类的属性,第一次调用构造器
    Father.call(this, "Father");
    //添加了实例属性
    this.name = "Son";
  }
  //第二次调用了构造器
  Son.prototype = new Fater();
  Son.prototype.method = function() {
    console.log("this is a method");
  };
  ```
- 原型继承: 在 es5 中被 规范为新的`Object.create()` 但是这样做会让所有实例共享继承的属性.
  ```js
  function object(obj) {
    //新建端详
    function F() {}
    //构造原型
    F.prototype = obj;
    //返回新的对象
    return new F();
  }
  ```
- 寄生式继承
  ```js
  function createAnoter(origin) {
    // 创建了新的对象
    let clone = object(original);
    // 完善对象,缺少复用性质
    clone.sayHi = function() {
      alert("hight");
    };
    // 返回对象
    return clone;
  }
  ```
- 寄生组合式寄生

  ```js
  //只调用一次构造器进行复制
  //继承Father共享方法
  function inherit(s, f) {
    //复制,新建一个对象
    let proto = new Object(f.proto);
    console.log(proto);
    proto.constructor = s;
    s.proto = proto;
    //f.prototype = f;
  }
  //继承父类的属性
  function Father(name) {
    this.name = name;
  }
  Father.prototype.getName = function() {
    console.log(this.name);
  };
  function Son() {
    Father.call(this, "elicxh");
    this.age = 11;
  }

  //Son.prototype = new Father();
  inherit(Son, Father);
  let a1 = new Son();
  ```

## 函数表达式

1. 函数声明通常为: `funtion functionName(arg1,arg2){}`  
   函数表达式为:　`var a = function(arg1,arg2){}`或者是`var c = function cd(arg1,ag2){}` cd 没有什么用
   函数表达式中的匿名函数部分不会存在函数提升.
1. 闭包: 有权限访问另一个函数作用域中的变量的函数.(并不是通常所说函数中的另一个函数,只是一种常见的创建方式.)
   - 闭包只能取得函数变量中的最后一个值,他保存的整个变量对象.
   ```js
   function createFunctions() {
     var result = new Array();
     for (var i = 0; i < 10; i++) {
       result[i] = function() {
         return i;
       };
     }
     return result;
   }
   ```
   ```js
   //resolve
   function createFunctions() {
     var result = new Array();
     for (var i = 0; i < 10; i++) {
       result[i] = (function(num) {
         return function(num) {
           return num;
         };
       })(i);
     }
     return result;
   }
   ```
1. 闭包中的 this:

   ```js
   name = "windows";
   var obj = {
     name: "obj",
     getName: function() {
       console.log(this);
       return function() {
         return this.name;
       };
     }
   };
   obj.getName()();
   /*分成两部分来看
    *第一部分为: (obj.getName())(); 执性Memeber做部分为obj.getName() Let ref be the result of evaluating MemberExpression.;首先他不是一个引用ref,也不是一个有效的值,则环境指向undefined,由于当前作用环境是windows,所以this隐式只想window
    第二部分是:obj.getName(); 由于执行部分左侧是 obj.getName;
    obj.getName是一个引用,值也是引用,获取GetBase(obj.getName) = obj
    所以obj.getName中的this为 obj
    */
   ```

   注意变量回收

1. 模仿块级作用

   ```js
   function outputNum(count) {
     //函数生命转化内函数表达式,立即执行,退出活动区域AO,外部访问不了内部的属性
     (function() {
       for (var i = 0; i < count; i++) {
         alert(i);
       }
     })();
   }
   ```

1. 模仿私有变量
   ```js
   function MyObject() {
     //使用var的方式外部访问不了
     var privateValue = 20;
     function privateFunction() {
       return false;
     }
     this.publicMethod = function() {
       this.privateValue += privateValue;
     };
   }
   ```
   ```js
   function Person(name) {
     this.getName = function() {
       return this.name;
     };
     this.setName = function(value) {
       this.name = value;
     };
   }
   ```
1. 模仿静态变量

   ```js
   (function() {
       var private = 10
       function do() {}
       //全局作用与
       Myobj = function() {

       }
       Myobj.prototype.method = function() {

       }
   })();
   ```

1. 单例模式

   ```js
   var singleton = function() {
       let private  = 10;
       //特权方法
       function privateFunction() {
           return false;
       }
       //返回对象
       return {
           publicProperty: true,
           publicMethod: function() {
               private++;
               return privateFunction() {

               }
           }
       }
   }
   ```

   ```js
   var singleton = function() {
     let privateValue = 1;
     //特权方法
     function privateFunc() {
       return fasle;
     }
     //添加共有方法
     let obj = new CustomType();
     obj.publicProperty = true;
     obj.publicMethod = function() {};
     return obj;
   };
   ```

## 常用 BOMCAOZUO

## 常用 DOM 操作

    ```
    documet
    --element html
      --element head
        --element title
          --text page
    --element body
      --element p
        --text hello world
    ```
- Node
    - appenChild()
    - insertBefore
- Document
    - nodeType的值为9
    - nodeName 为#doucment
    - document.title
    - documnet.getElementById("myDiv")
    - document.getElementByTagName("img")
- Element
    - nodeType的值为1
    - nodeName 为元素的标签的名字
    - id
    - title
    - lang
    - className
    - document.createElement
- Text
    - nodeType = 3
    - nodeName "#Text"